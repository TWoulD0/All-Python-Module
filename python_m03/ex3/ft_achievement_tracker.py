
alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
           'perfectionist'}

print("=== Achievement Analytics ===\n")

print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===")

all_unique_achievements = alice | bob | charlie
print(f"All unique achievements: {all_unique_achievements}")
print(f"Total unique achievements: {len(all_unique_achievements)}")

common_all_players = alice & bob & charlie
print(f"\nCommon to all players: {common_all_players}")

alice_rare = alice - bob - charlie
bob_rare = bob - alice - charlie
charlie_rare = charlie - bob - alice
rare_achievements = alice_rare | bob_rare | charlie_rare
print(f"Rare achievements (1 player): {rare_achievements}")

alice_bob = alice & bob
print(f"\nAlice vs Bob common: {alice_bob}")
alice_unique = alice - bob
print(f"Alice unique: {alice_unique}")
bob_unique = bob - alice
print(f"Bob unique: {bob_unique}")
