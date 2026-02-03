from ex0.Card import Card, CardType


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self._effect_type = effect_type

    def get_card_info(self):
        info = super().get_card_info()
        info["type"] = CardType.SPELL
        info["effect_type"] = self._effect_type
        return info

    def play(self, game_state: dict) -> dict:
        self._played = True
        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": f"Deal {self._cost} damage to target"
        }

    def resolve_effect(self, targets: list) -> dict:
        pass

    def can_be_attacked(self) -> bool:
        return False

    def is_played(self) -> bool:
        return self._played
