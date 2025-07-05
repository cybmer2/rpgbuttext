from game_data import player, inventory, weapons, enemy_templates, misc, armours, spells
from combat import combat, clear_screen, genenemy, geneweap
from text import *
import random
import time
import os
import json



def save_game(filename="savegame.json"):
    save_data = {
        "player": player,
        "inventory": inventory,
        "misc": misc,
        "weapons": [{k: w[k] for k in ("name", "Obtained")} for w in weapons],
        "spells": [{k: s[k] for k in ("name", "Obtained")} for s in spells],
        "armours": [{k: a[k] for k in ("name", "Obtained")} for a in armours],
    }
    with open(filename, "w") as f:
        json.dump(save_data, f, indent=4)
    clear_screen()
    print("Game Saved!")
    input("\n> ")

def load_game(filename="savegame.json"):
    global player, inventory, misc, weapons, spells, armours
    try:
        with open(filename, "r") as f:
            save_data = json.load(f)
        player.update(save_data["player"])
        inventory.update(save_data["inventory"])
        misc.update(save_data["misc"])


        for saved_weapon in save_data["weapons"]:
            for w in weapons:
                if w["name"] == saved_weapon["name"]:
                    w["Obtained"] = saved_weapon["Obtained"]
        for saved_spell in save_data["spells"]:
            for s in spells:
                if s["name"] == saved_spell["name"]:
                    s["Obtained"] = saved_spell["Obtained"]
        for saved_armour in save_data["armours"]:
            for a in armours:
                if a["name"] == saved_armour["name"]:
                    a["Obtained"] = saved_armour["Obtained"]

        clear_screen()
        print("Game loaded!")
        input("\n")
        
    except FileNotFoundError:
        clear_screen()
        print("No save file found.")
        input("\n")


def main():
    clear_screen()
    while True:
        clear_screen()
        if misc["location"] == "Main Menu":
            print("=== Main Menu ===")
            print("What would you like to do?")
            print("\n\n1. Start a save file.\n2. Load a save file.")
            choice = input("\n> ")
            if choice == "2":
                load_game()
            if choice == "1":
                clear_screen()
                txt1()
                misc["location"] = "Village"
            if choice =="3":
                misc["location"] = "Village"




        if misc["location"].lower() == "village":
            clear_screen()
            print("=== Village ===")
            print("What would you like to do?")
            print("\n1. Explore\n2. Misc ")
            choice = input("\n> ")
            if choice == "2":
                misc["location"] = "Other"
                misc["lastlocation"] = "Village"


        if misc["location"].lower() == "other":
            clear_screen()
            print("=== Misc ===")
            print("What would you like to do?")
            print("\n1. Save my game.\n2. Check my stats.\n3. Check my weapons.\n4. Commit suicide\n5. Eat / Heal\n6. Go back\n7. Load my game")
            choice = input("\n> ")
            if choice == "1":
                save_game()
            if choice == "7":
                load_game()
            if choice == "6":
                misc["location"] = misc["lastlocation"]
            if choice == "2":
                clear_screen()
                print("=== Stats ===")
                print(f"\n\nName: {player["name"]}")
                print(f"\nHealth: {player["health"]}")
                print(f"Max Health: {player["max_health"]}")
                print(f"Speed: {player["speed"]}")
                print(f"\nGold: {player["gold"]}")
                print(f"Not-Expended Experience: {player["xp"]}")
                print(f"\n\nSword Mastery: {player["swordskill"]}")
                print(f"Magic Mastery: {player["magicskill"]}")
                print(f"Raw Strength: {player["damage"]}")
                input("\n\nFINISH")   
            if choice == "3":
                clear_screen()
                print("=== Inventory ===")
                print(f"\nCurrent weapon: \"{player["weapon"]}\"")     
                print(f"Damage: {player["weapondamage"]}")
                print(f"Luck: {player["weaponluck"]}")  
                print(f"Durability: {player["weapondurability"]}") 
                if player["magic"] == True:
                    print(f"Is a magic weapon") 
                else:
                    print("Is not a magic weapon")
                if player["ranged"] == True:
                    print("Is a ranged weapon")
                else:
                    print("Is not a ranged weapon")
                print(f"\n\nCurrent Armour: {player["armour"]}")
                print(f"Protection: {player["protection"]}")
                print(f"Luck resistance: {player["luckproof"]}")
                print(f"Sword Resistance: {player["swordres"]}")
                print(f"Magic Resistance: {player["magicres"]}")
                
                print("\nChange armour / weapon?")
                print("w for weapon, a for armour. Anything else exits.")
                choice2 = input("\n> ")

                #weapon
                if choice2.lower() == "w":
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
                    #armour


                if choice2.lower() == "a":
                    clear_screen()

                    print("===AVAILABLE ARMOUR===\n\n\n")
                    obtained_armours = [a for a in armours if a["Obtained"]]
                    for idx, armour in enumerate(obtained_armours, 1):
                        print(f"{idx}. {armour['name']} (Protection: {armour['protection']}, Luckproof: {armour['luckproof']})")
                    choice = input("\n\nChoose your armour.\n> ")
                    selected_armour = None
                    if choice.isdigit():
                        index = int(choice) - 1
                        if 0 <= index < len(obtained_armours):
                            selected_armour = obtained_armours[index]
                        else:
                            clear_screen()
                            print("Invalid choice. Defaulting to Naked.")
                            time.wait(2)
                    else:
                        clear_screen()
                        print("Invalid input. Defaulting to Naked.")
                        time.wait(2)
                    if not selected_armour:
                        selected_armour = next(a for a in armours if a["name"] == "Naked")
                    player["armour"] = selected_armour["name"]
                    player["protection"] = selected_armour["protection"]
                    player["luckproof"] = selected_armour["luckproof"]
                    player["swordres"] = selected_armour["swordres"]
                    player["magicres"] = selected_armour["magicres"]

                    clear_screen()
                    print(f"You equipped: {selected_armour['name']}")
                    print(f"Protection: {selected_armour['protection']}, Luckproof: {selected_armour['luckproof']}, Sword Resistance: {selected_armour['swordres']}, Magic Resistance: {selected_armour['magicres']}")
                    input("\n\nCONTINUE")
            if choice == "4":
                clear_screen()
                print("=== SUICIDE ===")
                print("\n\n\nSuicide is never the answer.")
                print("\n\n\nDo it anyway? Y/N")
                choice2 = input("\n> ")
                if choice2.lower() in ["y", "yes"]:
                    clear_screen()
                    print("=== SUICIDE ===")
                    print("Are you SURE?")
                    print("Type out \"YES\" (Case sensitive!)")
                    choice2 = input("\n> ")
                    if choice2 == "YES":
                        print("suicide")
                        player["health"] = -99999999999999
                        exit()
            if choice == "4":
                misc["lastlocation"] = misc["location"]











        if choice == "1":
            clear_screen()
            print("=== Village ===")
            print("Where would you like to go?")
            print("\n1. Spooky Cave\n2. Dojo.\n3. Home.")
            choice = input("\n> ")
            if choice == "1":
                misc["lastlocation"] = misc["location"]
                misc["location"] = "Cave"
            if choice == "2":
                misc["lastlocation"] = "village"
                misc["location"] = "dojo"
            if choice == "3":
                misc["lastlocation"] = "village"
                misc["location"] = "home"



        if misc["location"].lower() == "home":
            clear_screen()
            print("=== Anwen's home ===")
            print("What would you like to do?\n\n1. Steal 2 door handles\n2. Leave")
            choice = input("\n>")
            if choice == "1":
                clear_screen()
                print("You stole 2 door handles.")
                misc["doorhandles"] = 2
            if choice == "2":
                misc["location"] = "village"
                misc["lastlocation"] = "home"



        if misc["location"].lower() == "dojo":
            if misc["dojovisit"] == "no":
                txt5()
                misc["dojovisit"] = "yes"
            clear_screen()
            print("=== Dojo ====")
            print("What would you like to do?")
            if misc["magicunlocked"] == False:
                print("\n\n1. Inquire about unlocking magic\n2. Ask to be trained in the art of swordsmanship\n3. Spend time working agility \n4. Spend time working on your strength\n5. Leave")
            if misc["magicunlocked"] == True:
                print("\n\n1. Ask to be trained in magic\n2. Ask to be trained in the art of swordsmanship\n3. Spend time working agility \n4. Spend time working on your strength\n5. Leave")
            choice = input("\n> ")
            if choice == "1":
                if misc["magicasked"] == False and misc["magicunlocked"] == False:
                    txt6()
                    misc["magicasked"] = True
                else:
                    if misc["doorhandles"] != 2:
                        txt7()

                    elif misc["magicunlocked"] == False:
                        txt8()
                        misc["magicunlocked"] = True

                if misc["magicunlocked"] == True:
                    clear_screen()
                    print("=== Magic Technique \"Store\" ===")
                    print("What would you like to learn?")
                    print("\n")
                    print(f"Your available XP {player["xp"]}")
                    available_spells = [spell for spell in spells if not spell["Obtained"]]
                    if not available_spells: 
                        print("You own all the spells!")
                        break
                    print("Available spells to buy:")
                    for i, spell in enumerate(available_spells):
                        print(f"{i + 1}. {spell['name']} (Mana: {spell['Mana']}, Cost: {spell['Cost']} XP)")
                    choice = input("\nEnter spell number to buy.\n> ").strip()

                    if not choice.isdigit() or not (1 <= int(choice) <= len(available_spells)):
                        print("Invalid.")
                        continue

                    selected_spell = available_spells[int(choice) - 1]

                    if player["xp"] >= selected_spell["Cost"]:
                        player["xp"] -= selected_spell["Cost"]
                        selected_spell["Obtained"] = True
                        print(f"You bought {selected_spell['name']}")
                    else:
                        clear_screen()
                        print("Not enough XP.")
                        input("\n\n")







                    
                

                
            


                
        
        
        if misc["location"].lower() == "cave":
            if misc["cavevisits"] == 0:
                misc["cavevisits"] = 1
                clear_screen()
                txt2()
                combat(genenemy("Goblin", 10, 100, 1, 75, 100, 150),geneweap("Goblin Brass Knuckles", 40, 4, 30, False, False, 100))
                txt3()         # name, hp, dropgold, attack, luck, confidence, dropxp | name, wluck, damage, durability, ranged, magic, dropchance
                combat(genenemy("Bigger Goblin", 25, 250, 3, 30, 1, 300),geneweap("Goblin Dagger", 70, 10, 100, False, False, 100))
                txt4()
            clear_screen()
            print("=== Cave ===")
            print("What would you like to do?")
            print("\n\n1. Go into the shiny green area\n2. Enter into the rather dark area\n3. Leave\n4. Other")
            choice = input("\n> ")
            if choice == "1" or "2":
                misc["lastlocation"] = misc["location"]
                misc["location"] = "notadded"
            if choice == "3":
                misc["location"] = "Village"
                misc["lastlocation"] = misc["location"]
            if choice == "4":
                misc["lastlocation"] = "cave"
                misc["location"] = "other"
        








        if misc["location"].lower() == "notadded":
            clear_screen()
            print("Sorry!\n\n\nThis place hasn't been added yet as this was made primarily in a 30 hour coding sprint! Enter literally anything to go back :3")
            input("\n> ")
            misc["location"] = misc["lastlocation"]
        

        

            

            



            



            
        








misc["location"] = "Main Menu"
main()