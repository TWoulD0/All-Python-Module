
def mage_counter() -> callable:
    current_count = 0

    def count(*args, **kw_args):
        nonlocal current_count
        current_count += 1
        return f"Call {current_count}: {current_count}"

    return count


def spell_accumulator(initial_power: int) -> callable:
    total_power = 0

    def accumulator(*args, **kw_args):
        nonlocal total_power
        total_power += initial_power
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchantment(name: str):
        return f"{enchantment_type} {name}"

    return enchantment


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    count = mage_counter()
    print(count())
    print(count())
    print(count())

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(65)
    print(accumulator())
    print(accumulator())
    print(accumulator())

    print("\nTesting enchantment factory...")
    enchantment = enchantment_factory("Flaming")
    print(enchantment("Sword"))
    enchantment = enchantment_factory("Frozen")
    print(enchantment("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()

    vault["store"]("Sword", "Flaming")
    vault["store"]("Armor", "Earthen")

    print(vault["recall"]("Sword"))
    print(vault["recall"]("Wand"))


if __name__ == "__main__":
    main()
