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
            print("\n\n1. Go to the shop\n2. Go to the mineshafts\n3. Explore")
            input("\n> ")



            
        









main()