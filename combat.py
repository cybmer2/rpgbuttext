from game_data import player, inventory, weapons, enemy_templates
import random
import time
import os



def geneweap(name, wluck, damage, durability, ranged, magic, dropchance):
    """Generate a weapon dictionary."""
    weapon = {
        "name": name,
        "wluck": wluck,
        "damage": damage,
        "durability": durability,
        "ranged": ranged,
        "magic": magic,
        "dropchance": dropchance,
        "blessed": False  # Default no blessing
    }
    return weapon




def genenemy(name, hp, dropgold, attack, luck, confidence, dropxp):
    """Generate enemy dictionary."""
    enemy = {
        "name": name,
        "hp": hp,
        "dropgold": dropgold,
        "attack": attack,
        "luck": luck,
        "confidence": confidence,
        "dropxp": dropxp
    }
    return enemy


def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')






def combat(enemy, weapon_drop):
    emaxhealth = enemy['hp']
    ranaway = 0
    weapon_used = weapon_drop['name']
    weapon_type = 'Sword' if not weapon_drop['ranged'] and not weapon_drop['magic'] else 'magic' if weapon_drop['magic'] else 'ranged'

    while enemy['hp'] > 0 and player['health'] > 0 and ranaway != 1:
        clear_screen()
        print("===FIGHT===")
        print(f"\nYou are fighting a {enemy['name']} who is using a {weapon_used} ({weapon_type}).")
        print(f"\n\"{player['name']}\" HP: {player['health']}\n{enemy['name']} HP: {enemy['hp']}")
        print("\n\n1. Attack\n2. Magic / Healing\n3. Switch weapon\n4. Run")
        choice = input("\n> ")

        if choice == "1":
            if player["weapondurability"] >= 1 or player["weapondurability"] == False:
                clear_screen()
                print(f"You are wielding: {player['weapon']}.\nDamage: {player['weapondamage']}\nLuck: ±{player['weaponluck']}%")
                print("Attack? Y/N")
                attackinp = input("> ")
                if attackinp.lower() in ["y", "yes"]:


                    clear_screen()
                    luck = player["weaponluck"]
                    luck_roll = round(random.uniform(-luck, luck), 1)
                    if luck != 0:


                        clear_screen()
                        if luck_roll == luck: print(f"You got insanely lucky! (+{luck_roll}%)")
                        elif luck_roll >= 0.75 * luck: print(f"You got very lucky! (+{luck_roll}%)")
                        elif luck_roll >= 0.5 * luck: print(f"You got lucky. (+{luck_roll}%)")
                        elif luck_roll >= 0: print(f"You got mediocrely lucky. (+{luck_roll}%)")
                        elif luck_roll == -luck: print(f"You got insanely unlucky! ({luck_roll}%)")
                        elif luck_roll <= -0.75 * luck: print(f"You got very unlucky. ({luck_roll}%)")
                        elif luck_roll <= -0.5 * luck: print(f"You got unlucky. ({luck_roll}%)")
                        else: print(f"You got mediocrely unlucky. ({luck_roll}%)")
                    skillmult = 1


                    if not player['ranged'] and not player['magic']: skillmult += player['swordskill']
                    elif player['magic']: skillmult += player['magicskill']

                    basedamage = ((luck_roll / 100) + 1) * player['weapondamage'] * skillmult

                    if player['damage'] != 0 and not player['ranged'] and not player['magic']: basedamage += player['damage']
                    basedamage = round(basedamage, 1)
                    
                    enemy['hp'] -= basedamage
                    enemy['hp'] = max(round(enemy['hp'], 1), 0)
                    if player['weapondurability'] != False: player['weapondurability'] -= 1
                    for w in weapons:
                        if w['name'] == player['weapon']:
                            w['Durability'] = player['weapondurability']
                            break
                    print(f"\nYou did Total Damage: {basedamage} ({round(player['damage'], 1)} - Raw Strength | {round(basedamage - player['damage'], 1)} - Weapon).\n{enemy['name']} has {enemy['hp']} HP remaining.")
                    time.sleep(0.6)
                    input("\n\nCONTINUE")




                    if enemy['hp'] != 0:
                        clear_screen()
                        ranaway = 0
                        caught = 0
                        luck = weapon_drop['wluck'] * (1 - player['luckproof'] / 100)
                        ehealth = enemy['hp']
                        confidence = enemy['confidence']
                        waittime = random.uniform(1, 3)
                        print(f"The {enemy['name']} is deciding what to do...")
                        time.sleep(waittime)
                        if ehealth < 0.5 * emaxhealth and player['health'] > 0.6 * player['max_health'] and ehealth > 0:
                            run_chance = (1 - (ehealth / emaxhealth)) * (1 - confidence / 10.0)
                            if random.random() < run_chance:
                                print(f"The {enemy['name']} runs away!")
                                print("Chase? Y/N")
                                chase = input("> ")
                                if chase.lower() in ["y", "yes"]:
                                    catch_chance = 0.5 * ((player['speed'] - 20) / 380) + 0.5 * (1 - ehealth / emaxhealth)
                                    if random.random() < catch_chance:
                                        print("You caught up!")
                                        caught = 1
                                    else:
                                        ranaway = 1
                                        print("The enemy escaped!")
                                else:
                                    ranaway = 1
                                    print("You let the enemy go.")
                                input("\n\nCONTINUE")




                        if enemy['hp'] != 0 and ranaway == 0 and caught == 0:
                            luck_roll = round(random.uniform(-luck, luck), 1)
                            edamage = weapon_drop['damage'] * ((luck_roll / 100) + 1)


                            if not weapon_drop['ranged'] and not weapon_drop['magic']:
                                edamage *= (1 - player['swordres'] / 100)
                            elif weapon_drop['magic']:
                            
                                edamage *= (1 - player['magicres'] / 100)


                            battack = enemy['attack']
                            luck = enemy['luck'] * (1 - player['luckproof'] / 100)
                            luck_roll = round(random.uniform(-luck, luck), 1)
                            battack = battack * ((luck_roll / 100) + 1)
                            battack = round(battack, 1)

                            battack *= (1 - player['protection'] / 200)
                            edamage *= (1 - player['protection'] / 200)
                            edamage = round(edamage, 1)
                            totaldamage = round((edamage + battack), 1)
                            player['health'] -= totaldamage
                            player['health'] = round(player['health'], 1)
                            print(f"\nThe {enemy['name']} attacks! He does {battack} via strength and {edamage} damage via his weapon (Total {totaldamage}). You have {player['health']} HP left.")
                            input("\n\nCONTINUE")

                    if enemy['hp'] == 0:
                        clear_screen()
                        gold = round(enemy['dropgold'] * random.uniform(0.9, 1.1), 1)
                        xp = round(enemy['dropxp'] * random.uniform(0.9, 1.1), 1)
                        print(f"You defeated the {enemy['name']}! You gain {gold} gold and {xp} XP.")
                        player['gold'] += gold
                        player['xp'] += xp
                        if random.uniform(0, 100) <= weapon_drop['dropchance']:
                            w = weapon_drop.copy()
                            key = f"{w['name']}|{w['durability']}"
                            if key in inventory:
                                inventory[key]['count'] += 1
                            else:
                                inventory[key] = {"weapon": w, "count": 1}
                            w_converted = {
                                'name': w['name'],
                                'Luck': w['wluck'],
                                'Damage': w['damage'],
                                'Durability': w['durability'],
                                'Obtained': True,
                                'Ranged': w['ranged'],
                                'Magic': w['magic']
                            }
                            weapons.append(w_converted)
                            print(f"You also found:\n\n\033[1m{w['name']}!\033[0m")
                        input("\n\nCONTINUE")



        elif choice == "2":
            clear_screen()
            has_potions = False
            options = []
            for i in range(1, 4):
                if inventory.get(f"l{i}healpot", 0) > 0:
                    print(f"{i} - Healing Potion L{i} ({inventory[f'l{i}healpot']})")
                    options.append(str(i))
                    has_potions = True
            if player['magic'] and inventory.get("manapot", 0) > 0:
                print(f"M - Mana Potion ({inventory['manapot']})")
                has_potions = True
            if not has_potions:
                print("NO POTIONS")
            choice3 = input("\n\n> ").lower()
            if choice3 in options:
                i = int(choice3)
                amount = round(random.uniform(5 * i, 5 * i + 5), 1)
                print(f"Healed {amount} HP.")
                player['health'] = min(player['health'] + amount, player['max_health'])
                inventory[f"l{i}healpot"] -= 1
            elif choice3 == "m" and player['magic'] and inventory.get("manapot", 0) > 0:
                print("Mana restored.")
                inventory["manapot"] -= 1
            input("\n\nCONTINUE")



        elif choice == "3":
            clear_screen()
            print("===AVAILABLE WEAPONS===\n\n\n")
            obtained_weapons = [w for w in weapons if w.get("Obtained", False)]
            for idx, weapon in enumerate(obtained_weapons, 1):
                print(f"{idx}. {weapon['name']} (Damage: {weapon['Damage']}, Luck: {weapon['Luck']}, Durability: {weapon['Durability']})")
            choice = input("\n\nChoose a weapon.\n> ")
            selected_weapon = None
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(obtained_weapons):
                    selected_weapon = obtained_weapons[index]
            if selected_weapon:
                player['weapon'] = selected_weapon['name']
                player['weapondamage'] = selected_weapon['Damage']
                player['weaponluck'] = selected_weapon['Luck']
                player['weapondurability'] = selected_weapon['Durability']
                player['ranged'] = selected_weapon['Ranged']
                player['magic'] = selected_weapon['Magic']
                clear_screen()
                print(f"You selected: {selected_weapon['name']}\nDamage: {selected_weapon['Damage']}, Luck: {selected_weapon['Luck']}, Durability: {selected_weapon['Durability']}")
            else:
                clear_screen()
                print("Invalid weapon choice.")
            input("\n\nCONTINUE")
            

        elif choice == "4":
            clear_screen()
            penalty = (player['health'] * 0.15) + (enemy['hp'] * 0.40)
            print("=== RUN AWAY ===")
            print(f"\n\nYou will lose {penalty:.1f} health, and have {max(player['health'] - penalty, 0):.1f} remaining.")
            print("\n\nAre you sure you want to run away? Y/N")
            choice2 = input("> ")
            if choice2.lower() in ["y", "yes"]:
                player['health'] = max(player['health'] - penalty, 0)
                ranaway = 1



            




        







            


                   
                    
                
            









