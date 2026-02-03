from ex0.Card import Card, CombatType
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, mana: int, armor: int = 0,
                 combat_type: CombatType = CombatType.MELEE) -> None:
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health
        self._mana = mana
        self._armor = armor
        self._combat_type = combat_type

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        if not isinstance(target, Card):
            return ("Error the target is not a card")

        if not target.can_be_attacked():
            return ("Target cannot be attacked")

        return {
            "attacker": self._name,
            "target": target._name,
            "damage": self._attack,
            "combat_type": self._combat_type.value
        }

    def defend(self, target) -> dict:
        if not isinstance(target, Card):
            return ("Error the target is not a card")

        if not target.can_be_attacked():
            return ("Target cannot be attacked")

        if self._armor >= target._attack:
            damage_taken = 0
        else:
            damage_taken = target._attack - self._armor

        if self._health - damage_taken <= 0:
            still_alive = False
        else:
            still_alive = True
        return {
            "defender": self._name,
            "damage_taken": damage_taken,
            "damage_blocked": self._armor,
            "still_alive": still_alive,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        for target in targets:
            if not isinstance(target, Card):
                return ("Error the target is not a card")

            if not target.can_be_attacked():
                return ("Target cannot be attacked")

        return {
            "caster": self._name,
            "spell": spell_name,
            "targets": [t._name for t in targets],
            "mana_used": self._mana
        }

    def can_be_attacked(self) -> bool:
        return True

    def get_combat_stats(self) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        if amount < 0:
            return ("Channel amount must be a positive number")
        self._mana += amount
        return {
            "channeled": amount,
            "total_mana": self._mana
        }

    def get_magic_stats(self) -> dict:
        pass

    def is_played(self) -> bool:
        return self._played
