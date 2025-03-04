from entityClass import Entity
from diceRoll import diceRoll
from weaponClass import Weapon
from battleClass import Battle

entities_in_initiative = []
entity_order = []
in_initiative = False

def main():
    entity1 = Entity(name = "Thorkin",
                     race = "Dvergr",
                     level = 1,
                     role = "Warrior",
                     health = { "Temp HP": 12, "Current HP": 40, "Max HP": 40},
                     armor = 16,
                     initiative = 3,
                     stats = {"Styrkr" : 18,
                              "Fimr" : 0,
                              "Megin" : 0,
                              "Fjölkyngr" : 0,
                              "Seiðr" : 0,
                              "Galdr" : 0 
                              }
                    )
    entity2 = Entity(name = "Balkor",
                     race = "Draugr",
                     level = 1,
                     role = "Warrior",
                     health = { "Temp HP": 0, "Current HP": 30, "Max HP": 30},
                     armor = 14,
                     initiative = 2
                    )
    print(entity1)
    print(entity2)

    axe = Weapon(dice = (2,6),
                 stat = "Styrkr")
    
    entity1.equipment["Main Hand"] = axe
    entity2.equipment["Main Hand"] = axe

    print(entity1)

    Battle(entities_in_initiative=[entity1,entity2])

    #entity1.weapon_attack(axe,True,False,entity2)




if __name__ == "__main__":
    main()