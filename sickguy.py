import random
import time
import os


player = {
    "name": "bob",
    "health": 100,
    "max_health": 200,
    "damage": 0,
    "speed": 15,
    "gold": 50,
    "potions": 0,
    "weapon": "Iron Sword",
    "weapondamage": 6,
    "weaponluck": 25

    
}



enemy_templates = [
    {"name": "Goblin", "hp": 10, "dropgold": 5, "attack": 3},
    {"name": "Golem", "hp": 40, "dropgold": 20, "attack": 5},
    {"name": "Skeleton", "hp": 15, "dropgold": 10, "attack": 5},
]



def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')




def combat(enemy):

    while enemy["hp"] > 0 and player["health"] > 0:
        clear_screen()
        print("===FIGHT===")

        print(f"\nYou are fighting a {enemy['name']}.")
        print(f'\n"{player["name"]}" HP: {player["health"]}')
        print(f"{enemy['name']} HP: {enemy['hp']}")
        print("\n\n1. Attack")
        print("2. Magic / Healing")
        print("3. Switch weapon")
        print("4. Run")

        choice = input("> ")


        if choice == "1":
            clear_screen()
            print(f"You are wielding an iron sword.\nDamage: {player['weapondamage']}\nLuck: ±{player['weaponluck']}%")
            print("Attack? Y/N")
            attackinp = input("> ")
            luck = player["weaponluck"]
            if attackinp.lower() in ["y", "yes"]:
                #attack


                luck_roll = random.randint(-luck, luck)
                if luck != 0:
                    if luck_roll == luck:
                        print(f"You got insanely lucky! (+{luck_roll}%)")
                    elif luck_roll >= 0.75 * luck:
                        print(f"You got very lucky! (+{luck_roll}%)")
                    elif luck_roll >= 0.5 * luck:
                        print(f"You got lucky. (+{luck_roll}%)")
                    elif luck_roll >= 0:
                        print(f"You got mediocrely lucky. (+{luck_roll}%)")
                    elif luck_roll == -luck:
                        print(f"You got insanely unlucky! ({luck_roll}%)")
                    elif luck_roll <= -0.75 * luck:
                        print(f"You got very unlucky. ({luck_roll}%)")
                    elif luck_roll <= -0.5 * luck:
                        print(f"You got unlucky. ({luck_roll}%)")
                    else:
                        print(f"You got mediocrely unlucky. ({luck_roll}%)")
                
                if player["damage"] == 0:
                    clear_screen()
                    damage = ((luck_roll / 100) +1) * player["weapondamage"]
                    enemy["hp"] -= damage
                    round(enemy["hp"], 1)
                    print(f"You did {damage} damage!\nThe {enemy['name']} has {enemy['hp']} remaining!")
                    





def main():
    print("==== WELCOME! ===")
    time.sleep(1)
    print("\nWhat's your name?")
    player["name"] = input("> ")
    combat(enemy_templates[0])

main()