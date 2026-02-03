from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards: dict[str, TournamentCard] = {}
        self._matches: list[dict] = []

    def gen_card(self, card: TournamentCard) -> str:
        id_counter = 1

        name = card._name.split()[-1].lower()

        for c in self.cards:
            if name in c:
                num = int(c.split("_")[1])
                id_counter = num + 1

        card_id = f"ID: {name}_{id_counter:03d}"
        return card_id

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            return "Only TournamentCard can be register"

        card_id = self.gen_card(card)
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards:
            return f"the card: {card1_id} not found"
        if card2_id not in self.cards:
            return f"the card: {card2_id} not found"

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        c_info1 = card1.get_combat_stats()
        c_info2 = card2.get_combat_stats()

        if (c_info1["health"] / c_info2["attack"] >
                c_info2["health"] / c_info1["attack"]):
            winner_id = card1_id
            winner = card1
            loser_id = card2_id
            loser = card2
        elif (c_info1["health"] / c_info2["attack"] <
                c_info2["health"] / c_info1["attack"]):
            winner_id = card2_id
            winner = card2
            loser_id = card1_id
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        match_result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

        self._matches.append(match_result)

        return match_result

    def get_leaderboard(self) -> list:

        def get_rating(card):
            return card.get_rank_info()["rating"]

        leaderboard = list(self.cards.values())

        leaderboard.sort(key=get_rating)

        result = []
        for i, card in enumerate(leaderboard, 1):
            info = card.get_rank_info()
            result.append(
                f"{i}. {card._name} - Rating: {info['rating']} "
                f"({info['wins']}-{info['losses']})"
            )

        return result

    def generate_tournament_report(self) -> dict:
        cards = list(self.cards.values())
        avg_rating = sum(c._rating for c in cards) / len(cards)
        return {
            "total_cards": len(self.cards),
            "matches_played": len(self._matches),
            "avg_rating": int(avg_rating),
            "platform_status": "active"
        }
