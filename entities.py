from entityClass import Entity
from weapons import *
import copy

Thorkin = Entity(
    name = "Thorkin",
    race = "Dvergr",
    level = 1,
    role = "Warrior",
    health = { "Temp HP": 0, "Current HP": 1, "Max HP": 40},
    armor = 10,
    initiative = 3,
    stats = {
        "Styrkr" : 18,
        "Fimr" : 16,
        "Megin" : 0,
        "Fjölkyngr" : 0,
        "Seiðr" : 0,
        "Galdr" : 0 
    },
    equipment = {
        "Main Hand" : copy.deepcopy(bronzeSpear),
        "Off-Hand" : copy.deepcopy(shield),
        "Head" : None,
        "Body" : None,
        "Legs" : None,
        "Hands" : None,
        "Feet" : None,
        "Rings" : [],
        "Necklace" : None
    },
    inventory = [],
    conditions = {},     # "Poison" : [False]   
    action_dict = {
        "Number of Actions" : 3,
        "Attack Actions" : {
            'Main Hand Attack': 1,
            'Off-Hand Attack': 1,
            'Grapple': 1,
            'Shove': 1,
        },
        "Magic Actions" : {
            'Cantrip' : 0,
            'Spell 1' : 0,
            'Spell 2' : 0,
            'Spell 3' : 0
        },
        "Move": 0,
        "Use Item" : {
            'Health Potion' : 0,
            'Mana Potion' : 0
        }
    },
    spell_dict = {
        "Cantrip" : None,
        "Spell 1" : None,
        "Spell 2" : None,
        "Spell 3" : None
    }

)

Balkor = Entity(
    name = "Balkor",
    race = "Draugr",
    level = 1,
    role = "Warrior",
    health = { "Temp HP": 0, "Current HP": 1, "Max HP": 30},
    armor = 14,
    initiative = 3,
    stats = {
        "Styrkr" : 16,
        "Fimr" : 0,
        "Megin" : 0,
        "Fjölkyngr" : 0,
        "Seiðr" : 0,
        "Galdr" : 0 
    },
    equipment = {
        "Main Hand" : copy.deepcopy(bronzeAxe),
        "Off-Hand" : copy.deepcopy(shield),
        "Head" : None,
        "Body" : None,
        "Legs" : None,
        "Hands" : None,
        "Feet" : None,
        "Rings" : [],
        "Necklace" : None
    },
    inventory = [],
    conditions = {},     # "Poison" : [False]     
    action_dict = {
        "Number of Actions" : 3,
        "Attack Actions" : {
            'Main Hand Attack': 1,
            'Off-Hand Attack': 1,
            'Grapple': 1,
            'Shove': 1,
        },
        "Magic Actions" : {
            'Cantrip' : 0,
            'Spell 1' : 0,
            'Spell 2' : 0,
            'Spell 3' : 0
        },
        "Move": 0,
        "Use Item" : {
            'Health Potion' : 0,
            'Mana Potion' : 0
        }
    },
    spell_dict = {
        "Cantrip" : None,
        "Spell 1" : None,
        "Spell 2" : None,
        "Spell 3" : None
    }
)

