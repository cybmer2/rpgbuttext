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
    "weapon": "Iron Sword",
    "weapondamage": 6

    
}



enemy_templates = [
    {"name": "Goblin", "hp": 10, "dropgold": 5, "attack": 3},
    {"name": "Golem", "hp": 40, "dropgold": 20, "attack": 5},
    {"name": "Skeleton", "hp": 15, "dropgold": 10, "attack": 5},
]


def combat(enemy):
    print(f"\nA wild {enemy['name']} appears!")

    while enemy["hp"] > 0 and player["health"] > 0:
        print("\n===FIGHT===")
        print(f'\n"{player["name"]}" HP: {player["health"]}')
        print(f"{enemy['name']} HP: {enemy['hp']}")
        print("1. Attack")
        print("2. Magic / Healing")
        print("3. Switch weapon")
        print("4. Run")

        choice = input("> ")


        if choice == "1":
            print(f"\nYou are wielding an iron sword. Damage: {player['weapondamage']}")
            print("Attack? Y/N")
            attackinp = input("> ")

            if attackinp.lower() in ["y", "yes"]:
                print("e")

def main():
    print("==== WELCOME! ===")
    time.sleep(1)
    print("\nWhat's your name?")
    player["name"] = input("> ")
    combat(enemy_templates[0])

main()