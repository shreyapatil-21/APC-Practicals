# ============================================================
# models.py
# Demonstrates: Classes, Inheritance, Polymorphism, __str__
# ============================================================


class ReportItem:
    """
    BASE CLASS — Represents any reported campus item.
    LostItem and FoundItem inherit from this class.
    """

    def __init__(self, item_name, category, location, date,
                 description="", contact=""):
        # Instance attributes (object properties)
        self.item_name   = item_name
        self.category    = category
        self.location    = location
        self.date        = date
        self.description = description
        self.contact     = contact

    def get_type(self):
        """
        Returns the item type label.
        Overridden in subclasses → POLYMORPHISM
        """
        return "Unknown"

    def get_summary(self):
        """
        Returns a one-line summary of the report.
        Overridden in subclasses → POLYMORPHISM
        """
        return (f"{self.get_type()} Item: '{self.item_name}' | "
                f"Category: {self.category} | Location: {self.location} | "
                f"Date: {self.date}")

    def to_csv_row(self):
        """Returns item data as a flat list — used for CSV export."""
        return [
            self.get_type(),
            self.item_name,
            self.category,
            self.location,
            self.date,
            self.description,
            self.contact,
        ]

    def __str__(self):
        """Special method — called when print(item_obj) is used."""
        return self.get_summary()

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.item_name}>"


# --------------------------------------------------------------
class LostItem(ReportItem):
    """
    CHILD CLASS — Represents a LOST item.
    Inherits all attributes from ReportItem.
    Overrides get_type() and get_summary() → Polymorphism
    """

    def get_type(self):
        """Polymorphism: returns 'Lost' instead of 'Unknown'."""
        return "Lost"

    def get_summary(self):
        """Polymorphism: customized message for lost items."""
        return (f"[LOST]  '{self.item_name}' ({self.category}) — "
                f"Last seen at '{self.location}' on {self.date}. "
                f"Contact: {self.contact or 'Not provided'}")


# --------------------------------------------------------------
class FoundItem(ReportItem):
    """
    CHILD CLASS — Represents a FOUND item.
    Inherits all attributes from ReportItem.
    Overrides get_type() and get_summary() → Polymorphism
    """

    def get_type(self):
        """Polymorphism: returns 'Found' instead of 'Unknown'."""
        return "Found"

    def get_summary(self):
        """Polymorphism: customized message for found items."""
        return (f"[FOUND] '{self.item_name}' ({self.category}) — "
                f"Found at '{self.location}' on {self.date}. "
                f"Contact: {self.contact or 'Not provided'}")


# --------------------------------------------------------------
def create_item(item_type, item_name, category, location, date,
                description="", contact=""):
    """
    FACTORY FUNCTION — Creates a LostItem or FoundItem based on item_type.

    This is where Polymorphism shines:
    - Same function call → different object is returned
    - Both objects share the same interface (get_type, get_summary, etc.)
    - Calling get_summary() on either gives a DIFFERENT result
    """
    if item_type == "Lost":
        return LostItem(item_name, category, location, date, description, contact)
    elif item_type == "Found":
        return FoundItem(item_name, category, location, date, description, contact)
    else:
        # Default to base class if type is unrecognised
        return ReportItem(item_name, category, location, date, description, contact)


# --------------------------------------------------------------
# Quick polymorphism demo (runs only when this file is executed directly)
if __name__ == "__main__":
    items = [
        LostItem("Dell Laptop", "Electronics", "Library", "2026-10-22",
                 contact="Roll: 22CS045"),
        FoundItem("Student ID Card", "ID Card", "Canteen", "2026-10-22",
                  contact="Security Desk"),
    ]

    print("=== Polymorphism Demo ===")
    for item in items:                    # Same loop, different output
        print(item.get_type())            # Lost / Found
        print(item.get_summary())         # Different message per class
        print(item)                       # Calls __str__
        print()
