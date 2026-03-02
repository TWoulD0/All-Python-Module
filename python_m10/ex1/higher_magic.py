
def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kw_args):
        r1 = spell1(*args, **kw_args)
        r2 = spell2(*args, **kw_args)
        return f"Combined spell result: {r1}, {r2}"

    return combined


def fireball(target):
    return f"Fireball hits {target}"


def heal(target):
    return f"Heals {target}"


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier(*args, **kw_args):
        result = base_spell(*args, **kw_args)
        return f"Original: {result}, Amplified: {result * multiplier}"

    return amplifier


def fireball2(target, power=10):
    return power


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kw_args):
        if condition(*args, **kw_args):
            return spell(*args, **kw_args)
        else:
            return "Spell fizzled"

    return caster


def is_enemy(target):
    return target == "Dragon"


def spell_sequence(spells: list[callable]) -> callable:
    def sequencer(*args, **kw_args):
        results = []
        for spell in spells:
            results.append(spell(*args, **kw_args))
        return results
    return sequencer


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon"))

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball2, 3)
    print(mega_fireball("Dragon"))

    print("\nTesting conditional caster...")
    cast_if_enemy = conditional_caster(is_enemy, fireball)
    print(cast_if_enemy("Dragon"))
    print(cast_if_enemy("enemy"))

    print("\nTesting spell sequence...")
    spells = [fireball, heal]
    combo = spell_sequence(spells)
    print(combo("Dragon"))


if __name__ == "__main__":
    main()
