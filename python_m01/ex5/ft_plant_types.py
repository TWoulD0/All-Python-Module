
class Plant:
    """Base class representing a plant with basic attributes"""
    def __init__(self, name, height, age):
        """Initialize a plant with name, height, and age"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a flowering plant with color attribute"""
    def __init__(self, name, height, age, color):
        """Initialize a flower with inherited attributes plus color"""
        super().__init__(name, height, age)
        self.color = color

    def get_info(s):
        """Display flower information"""
        print(f"\n{s.name} (Flower): ", end="")
        print(f"{s.height}cm, {s.age} days, {s.color} color")

    def bloom(s):
        """Display a blooming message"""
        print(f"{s.name} is blooming beautifully!")


class Tree(Plant):
    """Represents a tree with trunk diameter and shade calculation"""
    def __init__(self, name, height, age,  trunk_diameter):
        """Initialize a tree with inherited attributes plus trunk diameter"""
        super().__init__(name, height, age)
        self. trunk_diameter = trunk_diameter

    def get_info(s):
        """Display tree information including trunk diameter"""
        print(f"\n{s.name} (Tree): ", end="")
        print(f"{s.height}cm, {s.age} days, {s.trunk_diameter}cm diameter")

    def produce_shade(s):
        """Calculate and display the shade area provided by the tree"""
        shade = s.trunk_diameter * 1.56
        print(f"{s.name} provides {int(shade)} square meters of shade")


class Vegetable(Plant):
    """Represents a vegetable plant with harvest and nutritional information"""
    def __init__(self, name, height, age, harvest_season,  nutritional_value):
        """Initialize with inherited attributes plus season and nutrition"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(s):
        """Display vegetable information"""
        print(f"\n{s.name} (Vegetable): ", end="")
        print(f"{s.height}cm, {s.age} days, {s.harvest_season}")
        print(f"{s.name} is rich in {s.nutritional_value}")


print("=== Garden Plant Types ===")
rose = Flower("Rose", 25, 30, "red")
sunflower = Flower("Sunflower", 40, 25, "yellow")
oak = Tree("Oak", 500, 1825, 50)
pine = Tree("Pine", 600, 2300, 60)
tomato = Vegetable("Tomato", 80, 90, "summer harvest", "Vitamin C")
potato = Vegetable("Potato", 60, 70, "summer harvest", "fiber")

rose.get_info()
rose.bloom()

sunflower.get_info()

oak.get_info()
oak.produce_shade()

pine.get_info()
tomato.get_info()
potato.get_info()
