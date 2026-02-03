from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity, attack, health, rating):
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health
        self._max_health = health
        self._rating = rating
        self._wins = 0
        self._losses = 0

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins += wins
        self._rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self._losses += losses
        self._rating -= losses * 16

    def get_rank_info(self) -> dict:
        return {
            "name": self._name,
            "wins": self._wins,
            "losses": self._losses,
            "rating": self._rating,
            "record": f"{self._wins}-{self._losses}"
        }

    def get_tournament_stats(self) -> dict:
        pass

    def can_be_attacked(self) -> bool:
        pass

    def is_played(self) -> bool:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        return {
            "name": self._name,
            "attack": self._attack,
            "health": self._health,
            "max_health": self._max_health,
        }

    def interfaces(self):
        return [Card.__name__,
                Combatable.__name__,
                Rankable.__name__,]
