import random
import time

player = {
    "name": "bob",
    "health": 100,
    "max_health": 200,
    "damage": 0,
    "speed": 15,
    "gold": 50,
    "potions": 0,

    
}



enemy_templates = [
    {"name": "Goblin", "hp": 10, "dropgold": 5, "attack": 3},
    {"name:": "Golem", "hp": 40, "dropgold": 20, "attack": 5},
    {"name:": "Skeleton", "hp": 15, "dropgold": 10, "attack": 5},
]


def combat(enemy):
    print(f"\nA wild {enemy["name"]} appears!")

    while enemy["hp"] > 0 and player["health"] > 0:
        print("e")
        exit()


def main():
    print("==== WELCOME! ===")
    time.sleep(1)
    print("\nWhat's your name?")
    player["name"] = input("> ")
    print(f"{player['name']}")

main()