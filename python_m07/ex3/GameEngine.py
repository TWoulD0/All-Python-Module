from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:
    def __init__(self):
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._hand: list[Card] = []
        self._battlefield: list[Card] = []
        self.available_mana = 10
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy
                         ) -> None:
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        self._turns_simulated += 1
        if self._factory is None or self._strategy is None:
            return "Engine is not configured"

        self._hand = [
            self._factory.create_creature("dragon"),
            self._factory.create_creature("goblin"),
            self._factory.create_spell("fireball")
        ]

        hand_display = []

        for c in self._hand:
            card_info = f"{c._name} ({c._cost})"
            hand_display.append(card_info)
            if c._name == "Goblin Warrior" or c._name == "Lightning Bolt":
                game_state = {"mana": self.available_mana}
                c.play(game_state)

        result = self._strategy.execute_turn(self._hand, self._battlefield)
        self._total_damage = result["actions"]["damage_dealt"]
        self._cards_created = len(self._hand)

        return {
            "hand": hand_display,
            "turn_excution": result
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": self._strategy.get_strategy_name(),
            "total_damage": self._total_damage,
            "cards_created": self._cards_created
        }
