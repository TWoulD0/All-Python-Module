
def water_plants(plant_list):
    """Water all plants in the list with automatic cleanup"""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise Exception(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test the watering system with normal and error cases"""

    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)

    print("\nTesting with error...")
    plants = ["tomato", None, "carrots"]
    water_plants(plants)

    print("\nCleanup always happens, even with errors!")


test_watering_system()
