from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard
from ex0.Card import CombatType


def main() -> None:
    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")
    warrior = EliteCard(
        "Arcane Warrior", 4, "Legandary", 5, 7, 4, 3, CombatType.MELEE)
    print("\nCombat phase:")
    enemy = CreatureCard("Enemy", 4, "Rare", 5, 7)
    print(f"Attack result: {warrior.attack(enemy)}")
    print(f"Defense result: {warrior.defend(enemy)}")

    print("\nMagic phase:")
    enemy1 = CreatureCard("Enemy1", 4, "Rare", 5, 7)
    enemy2 = CreatureCard("Enemy2", 4, "Rare", 5, 7)
    enemies = [enemy1, enemy2]
    print(f"Spell cast: {warrior.cast_spell("Fireball", enemies)}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
