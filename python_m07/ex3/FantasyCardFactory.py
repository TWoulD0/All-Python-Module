from ex3.CardFactory import CardFactory, Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Dict


class FantasyCardFactory(CardFactory):

    CREATURES: Dict[str, dict] = {
        "dragon": {
            "name": "Fire Dragon", "cost": 5, "rarity": "Legendary",
            "attack": 7, "health": 5
        },
        "goblin": {
            "name": "Goblin Warrior", "cost": 2, "rarity": "Common",
            "attack": 2, "health": 1
        },
    }

    SPELLS: Dict[str, dict] = {
        "fireball": {
            "name": "Lightning Bolt", "cost": 3, "rarity": "Common",
            "effect_type": "damage"
        },
    }

    ARTIFACTS: Dict[str, dict] = {
        "mana_ring": {
            "name": "Mana Ring", "cost": 2, "rarity": "Common",
            "durability": 5, "effect": "Permanent: +1 mana per turn"
        },
    }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if not isinstance(name_or_power, str):
            return "error: the input not a str"
        if name_or_power in self.CREATURES:
            card = self.CREATURES[name_or_power]
        else:
            return "we dont have this card"

        return CreatureCard(card["name"], card["cost"], card["rarity"],
                            card["attack"], card["health"])

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if not isinstance(name_or_power, str):
            return "error: the input not a str"
        if name_or_power in self.SPELLS:
            card = self.SPELLS[name_or_power]
        else:
            return "we dont have this card"

        return SpellCard(card["name"], card["cost"], card["rarity"],
                         card["effect_type"])

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if not isinstance(name_or_power, str):
            return "error: the input not a str"
        if name_or_power in self.ARTIFACTS:
            card = self.ARTIFACTS[name_or_power]
        else:
            return "we dont have this card"

        return ArtifactCard(card["name"], card["cost"], card["rarity"],
                            card["durability"], card["effect"])

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        return {
            "creatures": list(self.CREATURES.keys()),
            "spells": list(self.SPELLS.keys()),
            "artifacts": list(self.ARTIFACTS.keys())
        }
