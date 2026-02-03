from ex0.Card import Card, CardType


class CreatureCard(Card):
    def __init__(self,
                 name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health

    def get_card_info(self):
        info = super().get_card_info()
        info["type"] = CardType.CREATURE
        info["attack"] = self._attack
        info["health"] = self._health
        return info

    def play(self, game_state: dict) -> dict:
        self._played = True
        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        if isinstance(target, CreatureCard):
            target_name = target._name
        else:
            return ("Error the target is not a creature card")

        return {
            "attacker": self._name,
            "target": target_name,
            "damage_dealt": self._attack,
            "combat_resolved": self._attack >= target._health
        }

    def can_be_attacked(self) -> bool:
        return True

    def is_played(self) -> bool:
        return self._played
