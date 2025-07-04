import random
import time
import os


inventory = {
    "bandaid": 0,
    "l1healpot": 2,
    "bow": 1,
    "ironsword": 1,
    "arrow": 15,

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


player = {
    "name": "bob",
    "health": 80,
    "max_health": 100,
    "damage": 1.5,
    "speed": 20,
    "gold": 250,
    "potions": 0,
    "weapon": "Iron Sword",
    "weapondamage": 6,
    "weaponluck": 25,
    "weapondurability": 25,
    "magic": False,
    "speed": 100,
    "ranged": False,
    "xp": 0,
    "armour": "naked",
    
}

misc = {

    "location": "Main Menu"



}