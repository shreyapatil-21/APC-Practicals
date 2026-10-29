import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

# Import our custom modules
from models       import create_item          # Polymorphism classes
from file_handler import log_activity, export_to_csv, read_recent_logs  # File handling

app = Flask(__name__)
app.secret_key = "college_lost_and_found_secret_key_2024"


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------

def get_db_connection():
    """Return a SQLite connection with Row factory enabled."""
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create (or migrate) the items table when the application starts."""
    conn = None
    try:                                            # EXCEPTION HANDLING
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                item_type   TEXT NOT NULL,
                item_name   TEXT NOT NULL,
                category    TEXT NOT NULL,
                location    TEXT NOT NULL,
                date        TEXT NOT NULL,
                description TEXT,
                contact     TEXT,
                status      TEXT NOT NULL DEFAULT 'Open'
            )
        """)
        # Migration — add new columns to existing databases
        existing = [r[1] for r in cursor.execute("PRAGMA table_info(items)")]
        if "contact" not in existing:
            cursor.execute("ALTER TABLE items ADD COLUMN contact TEXT")
        if "status" not in existing:
            cursor.execute("ALTER TABLE items ADD COLUMN status TEXT NOT NULL DEFAULT 'Open'")
        conn.commit()
        log_activity("STARTUP", extra="Database initialised successfully")

    except Exception as e:                          # EXCEPTION HANDLING
        print(f"[ERROR] Database init failed: {e}")

    finally:                                        # EXCEPTION HANDLING
        if conn:
            conn.close()


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CATEGORIES = ["Electronics", "Books", "Documents", "Accessories",
              "Clothing", "ID Card", "Keys", "Other"]


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    """Home page — items with optional type + category filter."""
    filter_type     = request.args.get("filter",   "All")
    filter_category = request.args.get("category", "All")

    conn = None
    try:                                            # EXCEPTION HANDLING
        conn = get_db_connection()

        conditions, params = [], []
        if filter_type in ("Lost", "Found"):
            conditions.append("item_type = ?")
            params.append(filter_type)
        if filter_category != "All" and filter_category in CATEGORIES:
            conditions.append("category = ?")
            params.append(filter_category)

        where  = ("WHERE " + " AND ".join(conditions)) if conditions else ""
        items  = conn.execute(f"SELECT * FROM items {where} ORDER BY id DESC", params).fetchall()

        total   = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
        lost    = conn.execute("SELECT COUNT(*) FROM items WHERE item_type='Lost'").fetchone()[0]
        found   = conn.execute("SELECT COUNT(*) FROM items WHERE item_type='Found'").fetchone()[0]
        claimed = conn.execute("SELECT COUNT(*) FROM items WHERE status='Claimed'").fetchone()[0]

        cat_counts = {}
        for cat in CATEGORIES:
            cat_counts[cat] = conn.execute(
                "SELECT COUNT(*) FROM items WHERE category=?", (cat,)
            ).fetchone()[0]

        stats = {"total": total, "lost": lost, "found": found, "claimed": claimed}
        return render_template("index.html", items=items, stats=stats,
                               filter_type=filter_type, filter_category=filter_category,
                               categories=CATEGORIES, cat_counts=cat_counts)

    except Exception as e:                          # EXCEPTION HANDLING
        flash(f"Error loading items: {str(e)}", "error")
        return render_template("index.html", items=[], stats={},
                               filter_type="All", filter_category="All",
                               categories=CATEGORIES, cat_counts={})

    finally:                                        # EXCEPTION HANDLING
        if conn:
            conn.close()


@app.route("/item/<int:id>")
def item_detail(id):
    """Full detail view for a single item."""
    conn = None
    try:                                            # EXCEPTION HANDLING
        conn = get_db_connection()
        item = conn.execute("SELECT * FROM items WHERE id=?", (id,)).fetchone()
        if item is None:
            flash("Item not found.", "error")
            return redirect(url_for("home"))
        return render_template("item_detail.html", item=item)

    except Exception as e:                          # EXCEPTION HANDLING
        flash(f"Error fetching item: {str(e)}", "error")
        return redirect(url_for("home"))

    finally:                                        # EXCEPTION HANDLING
        if conn:
            conn.close()


@app.route("/lost", methods=["GET", "POST"])
def lost():
    """Report a lost item."""
    if request.method == "POST":
        item_name   = request.form.get("item_name",   "").strip()
        category    = request.form.get("category",    "").strip()
        location    = request.form.get("location",    "").strip()
        date        = request.form.get("date",        "").strip()
        description = request.form.get("description", "").strip()
        contact     = request.form.get("contact",     "").strip()

        if not item_name or not category or not location or not date:
            flash("Please fill in all required fields.", "error")
            return render_template("lost.html")

        conn = None
        try:                                        # EXCEPTION HANDLING
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO items (item_type,item_name,category,location,date,description,contact,status) "
                "VALUES (?,?,?,?,?,?,?,'Open')",
                ("Lost", item_name, category, location, date, description, contact)
            )
            conn.commit()

            # Polymorphism — create a LostItem object and use its get_summary()
            item_obj = create_item("Lost", item_name, category, location, date, description, contact)
            log_activity("REPORT", item_name=item_name, item_type="Lost",
                         extra=item_obj.get_summary())    # FILE HANDLING + POLYMORPHISM

            flash("Lost item reported successfully.", "success")
            return redirect(url_for("home"))

        except Exception as e:                      # EXCEPTION HANDLING
            flash(f"Could not save report: {str(e)}", "error")
            return render_template("lost.html")

        finally:                                    # EXCEPTION HANDLING
            if conn:
                conn.close()

    return render_template("lost.html")


@app.route("/found", methods=["GET", "POST"])
def found():
    """Report a found item."""
    if request.method == "POST":
        item_name   = request.form.get("item_name",   "").strip()
        category    = request.form.get("category",    "").strip()
        location    = request.form.get("location",    "").strip()
        date        = request.form.get("date",        "").strip()
        description = request.form.get("description", "").strip()
        contact     = request.form.get("contact",     "").strip()

        if not item_name or not category or not location or not date:
            flash("Please fill in all required fields.", "error")
            return render_template("found.html")

        conn = None
        try:                                        # EXCEPTION HANDLING
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO items (item_type,item_name,category,location,date,description,contact,status) "
                "VALUES (?,?,?,?,?,?,?,'Open')",
                ("Found", item_name, category, location, date, description, contact)
            )
            conn.commit()

            # Polymorphism — create a FoundItem object and use its get_summary()
            item_obj = create_item("Found", item_name, category, location, date, description, contact)
            log_activity("REPORT", item_name=item_name, item_type="Found",
                         extra=item_obj.get_summary())    # FILE HANDLING + POLYMORPHISM

            flash("Found item reported successfully.", "success")
            return redirect(url_for("home"))

        except Exception as e:                      # EXCEPTION HANDLING
            flash(f"Could not save report: {str(e)}", "error")
            return render_template("found.html")

        finally:                                    # EXCEPTION HANDLING
            if conn:
                conn.close()

    return render_template("found.html")


@app.route("/search")
def search():
    """Search items by name, category, or location."""
    query = request.args.get("q", "").strip()
    items = []

    if query:
        conn = None
        try:                                        # EXCEPTION HANDLING
            pattern = f"%{query}%"
            conn    = get_db_connection()
            items   = conn.execute(
                "SELECT * FROM items "
                "WHERE item_name LIKE ? OR category LIKE ? OR location LIKE ? "
                "ORDER BY id DESC",
                (pattern, pattern, pattern)
            ).fetchall()
            log_activity("SEARCH", extra=f"Query='{query}', Results={len(items)}")

        except Exception as e:                      # EXCEPTION HANDLING
            flash(f"Search error: {str(e)}", "error")

        finally:                                    # EXCEPTION HANDLING
            if conn:
                conn.close()

    return render_template("search.html", items=items, query=query)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    """Edit item details — item_type cannot be changed."""
    conn = None
    try:                                            # EXCEPTION HANDLING
        conn  = get_db_connection()
        item  = conn.execute("SELECT * FROM items WHERE id=?", (id,)).fetchone()

        if item is None:
            flash("Item not found.", "error")
            return redirect(url_for("home"))

        if request.method == "POST":
            item_name   = request.form.get("item_name",   "").strip()
            category    = request.form.get("category",    "").strip()
            location    = request.form.get("location",    "").strip()
            date        = request.form.get("date",        "").strip()
            description = request.form.get("description", "").strip()
            contact     = request.form.get("contact",     "").strip()

            if not item_name or not category or not location or not date:
                flash("Please fill in all required fields.", "error")
                return render_template("edit.html", item=item)

            conn.execute(
                "UPDATE items SET item_name=?,category=?,location=?,date=?,description=?,contact=? WHERE id=?",
                (item_name, category, location, date, description, contact, id)
            )
            conn.commit()
            log_activity("EDIT", item_name=item_name, item_type=item["item_type"],
                         extra=f"ID={id}")       # FILE HANDLING

            flash("Item updated successfully.", "success")
            return redirect(url_for("home"))

        return render_template("edit.html", item=item)

    except Exception as e:                          # EXCEPTION HANDLING
        flash(f"Error updating item: {str(e)}", "error")
        return redirect(url_for("home"))

    finally:                                        # EXCEPTION HANDLING
        if conn:
            conn.close()


@app.route("/mark_claimed/<int:id>")
def mark_claimed(id):
    """Toggle item status between Open and Claimed."""
    conn = None
    try:                                            # EXCEPTION HANDLING
        conn = get_db_connection()
        item = conn.execute("SELECT status, item_name, item_type FROM items WHERE id=?", (id,)).fetchone()

        if item is None:
            flash("Item not found.", "error")
            return redirect(url_for("home"))

        new_status = "Open" if item["status"] == "Claimed" else "Claimed"
        conn.execute("UPDATE items SET status=? WHERE id=?", (new_status, id))
        conn.commit()
        log_activity("STATUS", item_name=item["item_name"],
                     item_type=item["item_type"], extra=f"→ {new_status}")  # FILE HANDLING

        msg = "Item marked as Claimed." if new_status == "Claimed" else "Item marked as Open again."
        flash(msg, "success")

    except Exception as e:                          # EXCEPTION HANDLING
        flash(f"Error updating status: {str(e)}", "error")

    finally:                                        # EXCEPTION HANDLING
        if conn:
            conn.close()

    return redirect(url_for("home"))


@app.route("/delete/<int:id>")
def delete(id):
    """Delete an item from the database."""
    conn = None
    try:                                            # EXCEPTION HANDLING
        conn = get_db_connection()
        item = conn.execute("SELECT item_name, item_type FROM items WHERE id=?", (id,)).fetchone()
        if item:
            conn.execute("DELETE FROM items WHERE id=?", (id,))
            conn.commit()
            log_activity("DELETE", item_name=item["item_name"],
                         item_type=item["item_type"], extra=f"ID={id}")  # FILE HANDLING
        flash("Item deleted successfully.", "success")

    except Exception as e:                          # EXCEPTION HANDLING
        flash(f"Error deleting item: {str(e)}", "error")

    finally:                                        # EXCEPTION HANDLING
        if conn:
            conn.close()

    return redirect(url_for("home"))


@app.route("/export")
def export():
    """Export all items to a CSV file (File Handling demonstration)."""
    conn = None
    try:                                            # EXCEPTION HANDLING
        conn   = get_db_connection()
        items  = conn.execute("SELECT * FROM items ORDER BY id DESC").fetchall()
        fname  = export_to_csv(items)              # FILE HANDLING — CSV write
        flash(f"Exported {len(items)} item(s) successfully! File saved: {fname}", "success")

    except Exception as e:                          # EXCEPTION HANDLING
        flash(f"Export failed: {str(e)}", "error")

    finally:                                        # EXCEPTION HANDLING
        if conn:
            conn.close()

    return redirect(url_for("home"))


@app.route("/logs")
def logs():
    """View recent activity logs (File Handling demonstration)."""
    try:                                            # EXCEPTION HANDLING
        entries = read_recent_logs(80)             # FILE HANDLING — file read
    except Exception as e:                          # EXCEPTION HANDLING
        entries = [f"Error reading logs: {str(e)}"]
    return render_template("logs.html", entries=entries)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)