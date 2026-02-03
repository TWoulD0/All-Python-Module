from ex0.Card import Card, CardType
from typing import List


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        if not self.cards:
            return False

        for card in self.cards:
            if card.get_card_info().get("name") == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        if not self.cards:
            return None

        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        creatures_cards = 0
        spells_cards = 0
        artifacts_cards = 0
        total_cost = 0

        for card in self.cards:
            card_type = card.get_card_info().get("type", "Unknown")
            card_cost = card.get_card_info().get("cost", "None")

            if card_type == CardType.CREATURE:
                creatures_cards += 1
            elif card_type == CardType.SPELL:
                spells_cards += 1
            elif card_type == CardType.ARTIFACT:
                artifacts_cards += 1

            total_cost += card_cost

        return {
            "total_cards": total_cards,
            "creatures": creatures_cards,
            "spells": spells_cards,
            "artifacts": artifacts_cards,
            "avg_cost": total_cost
        }
