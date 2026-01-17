
class Plant:
    """Represents a plant with name, height, and age."""

    def __init__(self, name, height, age):
        """Initialize a plant with name, height, and age"""
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)
oak = Plant("Oak", 200, 365)
cactus = Plant("Cactus", 5, 90)
sunflower = Plant("Sunflower", 80, 45)
fern = Plant("Fern", 15, 120)

plants = [rose, oak, cactus, sunflower, fern]

print("=== Plant Factory Output ===")

for plant in plants:
    print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

print("\nTotal plants created: 5")
