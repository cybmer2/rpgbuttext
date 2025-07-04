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




        if misc["location"] == "Village":
            clear_screen()
            print("=== Village ===")
            print("What would you like to do?")
            print("\n\n1. Go to the shop\n2. Go to the mineshafts\n3. Explore\n4. Other")
            choice == input("\n> ")
            if choice == "4":
                misc["location"] = "Other"
                misc["lastlocation"] = "Village"


        if misc["location"] == "Other":
            clear_screen()
            print("=== Misc ===")
            print("What would you like to do?")
            print("\n1. Save my game.\n2. Check my stats.\n3. Check my inventory.\n4. Commit suicide\n5. Eat / Heal\n6. Go back")
            if choice == "6":
                misc["location"] = misc["lastlocation"]
            if choice == "2":
                clear_screen()
                
            
            



            
        









main()