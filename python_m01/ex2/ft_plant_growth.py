
class Plant:
    """Represents a plant with growth tracking"""

    def __init__(self, name, height, age):
        """Initialize a plant with name, height, and age"""
        self.name = name
        self.height = height
        self._age = age
        self.total_grow = 0

    def grow(self, amount):
        """Increase plant height by the given amount"""
        self.height += amount
        self.total_grow += amount

    def age(self, amount):
        """Increase plant age by the given number"""
        self._age += amount

    def get_info(self):
        """Display current plant information"""
        print(f"=== Day {1 + self.total_grow} ===")
        print(f"{self.name}: {self.height}cm, {self._age} days old")

    def get_growth(self):
        """Display total growth"""
        print(f"Growth this week: +{self.total_grow}cm")


rose = Plant("Rose", 25, 30)

rose.get_info()

rose.grow(6)
rose.age(6)

rose.get_info()

rose.get_growth()
