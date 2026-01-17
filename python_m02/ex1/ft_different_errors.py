
def garden_operations(type):
    """Demonstrate different error types and their handling"""

    if type == "ValueError":
        try:
            int("abc")
        except ValueError as e:
            print(f"Caught ValueError: {e}")

    elif type == "ZeroDivisionError":
        try:
            10 / 0
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")

    elif type == "FileNotFoundError":
        try:
            open("missing.txt", "r")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")

    elif type == "KeyError":
        try:
            garden = {"plant1": 4, "plant2": 3}
            garden["missing_plant"]
        except KeyError as e:
            print(f"Caught KeyError: {e}")

    elif type == "multiple":
        try:
            int("abc")
            10 / 0
            open("missing.txt", "r")
            garden = {"plant1": 4, "plant2": 3}
            garden["missing_plant"]
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!")


def test_error_types():
    """Run test cases for all error handling types"""

    print("\n=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    garden_operations("ValueError")

    print("\nTesting ZeroDivisionError...")
    garden_operations("ZeroDivisionError")

    print("\nTesting FileNotFoundError...")
    garden_operations("FileNotFoundError")

    print("\nTesting KeyError...")
    garden_operations("KeyError")

    print("\nTesting multiple errors together...")
    garden_operations("multiple")

    print("\nAll error types tested successfully!")


test_error_types()
