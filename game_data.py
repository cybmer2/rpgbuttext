import random
import time
import os


inventory = {
    "bandaid": 0,
    "l1healpot": 0,
    "arrow": 0,

}



weapons = [
    {"name": "Fists", "Luck": 60, "Damage": 2, "Durability": False, "Obtained": True, "Ranged": False, "Magic": False},
    {"name": "Iron sword", "Luck": 25, "Damage": 6, "Durability": 25, "Obtained": True, "Ranged": False, "Magic": False},
    {"name": "Bow", "Luck": 60, "Damage": 20, "Durability": 80, "Obtained": True, "Ranged": True, "Magic": False},
    {"name": "Katana", "Luck": 40, "Damage": 30, "Durability": 400, "Obtained": False, "Ranged": False, "Magic": False},
    {"name": "Firestaff", "Luck": 0, "Damage": 30, "Durability": 400, "Obtained": False, "Ranged": False, "Magic": True},
]





enemy_templates = [
    {"name": "Goblin", "hp": 10, "dropgold": 5, "attack": 3, "luck": 1000, "confidence": 2.2, "dropxp": 15},
    {"name": "Golem", "hp": 40, "dropgold": 20, "attack": 5, "luck": 5, "confidence": 4, "dropxp": 50},
    {"name": "Skeleton", "hp": 15, "dropgold": 10, "attack": 5, "luck": 15, "confidence": 1.5, "dropxp": 10},
    {"name": "Dragon", "hp": 2500, "dropgold": 300000, "attack": 300, "luck": 65, "confidence": 9.4, "dropxp": 250000}
]


armours = [

    {"name": "naked", "protection": 0, "fireres": 0, "luckproof": 100, "slashres": 0, "magicres": 0,}
    {"name": "raggy", "protection", 5, "fireres:" -20, "luckproof": 0, "slashres": 0, "magicres": 0,}

]


player = {
    "name": "bob",

    #basic stats

    "health": 100,
    "max_health": 100,
    "damage": 1,
    "speed": 100,

    #general

    "gold": 0,
    "potions": 0,
    "xp": 0,


    #weapon

    "weapon": "Fists",
    "weapondamage": 2,
    "weaponluck": 60,
    "weapondurability": False,
    "magic": False,
    "speed": 100,
    "ranged": False,

    #armour

    "armour": "naked",
    "protection": 0,
    
}

misc = {

    "location": "x",
    "lastlocation": "x",


}