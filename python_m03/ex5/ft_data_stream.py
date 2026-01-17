import time
import random


def event_stream(num_events):
    players = ["alice", "bob", "charlie"]
    event_types = ["killed monster", "found treasure", "leveled up"]

    for i in range(num_events):
        event = {
            "id": i + 1,
            "player": random.choice(players),
            "level": random.randint(1, 20),
            "action": random.choice(event_types)
        }
        yield event


def fibonacci_generator(num):
    a = 0
    b = 1
    count = 0

    while count < num:
        yield a
        a, b = b, a + b
        count += 1


def prime_generator(num):
    count = 0
    prime = 2
    while count < num:
        is_prime = True

        for i in range(2, prime):
            if prime % i == 0:
                is_prime = False
                break

        if is_prime:
            yield prime
            count += 1

        prime += 1


def main():
    print("=== Game Data Stream Processor ===")

    num_event = 1000
    print(f"\nProcessing {num_event} game events...\n")

    start_time = time.time()

    events = event_stream(num_event)

    total_event = 0
    hight_level_players = 0
    treasure_events = 0
    level_up_events = 0

    for event in events:
        total_event += 1

        if total_event <= 3:
            print(f"Event {event["id"]}: Player {event["player"]} "
                  f"(level {event["level"]}) {event["action"]}")

        if event["level"] >= 10:
            hight_level_players += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1

    if total_event > 3:
        print("...")

    processing_time = time.time() - start_time

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_event}")
    print(f"High-level players (10+): {hight_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    fib_gen = fibonacci_generator(10)
    fib_num = []
    for num in fib_gen:
        fib_num.append(str(num))
    print(f"Fibonacci sequence (first 10): {', '.join(fib_num)}")

    prime_gen = prime_generator(5)
    prime_num = []
    for num in prime_gen:
        prime_num.append(str(num))
    print(f"Prime numbers (first 5): {', '.join(prime_num)}")


main()
