from ex0.Card import Card, CardType


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):

        super().__init__(name, cost, rarity)
        self._durability = durability
        self._effect = effect

    def get_card_info(self):
        info = super().get_card_info()
        info["type"] = CardType.ARTIFACT
        info["durability"] = self._durability
        info["effect"] = self._effect
        return info

    def play(self, game_state: dict) -> dict:
        self._played = True
        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": f"{self._effect}"
        }

    def activate_ability(self) -> dict:
        pass

    def can_be_attacked(self) -> bool:
        return False

    def is_played(self) -> bool:
        return self._played
