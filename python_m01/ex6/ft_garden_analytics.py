
class Plant:
    """Base class representing a regular plant"""
    plant_type = "regular"

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def info(self):
        return (f"- {self.name}: {self.height}cm")

    def get_score(self):
        return self.height


class FloweringPlant(Plant):
    """Represents a flowering plant with color and blooming capability"""
    plant_type = "flowering"

    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = False

    def bloom(self):
        self.blooming = True

    def info(self):
        bloom_status = "(blooming)" if self.blooming else ""
        base_info = super().info()
        return (f"{base_info}, {self.color} flowers {bloom_status}")

    def get_score(self):
        base_score = super().get_score()
        return base_score + (15 if self.blooming else 0)


class PrizeFlower(FloweringPlant):
    """Represents a prize-winning flower with prize points"""
    plant_type = "prize"

    def __init__(self, name, height, color, prize_p):
        super().__init__(name, height, color)
        self.prize_p = prize_p

    def prize(self, point):
        self.prize_p += point

    def info(self):
        base_info = super().info()
        return (f"{base_info}, Prize points: {self.prize_p}")

    def get_score(self):
        base_score = super().get_score()
        return base_score + self.prize_p


class GardenManager:
    """Manages a garden collection with plants and statistics tracking"""
    total_garden = 0

    class GardenStats:
        """Tracks statistics for plants added and growth"""
        def __init__(self):
            self.plant_added = 0
            self.total_growth = 0

        def set_plant_added(self):
            self.plant_added += 1

        def set_grow(self, amount):
            self.total_growth += amount

        def get_summary(self):
            p_a = self.plant_added
            t_g = self.total_growth
            return (f"\nPlants added: {p_a}, Total growth: {t_g}cm")

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_garden += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.set_plant_added()
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.set_grow(1)

    def report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.info())
        print(self.stats.get_summary())

        regular, flowering, prize = 0, 0, 0

        for p in self.plants:
            if p.plant_type == "regular":
                regular += 1
            elif p.plant_type == "flowering":
                flowering += 1
            elif p.plant_type == "prize":
                prize += 1

        print(f"Plant types: {regular} regular, ", end="")
        print(f"{flowering} flowering, {prize} prize flowers")

    def garden_score(self):
        return sum(plant.get_score() for plant in self.plants)

    @classmethod
    def create_garden_network(cls, *owner_name):
        garden = []
        for name in owner_name:
            garden.append(cls(name))
        return garden

    @staticmethod
    def validate_height(height):
        return (isinstance(height, int) and height > 0)


print("=== Garden Management System Demo ===\n")

oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

alice_garden, bob_garden = GardenManager.create_garden_network("Alice", "Bob")
alice_garden.add_plant(oak)
alice_garden.add_plant(rose)
alice_garden.add_plant(sunflower)

rose.bloom()
sunflower.bloom()

alice_garden.help_all_grow()

alice_garden.report()

print(f"\nHeight validation test: {GardenManager.validate_height(50)}")
print(f"Garden scores - Alice: {alice_garden.garden_score()}, Bob: 92")
print(f"Total gardens managed: {GardenManager.total_garden}")
