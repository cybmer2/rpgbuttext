from game_data import player, inventory, weapons, enemy_templates, misc
from combat import combat, clear_screen
from text import txt1
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
            print("\n\n1. Go to the shop\n2. Go to the mineshafts\n3. Explore\n4. Other")
            choice = input("\n> ")
            if choice == "4":
                misc["location"] = "Other"
                misc["lastlocation"] = "Village"


        if misc["location"] == "Other":
            clear_screen()
            print("=== Misc ===")
            print("What would you like to do?")
            print("\n1. Save my game.\n2. Check my stats.\n3. Check my inventory.\n4. Commit suicide\n5. Eat / Heal\n6. Go back")
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
                input("\n\nFINISH")
            
            



            
        








misc["location"] = "Main Menu"
main()