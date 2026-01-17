
def list_comprehension(players):
    hight_scores = [p for p in players.keys() if players[p]["score"] > 2000]
    print(f"High scorers (>2000): {hight_scores}")

    double_scores = [players[s]["score"] * 2 for s in players.keys()]
    print(f"Scores doubled: {double_scores}")

    active_players = [p for p in players.keys() if players[p]["active"]]
    print(f"Active players: {active_players}")


def dict_comprehension(players):
    player_scores = {p: players[p]["score"] for p in players.keys()}
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": sum(1 for p in players.keys() if players[p]["score"] > 2000),
        "medium":
        sum(1 for p in players.keys() if 1800 <= players[p]["score"] <= 2000),
        "low": sum(1 for p in players.keys() if players[p]["score"] < 1800)
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {p: len(players[p]["achievements"]) for p in players}
    print(f"Achievement counts: {achievement_counts}")


def set_comprehension(players):
    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievs = {a for p in players.values() for a in p["achievements"]}
    print(f"Unique achievements: {unique_achievs}")

    active_regions = {
        players[p]["region"] for p in players.keys() if players[p]["active"]}
    print(f"Active regions: {active_regions}")


def combine(players):
    total_players = len(players)
    print(f"Total players: {total_players}")

    total_unique_achievements = sum(
        len(set(p["achievements"]))
        for p in players.values())
    print(f"Total unique achievements: {total_unique_achievements}")

    player_scores = {players[p]["score"] for p in players.keys()}
    average_score = sum(player_scores) / len(player_scores)
    print(f"Average score: {average_score}")

    max_score = max(player["score"] for player in players.values())
    player_name = [
        p for p in players.keys() if players[p]["score"] == max_score][0]
    player_achiv = [len(players[p]["achievements"])
                    for p in players.keys()
                    if players[p]["score"] == max_score][0]
    print(f"Top performer: "
          f"{player_name} ({max_score} points, {player_achiv} achievements)")


def main():
    players = {
        "alice":
        {
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": ["first_kill", "level_10", "boss_slayer",
                             "level_10", "boss_slayer"]
        },
        "bob":
        {
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements": ["level_10", "first_kill", "boss_slayer"]
        },
        "charlie":
        {
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements": ["first_kill", "level_10", "boss_slayer",
                             "level_10", "boss_slayer", "first_kill",
                             "level_10"]
        },
        "diana":
        {
            "score": 2050,
            "active": False,
            "region": "north",
            "achievements": ["level_10", "first_kill", "boss_slayer"]
        }
    }

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    list_comprehension(players)

    print("\n=== Dict Comprehension Examples ===")
    dict_comprehension(players)

    print("\n=== Set Comprehension Examples ===")
    set_comprehension(players)

    print("\n=== Combined Analysis ===")
    combine(players)


main()
