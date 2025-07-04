from combat import clear_screen
from game_data import player, inventory, weapons, enemy_templates, misc
import random
import time
import os
import sys




def center_text(text):
    # Get terminal width and center the text
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80  # fallback width
    return text.center(width)



def flashing_dots(duration=5, interval=0.5):
    end_time = time.time() + duration
    dots = ['', '.', '..', '...']
    i = 0
    while time.time() < end_time:
        clear_screen()
        print(center_text(dots[i % len(dots)]))
        i += 1
        time.sleep(interval)
    clear_screen()





#entrance 
def txt1():
    clear_screen()
    print("Strange Woman: You've been asleep for quite some time now...")
    input("\n")
    clear_screen()
    print("Strange Woman: You've been asleep for quite some time now...")
    print("Strange Woman: I found you in the woods. You looked hurt, so I took you home.")
    input("\n")
    clear_screen()
    print("Strange Woman: You've been asleep for quite some time now...")
    print("Strange Woman: I found you in the woods. You looked hurt, so I took you home.")
    print("Strange Woman: I don't mean to be rude... but who are you?")
    input("\n")
    clear_screen()
    player["name"] = input("\n\033[1mWho am I?\033[0m\nI am.. ")
    clear_screen()
    print(f"Strange Woman: {player['name']}, Huh?")
    input("\n")
    clear_screen()
    print(f"Strange Woman: {player['name']}, Huh?")
    print("Strange woman: I feel like I've heard that name before.")
    input("\n")
    clear_screen()
    print(f"Strange Woman: {player['name']}, Huh?")
    print("Strange woman: I feel like I've heard that name before.")
    print("Strange Woman: Doesn't matter.. I'll go get you some clothes.")
    input("\n")
    print("Strange Woman: I'll get you some clothes..")
    clear_screen()
    print(f"Strange Woman: {player['name']}, Huh?")
    print("Strange woman: I feel like I've heard that name before.")
    print("Strange Woman: Doesn't matter.. I'll go get you some clothes.")
    input("\n")
    flashing_dots()
    clear_screen()
    print("Strange Woman: Here you go!")
    input("\n")
    clear_screen()
    print(center_text("\033[1mShe gave you raggy clothes!\033[0m"))
    player["armour"] = "raggy"
    input("\n\n\n")
    clear_screen()
    print("Strange Woman: Oh!")
    input("\n")
    clear_screen()
    print("Strange Woman: Oh! How awfully rude of me!")
    input("\n")
    clear_screen()
    print("Strange Woman: Oh! How awfully rude of me!")
    print("Strange Woman: I forgot to introduce myself! My name is Anwen!")
    input("\n")
    clear_screen()
    print("Anwen: Oh! How awfully rude of me!")
    print("Anwen: I forgot to introduce myself! My name is Anwen!")
    print("Anwen: I'm pleased to meet you.")
    input("\n")
    clear_screen()
    print("Anwen: Oh! How awfully rude of me!")
    print("Anwen: I forgot to introduce myself! My name is Anwen!")
    print("Anwen: I'm pleased to meet you.")
    print("Anwen: Do you already know the town you're in?, You know, based off where you were in the woods.")
    input("\n")
    clear_screen()
    print("Anwen: I forgot to introduce myself! My name is Anwen!")
    print("Anwen: I'm pleased to meet you.")
    print("Anwen: Do you already know the town you're in?, You know, based off where you were in the woods.")
    print("Anwen: No? It's called Elmvale.")
    input("\n")
    clear_screen()
    print("...")
    input("\n")
    clear_screen()
    print("Anwen: You going to say anything to that..?")
    input("\n")
    clear_screen()
    print("...")
    input("\n")
    clear_screen()
    print("Anwen: Not much of a talker, are you?")
    input("\n")
    clear_screen()
    print("Anwen: Oh well. Look, this town is not exactly.. the most hospitable or rich, it's quite the opposite.")
    input("\n")
    clear_screen()
    print("Anwen: Oh well. Look, this town is not exactly.. the most hospitable or rich, it's quite the opposite.")
    print("Anwen: I certainly hope you can fight, if not.. it's about time you learnt.")
    input("\n")
    clear_screen()
    print("Anwen: Oh well. Look, this town is not exactly.. the most hospitable or rich, it's quite the opposite.")
    print("Anwen: I certainly hope you can fight, if not.. it's about time you learnt.")
    print("Anwen: Or learn to use a sword well!")
    input("\n")
    clear_screen()
    print("Anwen: Oh well. Look, this town is not exactly.. the most hospitable or rich, it's quite the opposite.")
    print("Anwen: I certainly hope you can fight, if not.. it's about time you learnt.")
    print("Anwen: Or learn to use a sword well!")
    print("Anwen: Theres nothing of note here, to be honest, now, I told you Elmvale is poor, as am I. Thus can't keep you here forever.")
    input("\n")
    clear_screen()
    print("Anwen: I certainly hope you can fight, if not.. it's about time you learnt.")
    print("Anwen: Or learn to use a sword well!")
    print("Anwen: Theres nothing of note here, to be honest, now, I told you Elmvale is poor, as am I. Thus can't keep you here forever.")
    print("Anwen: Tragic, I know. But..! I'll let you sleep here sometimes. Do note though, don't count on me saving you again!")
    input("\n")
    clear_screen()
    print("Anwen: Or learn to use a sword well!")
    print("Anwen: That should be about everything. I told you Elmvale is poor, as am I. I can't keep you here forever.")
    print("Anwen: Tragic, I know. But..! I'll let you sleep here sometimes. Do note though, don't count on me saving you again!")
    print("Anwen: I have to go to work.. So you go off and.. do whatever, I don't know. Just don't get yourself killed.")
    input("\n")
    clear_screen()
    print(center_text("\033[1mAnwen shoves you out the door.\033[0m"))
    input("\n\n\n\n")
    clear_screen()
    print(center_text("\033[1mIt appears to be the later morning. The sun is up and birds are singing.\033[0m"))
    input("\n\n\n\n")
    clear_screen()
    print(center_text("\033[1mThis place doesn't look all that bad though, odd.\033[0m"))
    input("\n\n\n\n")
    clear_screen()



