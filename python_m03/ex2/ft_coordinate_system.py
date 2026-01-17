import math


def calculate_distance(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


def parse_coordinates(coord_string):
    parts = coord_string.split(',')
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def demonstrate_unpacking(position):
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={position[0]}, Y={position[1]}, Z={position[2]}")


def coordinate_system():
    print("=== Game Coordinate System ===")

    pos = (10, 20, 5)
    print(f"\nPosition created: {pos}")

    center = (0, 0, 0)
    distance = calculate_distance(center, pos)
    print(f"Distance between {center} and {pos}: {distance:.2f}")

    parsing_cor = "3,4,0"
    print(f"\nParsing coordinates: \"{parsing_cor}\"")
    parsing_pos = parse_coordinates(parsing_cor)
    print(f"Parsed position: {parsing_pos}")
    distance = calculate_distance(center, parsing_pos)
    print(f"Distance between {center} and {parsing_pos}: {distance}")

    parsing_invalid_cor = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{parsing_invalid_cor}\"")
    try:
        parsing_pos = parse_coordinates(parsing_invalid_cor)
        print(f"Parsed position: {parsing_pos}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    demonstrate_unpacking(parsing_pos)


coordinate_system()
