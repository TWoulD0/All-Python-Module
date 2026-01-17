import sys


def score_range():
    try:
        if len(sys.argv) == 1:
            print(
                "No scores provided."
                " Usage: python3 ft_score_analytics.py <score1> <score2> ...")
            return

        print("=== Player Score Analytics ===")
        scores = [int(arg) for arg in sys.argv[1:]]
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")

    except ValueError:
        print("Error: Invalid score format")


score_range()
