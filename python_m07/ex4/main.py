from ex4.TournamentPlatform import TournamentPlatform, TournamentCard

print("\n=== DataDeck Tournament Platform ===")

platform = TournamentPlatform()

dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 1200)
wizard = TournamentCard("Ice Wizard", 4, "Rare", 3, 4, 1150)

print("\nRegistering Tournament Cards...")
dragon_id = platform.register_card(dragon)
wizard_id = platform.register_card(wizard)

# ======== dragon info ======== #
print(f"\n{dragon._name} ({dragon_id})")
print(f"- Interfaces: {dragon.interfaces()}")
print(f"- Rating: {dragon.get_rank_info()["rating"]}")
print(f"- Record: {dragon.get_rank_info()["record"]}")

# ======== wizard info ======== #
print(f"\n{wizard._name} ({wizard_id})")
print(f"- Interfaces: {wizard.interfaces()}")
print(f"- Rating: {wizard.get_rank_info()["rating"]}")
print(f"- Record: {wizard.get_rank_info()["record"]}")

print("\nCreating tournament match...")
print(f"Match result: {platform.create_match(dragon_id, wizard_id)}")

print("\nTournament Leaderboard:")
print(f"{"\n".join(platform.get_leaderboard())}")

print("\nPlatform Report:")
print(platform.generate_tournament_report())

print("\n=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
