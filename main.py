from entityClass import Entity
from diceRoll import diceRoll
from weaponClass import Weapon
from battleClass import Battle
from entities import *
from weapons import *

entities_in_initiative = []
entity_order = []
in_initiative = False

def main():
    
    entities_in_initiative=[Thorkin,Balkor]

    #print(Thorkin)
    Thorkin.unequip('Off-Hand')
    #print(Thorkin)

    Battle(entities_in_initiative)

if __name__ == "__main__":
    
    main()