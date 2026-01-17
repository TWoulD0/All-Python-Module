
class SecurePlant:
    """Represents a plant with secure height and age"""

    def __init__(self, name):
        """Initialize a secure plant with a name and default height/age"""
        self.name = name
        self.__height = 0
        self.__age = 0

    def set_height(self, height):
        """Set plant height, rejecting negative values"""
        if height < 0:
            print("\nInvalid operation attempted: ", end="")
            print(f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        """Set plant age, rejecting negative values"""
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self):
        """Return the current height of the plant"""
        return self.__height

    def get_age(self):
        """Return the current age of the plant"""
        return self.__age

    def get_info(self):
        """Display current plant information"""
        print("\nCurrent plant: ", end="")
        print(f"{self.name} ({self.__height}cm, {self.__age} days)")


print("=== Garden Security System ===")

rose = SecurePlant("Rose")

print(f"Plant created: {rose.name}")
rose.set_height(25)
rose.set_age(30)
rose.set_height(-5)
rose.get_info()
