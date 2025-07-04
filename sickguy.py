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
    "speed": 100,
    "ranged": False
    
}

#confidence 1-10
#

enemy_templates = [
    {"name": "Goblin", "hp": 10, "dropgold": 5, "attack": 3, "luck": 10, "confidence": 1,},
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
                                time.sleep(5)
                            else:
                                ranaway = 1
                                print("The goblin got away!")
                                time.sleep(5)
                        else:
                            ranaway = 1
                            print("The goblin got away!")
                            time.sleep(5)
                




                if luck != 0 and ranaway == 0 and caught == 0:
                    luck_roll = random.randint(-luck, luck)
                    if luck_roll > 0:
                        print(f"Your enemmy acquires {luck_roll} extra damage through luck.")
                        time.sleep(5)
                    if luck_roll < 0:
                        print(f"Your enemy looses {luck_roll} damage through luck.")
                        time.sleep(5)
                    
                
            









def main():
    print("==== WELCOME! ===")
    time.sleep(1)
    print("\nWhat's your name?")
    player["name"] = input("> ")
    combat(enemy_templates[0])

main()