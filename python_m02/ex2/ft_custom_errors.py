
class GardenError(Exception):
    """Base exception for all garden-related errors"""
    pass


class PlantError(GardenError):
    """Exception raised when there's a problem with plants"""
    pass


class WaterError(GardenError):
    """Exception raised when there's a problem with water supply"""
    pass


def check_plant(plant, status):
    """Check plant status and raise error if wilting"""
    if status == "wilting":
        raise PlantError(f"The {plant} plant is wilting!")


def check_water(amount):
    """Check water amount and raise error if below minimum"""
    if amount < 10:
        raise WaterError("Not enough water in the tank!")


def plantError_Test():
    """Test PlantError exception handling"""
    print("\nTesting PlantError...")
    try:
        check_plant("tomato", "wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def waterError_Test():
    """Test WaterError exception handling"""
    print("\nTesting WaterError...")
    try:
        check_water(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def all_garden_Test():
    """Test catching all garden errors with base exception"""
    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato", "wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water(5)
    except GardenError as e:
        print(f"Caught a garden error: {e}")


print("=== Custom Garden Errors Demo ===")

plantError_Test()
waterError_Test()
all_garden_Test()

print("\nAll custom error types work correctly")
