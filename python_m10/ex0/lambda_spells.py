

artifacts = [
    {'name': 'Water Chalice', 'power': 117, 'type': 'relic'},
    {'name': 'Crystal Orb', 'power': 81, 'type': 'focus'},
    {'name': 'Light Prism', 'power': 93, 'type': 'relic'},
    {'name': 'Shadow Blade', 'power': 71, 'type': 'focus'}]

mages = [
    {'name': 'Alex', 'power': 92, 'element': 'earth'},
    {'name': 'Morgan', 'power': 100, 'element': 'wind'},
    {'name': 'Alex', 'power': 92, 'element': 'fire'},
    {'name': 'Sage', 'power': 86, 'element': 'light'},
    {'name': 'Alex', 'power': 84, 'element': 'water'}]

spells = ['freeze', 'heal', 'shield', 'darkness']

artifact_sorter = sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list, min_power: int) -> list:
    return list(filter(lambda m: m['power'] >= min_power, mages))


spell_transformer = list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list) -> dict:
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": sum(map(lambda m: m["power"], mages)) / len(mages)
    }


def main() -> None:
    print("Testing artifact sorter...")
    print(artifact_sorter)

    print("\nTesting power filter...")
    print(power_filter(mages, 95))

    print("\nTesting spell transformer...")
    print(spell_transformer)

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
