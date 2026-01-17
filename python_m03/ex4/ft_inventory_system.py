
def add_item(inventory, item_name, item_details, quantity=1):
    if item_name in inventory:
        inventory[item_name]["quantity"] += quantity
    else:
        inventory[item_name] = item_details
        inventory[item_name]["quantity"] = quantity


def display_inv(player_name, inventory):
    print(f"=== {player_name}'s Inventory ===")
    for item_name in inventory.keys():
        item = inventory[item_name]
        total_price = item["quantity"] * item["price"]

        print(f"{item_name} ({item["type"]}, {item["rarity"]}): \
{item["quantity"]}x @ {item["price"]} \
gold each = {total_price} gold")


def calculate_total_value(inventory):
    total = 0
    for item_name in inventory.keys():
        item = inventory[item_name]
        quantity = item["quantity"]
        price = item["price"]
        total += quantity * price
    return total


def get_item_count(inventory):
    count = 0
    for item in inventory.keys():
        quantity = inventory[item]["quantity"]
        count += quantity
    return count


def get_categories(inventory):
    categories = dict()
    for item in inventory.keys():
        quantity = inventory[item]["quantity"]
        if item in categories:
            categories[item] += quantity
        else:
            categories[item] = quantity
    return categories


def print_categories(categories):
    print("Categories: ", end="")
    first = True
    for type in categories.keys():
        if not first:
            print(", ", end="")
        print(f"{type}({categories[type]})", end="")
        first = False
    print()


def transfer_item(from_inventory, to_inventory, item_name, quantity):
    if item_name not in from_inventory:
        return False
    if from_inventory[item_name]["quantity"] < quantity:
        return False

    from_inventory[item_name]["quantity"] -= quantity

    item_details = {
        "type": from_inventory[item_name]["type"],
        "rarity": from_inventory[item_name]["rarity"],
        "price": from_inventory[item_name]["price"]
    }

    add_item(to_inventory, item_name, item_details, quantity)

    if from_inventory[item_name]["quantity"] <= 0:
        del from_inventory[item_name]

    return True


def inventory_analytics(items, alice_inv, bob_inv):
    alice_value = calculate_total_value(alice_inv)
    bob_value = calculate_total_value(bob_inv)

    if alice_value > bob_value:
        print(f"Most valuable player: Alice ({alice_value} gold)")
    else:
        print(f"Most valuable player: Bob ({bob_value} gold)")

    alice_items = get_item_count(alice_inv)
    bob_items = get_item_count(bob_inv)

    if alice_items > bob_items:
        print(f"Most items: Alice ({alice_items} items)")
    else:
        print(f"Most valuable player: Bob ({bob_items} gold)")

    rarest_items = {}

    for item in items:
        rare = items[item]["rarity"]
        if "rare" in rare:
            rarest_items[item] = items[item]

    print("Rarest items: ", end="")
    first = True
    for name in rarest_items.keys():
        if not first:
            print(", ", end="")
        print(name, end="")
        first = False
    print()


def main():
    print("=== Player Inventory System ===\n")

    items = {

        "sword":
        {
            "type": "weapon",
            "rarity": "rare",
            "price": 500,
        },
        "potion":
        {
            "type": "consumable",
            "rarity": "common",
            "price": 50,
        },
        "shield":
        {
            "type": "armor",
            "rarity": "uncommon",
            "price": 200,
        },
        "magic_ring":
        {
            "type": "armor",
            "rarity": "rare",
            "price": 200,
        }
    }

    alice_inv = dict()
    bob_inv = dict()

    add_item(alice_inv, "sword", items["sword"], 1)
    add_item(alice_inv, "potion", items["potion"], 5)
    add_item(alice_inv, "shield", items["shield"], 1)

    display_inv("Alice", alice_inv)
    print(f"\nInventory value: {calculate_total_value(alice_inv)} gold")
    print(f"Item count: {get_item_count(alice_inv)} items")

    categories = get_categories(alice_inv)
    print_categories(categories)

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    if transfer_item(alice_inv, bob_inv, "potion", 2):
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("\n=== Updated Inventories ===")
    alice_potions = alice_inv.get("potion", {"quantity": 0})["quantity"]
    bob_potions = bob_inv.get("potion", {"quantity": 0})["quantity"]
    print(f"Alice potions: {alice_potions}")
    print(f"Bob potions: {bob_potions}")

    print("\n=== Inventory Analytics ===")
    inventory_analytics(items, alice_inv, bob_inv)


main()
