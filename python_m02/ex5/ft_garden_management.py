
class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised for plant-specific errors."""
    pass


class WaterError(GardenError):
    """Raised for watering-related issues."""
    pass


class Plant:
    """Represents a plant with water and sunlight requirements"""
    def __init__(self, name, water, sun):
        """Initialize a plant with name, water level, and sunlight hours"""
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    """Manages a collection of plants and watering operations"""

    def __init__(self, water_tank):
        """Initialize garden manager with a water tank level"""
        self.plants = []
        self.water_tank = water_tank

    def add_plant(self, plant):
        """Add a plant to the garden with validation"""
        try:
            if plant.name == "":
                raise PlantError("Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plant(self):
        """Water all plants in the garden with cleanup handling"""
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.water_tank < 1:
                    raise WaterError("Not enough water in the tank!")
                self.water_tank -= 1

                plant.water += 1
                print(f"Watering {plant.name} - success")

        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def get_plant_health(self):
        """Check and report health status of all plants"""
        for plant in self.plants:
            p_w = plant.water
            p_s = plant.sun
            try:
                if plant.water < 1:
                    raise PlantError(f"Water level {p_w} is too low (min 1)")
                elif plant.water > 10:
                    raise PlantError(f"Water level {p_w} is too high (max 10)")
                elif plant.sun < 2:
                    raise PlantError(
                        f"Sunlight hours {p_s} is too low (min 2)")
                elif plant.sun > 12:
                    raise PlantError(
                        f"Sunlight hours {p_s} is too high (max 12)")
                else:
                    print(f"{plant.name}: healthy (water: {p_w}, sun: {p_s})")
            except PlantError as e:
                print(f"Error checking {plant.name}: {e}")

    def check_garden_status(self):
        """Check overall garden water tank status with error recovery"""
        try:
            if self.water_tank < 10:
                raise GardenError("Not enough water in tank")
            print("the tank have enough water")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...")


print("=== Garden Management System ===")
garden = GardenManager(5)
tomato = Plant("tomato", 4, 8)
lettuce = Plant("lettuce", 14, 6)
empty_plant = Plant("", 14, 6)

print("\nAdding plants to garden...")
garden.add_plant(tomato)
garden.add_plant(lettuce)
garden.add_plant(empty_plant)

print("\nWatering plants...")
garden.water_plant()

print("\nChecking plant health...")
garden.get_plant_health()

print("\nTesting error recovery...")
garden.check_garden_status()

print("\nGarden management system test complete!")
