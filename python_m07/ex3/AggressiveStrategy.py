from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:

        mana_used = 0
        cards_played: list[Card] = []
        cards_played_names = []
        for c in hand:
            if not isinstance(c, Card):
                return ("there is a none card in hand")

            if c.is_played():
                cards_played.append(c)

        for card in cards_played:
            mana_used += card._cost
            cards_played_names.append(card._name)

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played_names,
                "mana_used": mana_used,
                "targets_attacked": ['Enemy Player'],
                "damage_dealt": 8
            }
        }

    def get_strategy_name(self) -> str:
        return (__class__.__name__)

    def prioritize_targets(self, available_targets: list) -> list:
        pass
