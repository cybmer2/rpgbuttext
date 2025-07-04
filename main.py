from game_data import player, inventory, weapons, enemy_templates, misc, armours
from combat import combat, clear_screen, genenemy, geneweap
from text import txt1, center_text
import random
import time
import os






def main():
    clear_screen()
    while True:
        clear_screen()
        if misc["location"] == "Main Menu":
            print("=== Main Menu ===")
            print("What would you like to do?")
            print("\n\n1. Start a save file.\n2. Load a save file.\n3. Play around (Sandbox)")
            choice = input("\n> ")
            if choice == "1":
                clear_screen()
                txt1()
                misc["location"] = "Village"
            if choice =="3":
                misc["location"] = "Village"




        if misc["location"] == "Village":
            clear_screen()
            print("=== Village ===")
            print("What would you like to do?")
            print("\n\n1. Go to the shop\n2. Think really hard\n3. Explore\n4. Other")
            choice = input("\n> ")
            if choice == "4":
                misc["location"] = "Other"
                misc["lastlocation"] = "Village"


        if misc["location"] == "Other":
            clear_screen()
            print("=== Misc ===")
            print("What would you like to do?")
            print("\n1. Save my game.\n2. Check my stats.\n3. Check my weapons.\n4. Commit suicide\n5. Eat / Heal\n6. Go back")
            choice = input("\n> ")
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




        if choice == "3":
            clear_screen()
            print("=== Village ===")
            print("Where would you lieke to go?")
            print("\n\n1. Spooky Cave.\n2. Mineshafts\n3. Village Outskirts.\n4. Dojo")
            choice = input("\n> ")
            if choice == "1":
                misc["location"] = "Cave"
                misc["lastlocation"] = "Village"

        
        if misc["location"] == "Cave":
            if misc["cavevisits"] == 0:
                clear_screen()
                combat(genenemy("Goblin", 25, 5, 5, 25, 2.2, 15),geneweap("Goblin Brass Knuckles", 40, 6, 30, False, False, 70))
                misc["cavevisists"] = 1
                
            clear_screen()
            print("=== Cave ===")
            

            



            



            
        








misc["location"] = "Main Menu"
main()