import random
import time
import os


inventory = {
    "bandaid": 0,
    "healpot": 0,
    "strengthpot": 0,
    "manapot": 0,
    "arrow": 0,

}



weapons = [
    {"name": "Fists", "Luck": 60, "Damage": 2, "Durability": False, "Obtained": True, "Ranged": False, "Magic": False},
    {"name": "Iron sword", "Luck": 25, "Damage": 6, "Durability": 25, "Obtained": True, "Ranged": False, "Magic": False},
    {"name": "Bow", "Luck": 60, "Damage": 20, "Durability": 80, "Obtained": True, "Ranged": True, "Magic": False},
    {"name": "Katana", "Luck": 40, "Damage": 30, "Durability": 400, "Obtained": False, "Ranged": False, "Magic": False},
    {"name": "Firestaff", "Luck": 0, "Damage": 30, "Durability": 400, "Obtained": True, "Ranged": False, "Magic": True},
    {"name": "Wooden Staff", "Luck": 30, "Damage": 5, "Durability": 150, "Obtained": True, "Ranged": False, "Magic": True},
]


enemy_weapons = [
    {"name": "Fists", "Luck": 60, "Damage": 2, "Durability": False, "Obtained": True, "Ranged": False, "Magic": False},

]

spells = [
    {"name": "Fireball", "Obtained": False, "Mana": 15, "Cost": 50},
    {"name": "Healing", "Obtained": False, "Mana": 30, "Cost": 200},
    {"name": "Domain Expansion", "Obtained": False, "Mana": 2500, "Cost": 7500},
    {"name": "Spin", "Obtained": False, "Mana": 5, "Cost": 400},
    {"name": "Double Swipe", "Obtained": False, "Mana": 50, "Cost": 500},
    {"name": "Freeze", "Obtained": False, "Mana": 100, "Cost": 1200},
    {"name": "Double Spell", "Obtained": False, "Mana": 200, "Cost": 1000},
    {"name": "Tripple Spell", "Obtained": False, "Mana": 500, "Cost": 4000},
    {"name": "Potion enhance", "Obtained": False, "Mana": 50, "Cost": 300},
    {"name": "Mana Trickery", "Obtained": False, "Mana": 0, "Cost": 2500},
    {"name": "Strong Arm", "Obtained": False, "Mana": 100, "Cost": 100},
]

enemy_templates = [
    {"name": "Goblin", "hp": 10, "dropgold": 5, "attack": 3, "luck": 1000, "confidence": 2.2, "dropxp": 15}, #"Goblin", 10, 5, 3, 1000, 2.2, 15
    {"name": "Golem", "hp": 40, "dropgold": 20, "attack": 5, "luck": 5, "confidence": 4, "dropxp": 50},
    {"name": "Skeleton", "hp": 15, "dropgold": 10, "attack": 5, "luck": 15, "confidence": 1.5, "dropxp": 10},
    {"name": "Dragon", "hp": 2500, "dropgold": 300000, "attack": 300, "luck": 65, "confidence": 9.4, "dropxp": 250000}
]


armours = [

    {"name": "Naked", "protection": 0, "luckproof": 40, "swordres": 0, "magicres": 0, "Obtained": True},
    {"name": "Raggy clothes", "protection": 5, "luckproof": 0, "swordres": 0, "magicres": 0, "Obtained": True},

]


player = {
    "name": "bob",

    #skills & stats

    "health": 100,
    "max_health": 100,
    "speed": 100,

    "swordskill": 0, #max 10
    "magicskill": 0, #max 10
    "damage": 1, #raw strength

    #general

    "gold": 0,
    "xp": 1500,


    #weapon

    "weapon": "Fists",
    "weapondamage": 2,
    "weaponluck": 60,
    "weapondurability": False,
    "magic": False,
    "ranged": False,

    #armour

    "armour": "Naked",
    "protection": 0,
    "luckproof": 40,
    "swordres": 0,
    "magicres": 0
}

    
misc ={
 
    "location": "x",
    "lastlocation": "x",
    "cavevisits": 0,
    "dojovisit": "no",
    "magicunlocked": False,
    "magicasked": False,
    "doorhandles": 0,

}