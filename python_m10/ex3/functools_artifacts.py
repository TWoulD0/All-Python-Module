from functools import reduce, partial, lru_cache, singledispatch
import operator

spell_powers = [39, 21, 12, 38, 34, 28]
operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [17, 14, 19]


def spell_reducer(spells: list[int], operation: str) -> int:
    total = 0
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    total = reduce(ops[operation], spells)
    return total


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:

    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


def enchant(power: int, element: str, target: str):
    return f"{element} enchant {power} on {target}"


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def dispatch(value):
        return "Unknown spell type"

    @dispatch.register
    def _(value: int):
        return f"Damage spell deals {value} damage"

    @dispatch.register
    def _(value: str):
        return f"Enchantment spell: {value}"

    @dispatch.register
    def _(value: list):
        return [dispatch(item) for item in value]

    return dispatch


def main() -> None:
    print("\nTesting spell reducer...")
    spell_powers = [39, 21, 12, 38, 34, 28]
    add = spell_reducer(spell_powers, "add")
    mult = spell_reducer(spell_powers, "multiply")
    max = spell_reducer(spell_powers, "max")
    print(f"Sum: {add}")
    print(f"Product: {mult}")
    print(f"Max: {max}")

    print("\nTesting partial enchanter...")
    element = partial_enchanter(enchant)
    print(element["fire_enchant"]("Sword"))

    print("\nTesting memoized fibonacci...")
    fib = memoized_fibonacci(10)
    print(fib)

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(10))
    print(dispatch("fire"))
    print(dispatch([23, "ice"]))


if __name__ == "__main__":
    main()
