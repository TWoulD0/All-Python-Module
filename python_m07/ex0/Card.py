from abc import ABC, abstractmethod
from enum import Enum


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"


class CombatType(Enum):
    MELEE = "melee"
    RANGED = "ranged"
    MAGIC = "magic"
    SUPPORT = "support"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self._name = name
        self._cost = cost
        self._rarity = rarity
        self._played = False

    @abstractmethod
    def play(self, game_state: dict):
        pass

    def get_card_info(self):
        return {
            "name": self._name,
            "cost": self._cost,
            "rarity": self._rarity,
            "type": ""
        }

    def is_playable(self, available_mana: int):
        if available_mana >= self._cost:
            return True
        else:
            return False

    @abstractmethod
    def can_be_attacked(self) -> bool:
        pass

    @abstractmethod
    def is_played(self) -> bool:
        pass
