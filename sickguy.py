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
    "weaponluck": 25,
    "speed": 100,

    
}

#lower confidence = higher chance of running away
#min of 1
#high confidence = lower chance of running away
#20 is extremely high confidence, 1 in 20 chance of running away

enemy_templates = [
    {"name": "Goblin", "hp": 10, "dropgold": 5, "attack": 3, "luck": 10, "confidence": 3,},
    {"name": "Golem", "hp": 40, "dropgold": 20, "attack": 5, "luck": 0, "confidence": 8,},
    {"name": "Skeleton", "hp": 15, "dropgold": 10, "attack": 5, "luck": 0, "confidence": 5,},
]



def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')




def combat(enemy):
    emaxhealth = enemy['hp']
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
                    clear_screen()
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
                    damage = ((luck_roll / 100) +1) * player["weapondamage"]
                    damage = round(damage, 1)
                    enemy["hp"] -= damage
                    enemy["hp"] = round(enemy["hp"], 1)
                    print(f"\nYou did {damage} damage!\nThe {enemy['name']} has {enemy['hp']} health remaining!")
                    time.sleep(3)
                else:
                    damage = ((luck_roll / 100) +1) * player["weapondamage"]
                    damage = damage + player["damage"]
                    damage = round(damage, 1)
                    enemy["hp"] -= damage
                    enemy["hp"] = round(enemy["hp"], 1)
                    print(f"\nYour raw strength did {player['damage']} damage!\nIn total you did {damage} damage!\nThe {enemy['name']} has {enemy['hp']} health remaining!")
                    time.sleep(3) 
                    
                #attackback
                clear_screen()
                luck = enemy['luck']
                ehealth = enemy['hp']
                damage = enemy['luck']
                waittime = random.randint(0.25, 3)
                print(f"The {enemy['name']} is deciding what to do...")
                if ehealth < 0.15 * emaxhealth:
                    #runaway



                time.sleep(waittime)
                if luck != 0:
                    luck_roll = random.randint(-luck, luck)
                    if luck_roll > 0:
                        print(f"Your enemmy acquires {luck_roll} extra damage through luck.")
                    if luck_roll < 0:
                        print(f"Your enemy looses {luck_roll} damage through luck.")
                time.sleep(0.5)
                    
                
            









def main():
    print("==== WELCOME! ===")
    time.sleep(1)
    print("\nWhat's your name?")
    player["name"] = input("> ")
    combat(enemy_templates[0])

main()