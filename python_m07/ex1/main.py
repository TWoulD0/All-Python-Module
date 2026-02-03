from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")

    deck = Deck()
    deck.add_card(SpellCard(" Lightning Bol", 3, "Rare", "damage"))
    deck.add_card(ArtifactCard(
        "Mana Crystal", 2, "Uncommon", 2, "Permanent: +1 mana per turn"))
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    while len(deck.cards) > 0:
        card = deck.draw_card()
        card_info = card.get_card_info()

        print(f"\nDrew: {card_info.get("name")} ({card_info.get("type")})")
        game_state = {"mana": 10}
        print(f"Play result: {card.play(game_state)}")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
