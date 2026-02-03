from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")

    # ==== Info of Creature Card ==== #
    print("\nCreatureCard Info:")
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(dragon.get_card_info())

    # ==== Playing the card if mana available ==== #
    available_mana = 6
    print(f"\nPlaying {dragon._name} with {available_mana} mana available:")
    print(f"Playable: {dragon.is_playable(available_mana)}")
    game_state = {"mana": available_mana}
    print(f"Play result: {dragon.play(game_state)}")

    # ==== dragon card attacks goblin card ==== #
    print("\nFire Dragon attacks Goblin Warrior:")
    goblin = CreatureCard("Goblin Warrior", 2, "common", 1, 2)
    print(f"Attack result: {dragon.attack_target(goblin)}")

    # ==== Testing with low mana ==== #
    insufficient_mana = 3
    print(f"\nTesting insufficient mana ({insufficient_mana} available):")
    print(f"Playable: {dragon.is_playable(insufficient_mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
