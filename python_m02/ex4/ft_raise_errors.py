
def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check if plant conditions are within healthy ranges"""

    try:
        s_h = sunlight_hours

        if plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        elif water_level < 1 or water_level > 10:
            if water_level < 1:
                raise ValueError(
                    f"Water level {water_level} is too low (min 1)")
            else:
                raise ValueError(
                    f"Water level {water_level} is too high (max 10)")
        elif s_h < 2 or s_h > 12:
            if sunlight_hours < 2:
                raise ValueError(
                    f"Sunlight hours {sunlight_hours} is too low (min 2)")
            else:
                raise ValueError(
                    f"Sunlight hours {sunlight_hours} is too high (max 12)")
        else:
            print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks():
    """Run test cases for plant health validation"""

    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    check_plant_health("tomato", 5, 6)

    print("\nTesting empty plant name...")
    check_plant_health("", 5, 6)

    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 6)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 0)

    print("\nAll error raising tests completed!")


test_plant_checks()
