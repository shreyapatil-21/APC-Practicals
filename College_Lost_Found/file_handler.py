# ============================================================
# file_handler.py
# Demonstrates: File Handling (open, read, write, append, CSV)
# ============================================================

import os
import csv
from datetime import datetime

# --- Directory & file paths ---
LOG_DIR    = "logs"
EXPORT_DIR = "exports"
LOG_FILE   = os.path.join(LOG_DIR, "activity.log")


def ensure_directories():
    """Create logs/ and exports/ folders if they do not exist."""
    os.makedirs(LOG_DIR,    exist_ok=True)
    os.makedirs(EXPORT_DIR, exist_ok=True)


# ==============================================================
# FILE WRITE — Append Mode
# ==============================================================
def log_activity(action, item_name="", item_type="", extra=""):
    """
    Append a timestamped log entry to activity.log.

    FILE HANDLING — Opens file in APPEND mode ('a') so existing
    entries are kept and the new line is added at the bottom.
    """
    ensure_directories()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = (f"[{timestamp}]  {action:<12} | "
            f"Type: {item_type:<6} | "
            f"Item: {item_name}")
    if extra:
        line += f" | {extra}"

    # Open in APPEND mode — file is created if it doesn't exist
    with open(LOG_FILE, "a", encoding="utf-8") as f:   # FILE HANDLING
        f.write(line + "\n")


# ==============================================================
# FILE WRITE — CSV Write Mode
# ==============================================================
def export_to_csv(items):
    """
    Export all reported items to a CSV file.

    FILE HANDLING — Opens a new file in WRITE mode ('w') and uses
    the csv.writer to write structured rows.

    Returns the full path of the created CSV file.
    """
    ensure_directories()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename  = os.path.join(EXPORT_DIR, f"items_export_{timestamp}.csv")

    # Open in WRITE mode — creates a fresh CSV file
    with open(filename, "w", newline="", encoding="utf-8") as f:   # FILE HANDLING
        writer = csv.writer(f)

        # Write the header row
        writer.writerow(["ID", "Type", "Item Name", "Category",
                         "Location", "Date", "Description", "Contact", "Status"])

        # Write one data row per item
        for item in items:
            writer.writerow([
                item["id"],
                item["item_type"],
                item["item_name"],
                item["category"],
                item["location"],
                item["date"],
                item["description"] or "",
                item["contact"]     or "",
                item["status"],
            ])

    log_activity("EXPORT", extra=f"CSV saved → {filename}")
    return filename


# ==============================================================
# FILE READ — Read Mode
# ==============================================================
def read_recent_logs(n=80):
    """
    Read the last n lines from activity.log.

    FILE HANDLING — Opens file in READ mode ('r') and reads all lines.
    Returns the most recent entries first (reversed).
    """
    if not os.path.exists(LOG_FILE):
        return ["No activity has been recorded yet."]

    # Open in READ mode
    with open(LOG_FILE, "r", encoding="utf-8") as f:   # FILE HANDLING
        lines = f.readlines()

    # Strip blank lines, reverse so newest is first, limit to n
    entries = [line.strip() for line in lines if line.strip()]
    return list(reversed(entries))[:n]


def get_log_size():
    """Return the number of log entries recorded so far."""
    if not os.path.exists(LOG_FILE):
        return 0
    with open(LOG_FILE, "r", encoding="utf-8") as f:   # FILE HANDLING
        return sum(1 for line in f if line.strip())


def get_log_path():
    """Return the absolute path of the log file (used by Tkinter launcher)."""
    return os.path.abspath(LOG_FILE)
