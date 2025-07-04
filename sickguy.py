import random
import time
import os


player = {
    "name": "bob",
    "health": 100,
    "max_health": 100,
    "damage": 2,
    "speed": 20,
    "gold": 50,
    "potions": 0,
    "weapon": "Iron Sword",
    "weapondamage": 6,
    "weaponluck": 25,
    "weapondurability": 25,
    "magic": False,
    "speed": 100,
    "ranged": False
    
}

inventory = {
    "bandaid": 0,
    "l1healpot": 2,
    "bow": 1,
    "ironsword": 1,
    "arrow": 15,

}

weapons = [
    {"name": "Fists", "Luck": 60, "Damage": 2, "Durability": False, "Obtained": True, "Ranged": False, "Magic": False},
    {"name": "Iron sword", "Luck": 25, "Damage": 6, "Durability": 25, "Obtained": True, "Ranged": False, "Magic": False},
    {"name": "Bow", "Luck": 60, "Damage": 20, "Durability": 80, "Obtained": True, "Ranged": True, "Magic": False},
    {"name": "Katana", "Luck": 40, "Damage": 30, "Durability": 400, "Obtained": False, "Ranged": False, "Magic": False},
    {"name": "Firestaff", "Luck": 0, "Damage": 30, "Durability": 400, "Obtained": False, "Ranged": False, "Magic": True}
]



magic = False

#confidence 1-10
#

enemy_templates = [
    {"name": "Goblin", "hp": 10, "dropgold": 5, "attack": 3, "luck": 10, "confidence": 2.2,},
    {"name": "Golem", "hp": 40, "dropgold": 20, "attack": 5, "luck": 5, "confidence": 4 ,},
    {"name": "Skeleton", "hp": 15, "dropgold": 10, "attack": 5, "luck": 15, "confidence": 2,},
]



def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')




def combat(enemy):
    emaxhealth = enemy['hp']
    ranaway = 0
    while enemy["hp"] > 0 and player["health"] > 0 and ranaway != 1:
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
            print(f"You are wielding: {player['weapon']}.\nDamage: {player['weapondamage']}\nLuck: ±{player['weaponluck']}%")
            print("Attack? Y/N")
            attackinp = input("> ")
            luck = player["weaponluck"]
            if attackinp.lower() in ["y", "yes"]:
                #attack


                luck_roll = random.uniform(-luck, luck)
                luck_roll = round(luck_roll, 1)
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
                    print(f"\nYour raw strength added {player['damage']} damage! (Not luck affected.)\nIn total you did {damage} damage!\nThe {enemy['name']} has {enemy['hp']} health remaining!")
                    time.sleep(0.6)
                    input("\n\nCONTINUE")
                    





                
                #runawaying
                clear_screen()
                ranaway = 0
                caught = 0
                luck = enemy['luck']
                ehealth = enemy['hp']
                damage = enemy['luck']
                player_health = player['health']
                player_maxhp = player['max_health']
                confidence = enemy['confidence']
                waittime = random.uniform(1, 3)
                print(f"The {enemy['name']} is deciding what to do...")
                time.sleep(waittime)
                if ehealth < 0.5 * emaxhealth and player_health > 0.6 * player_maxhp:
                    health_ratio = ehealth / emaxhealth
                    run_chance = 1 - health_ratio
                    confidence_factor = confidence / 10.0
                    run_chance = run_chance * ( 1 - confidence_factor)
                    run_chance = max(0.0, min(run_chance, 1.0))

                    if random.random() < run_chance:
                        print(f"The {enemy['name']} assesses the situation and realises it's doomed, and runs away!")
                        print(f"Do you want to chase the {enemy['name']}? Y/N")
                        chase = input("> ")
                        if chase.lower() in ["y", "yes"]:
                            player_speed = max(20, min(player['speed'], 400))
                            speed_ratio = (player_speed - 20) / (400-20)
                            health_ratio = ehealth / emaxhealth
                            health_factor = 1 - health_ratio

                            catch_chance = 0.5 * speed_ratio + 0.5 * health_factor
                            catch_chance = max(0.0, min(catch_chance, 1.0))

                            if random.random() < catch_chance:
                                print(f"You managed to catch up!")
                                caught = 1
                                time.sleep(0.6)
                                input("\n\nCONTINUE")
                            else:
                                ranaway = 1
                                print("The goblin got away!")
                                time.sleep(0.6)
                                input("\n\nCONTINUE")
                        else:
                            ranaway = 1
                            print("The goblin got away!")
                            time.sleep(0.6)
                            input("\n\nCONTINUE")
                




                if luck != 0 and ranaway == 0 and caught == 0:
                    luck_roll = random.uniform(-luck, luck)
                    luck_roll = round(luck_roll, 1)
                    if luck_roll > 0:
                        print(f"Your enemy acquires {luck_roll} extra damage through luck.")
                    if luck_roll < 0:
                        print(f"Your enemy looses {luck_roll} damage through luck.")
                    if luck_roll == 0:
                        print("Your enemies luck damage stays unchanged!")
                if ranaway == 0 and caught == 0:
                    damage = luck_roll + enemy['attack']
                    damage = round(damage, 1)
                    player['health'] -= damage
                    time.sleep(3)
                    print(f"\nYou took {damage} damage! You have {player['health']} health left.")
                    time.sleep(0.6)
                    input("\n\nCONTINUE")



        if choice == "2":
            if player['magic'] == True:
                choice2 = input("Would you like to do magic or heal?\n > ")
            else:
                choice2 = "y"
        
        if choice == "2" and choice2.lower() in ["y", "yes"]:
            clear_screen()
            print(f"{inventory['bandaid']} - BANDAIDS (1)")
            print(f"{inventory['l1healpot']} - HEALING POTIONS (2)")
            bandaids = inventory["bandaid"]
            l1hpot = inventory["l1healpot"]
            choice3 = input("\n\n> ")
            if choice3 == "1" and bandaids > 0:
                clear_screen()
                print("Putting this bandaid on will heal you by 5 health.")
                print(f"Current health: {player['health']}, Max Health: {player['max_health']}")
                print("\n\nDo you wish to consume it? (Will NOT use a turn.) Y/N")
                choice2 = input("> ")
                if choice2.lower() in ["y", "yes"]:
                    clear_screen()
                    inventory['bandaid'] -= 1
                    player['health'] += 5
                    if player["max_health"] < player["health"]:
                        player["health"] = player["max_health"]
                    print(f"Your new health is {player['health']}.")
                    time.sleep(0.6)
                    input("\n\nCONTINUE")
            elif choice3 == "1":
                clear_screen()
                print("You do not have any bandaids to apply.")
                time.sleep(0.6)
                input("\n\nCONTINUE")

            if choice3 == "2" and l1hpot > 0:
                clear_screen()
                print("Drinking this will heal you by 15 health.")
                print(f"Current health: {player['health']}, Max Health: {player['max_health']}")
                print("\n\nDo you wish to consume it? (Will NOT use a turn.) Y/N")
                choice2 = input("> ")
                if choice2.lower() in ["y", "yes"]:
                    clear_screen()
                    inventory['l1healpot'] -= 1
                    player['health'] += 15
                    if player["max_health"] < player["health"]:
                        player["health"] = player["max_health"]
                    print(f"Your new health is {player['health']}.")
                    time.sleep(0.6)
                    input("\n\nCONTINUE")
            elif choice3 == "2":
                clear_screen()
                print("You do not have any health potions to consume.")
                time.sleep(0.6)
                input("\n\nCONTINUE")




        if choice == "3":
            clear_screen()
            print("===AVAILABLE WEAPONS===\n\n\n")
            obtained_weapons = [w for w in weapons if w["Obtained"]]
            for idx, weapon in enumerate(obtained_weapons, 1):
                print(f"{idx}. {weapon['name']} (Damage: {weapon['Damage']}, Luck: {weapon['Luck']})")
            choice = input("\n\nChoose a weapon.\n> ")
            selected_weapon = None
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(obtained_weapons):
                    selected_weapon = obtained_weapons[index]
                else:
                    clear_screen()
                    print("Invalid choice. Defaulting to Fists.")
                    time.wait(2)
            else:
                clear_screen()
                print("Invalid input. Defaulting to Fists.")
                time.wait(2)
            if not selected_weapon:
                selected_weapon = next(w for w in weapons if w["name"] == "Fists")
            player["weapon"] = selected_weapon["name"]
            player["weapondamage"] = selected_weapon["Damage"]
            player["weaponluck"] = selected_weapon["Luck"]
            player["weapondurability"] = selected_weapon["Durability"]
            player["ranged"] = selected_weapon["Ranged"]
            player["magic"] = selected_weapon["Magic"]

            clear_screen()
            print(f"You selected: {selected_weapon['name']}")
            print(f"Damage: {selected_weapon['Damage']}, Luck: {selected_weapon['Luck']}, Durability: {selected_weapon['Durability']}")
            input("\n\nCONTINUE")




        







            


                   
                    
                
            









def main():
    print("==== WELCOME! ===")
    time.sleep(1)
    print("\nWhat's your name?")
    player["name"] = input("> ")
    combat(enemy_templates[0])
main()