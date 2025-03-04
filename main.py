from entityClass import Entity
from diceRoll import diceRoll
from weaponClass import Weapon

def main():
    entity1 = Entity(name = "Thorkin",
                     race = "Dvergr",
                     level = 1,
                     role = "warrior",
                     health = { "Temp HP": 12, "Current HP": 40, "Max HP": 40},
                     armor = 16,
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
                    )
    print(entity1)

    axe = Weapon(dice = (2,6),
                 stat = "Styrkr")

    entity1.weapon_attack(axe,True,False,entity2)

if __name__ == "__main__":
    main()