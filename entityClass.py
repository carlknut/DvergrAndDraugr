from diceRoll import diceRoll

def stat_mod(stat):
    mod = (stat - 10) // 2
    print(mod)
    return mod

class Entity():
    
    health_dict = {  
        "Temp HP" : 0,
        "Current HP" : 0,
        "Max HP" : 0           
    }
    eitr_list = [ 0, 0 ]
    stats_dict = {
        "Styrkr" : 0,       # Strength
        "Fimr" : 0,         # Dexterity
        "Megin" : 0,        # Constitution
        "Fjölkyngr" : 0,    # Intelligence
        "Seiðr" : 0,        # Wisdom
        "Galdr" : 0         # Charisma
    }
    equipment_dict = {
        "Main Hand" : "Axe",
        "Off-Hand" : None,
        "Head" : None,
        "Body" : None,
        "Legs" : None,
        "Hands" : None,
        "Feet" : None,
        "Rings" : [],
        "Necklace" : None
    }
    inventory_list = []
    conditions_dict = {}     # "Poison" : [False]   

    def __init__( self, 
        name = "",
        race = None,                    # can be creature, race, etc.
        level = int(),
        role = None,
        health = health_dict,
        armor = int(), 
        speed = int(), 
        eitr = eitr_list,
        initiative = int(), 
        stats = stats_dict, 
        equipment = equipment_dict,
        inventory = inventory_list
    ):
        self.name = name
        self.race = race
        self.level = level
        self.role = role
        self.health = health
        self.armor = armor
        self.speed = speed
        self.initiative = initiative
        self.eitr = eitr
        self.stats = stats
        self.equipment = equipment
        self.inventory = inventory

    def weapon_attack(self,weapon,advantage,disadvantage,entity):
        
        if advantage == disadvantage:
            roll = diceRoll(1,20)
        elif advantage:
            roll = max(diceRoll(1,20),diceRoll(1,20))
        elif disadvantage:
            roll = min(diceRoll(1,20),diceRoll(1,20))

        if roll == 20:
            print("CRITICAL HIT!")
            damage = diceRoll(weapon.dice[0],weapon.dice[1]) + diceRoll(weapon.dice[0],weapon.dice[1]) + stat_mod(self.stats[weapon.stat])
            self.do_damage(damage,[entity])
        else:
            attack_roll = roll + stat_mod(self.stats[weapon.stat])
            if attack_roll >= entity.armor:
                damage = diceRoll(weapon.dice[0],weapon.dice[1]) + stat_mod(self.stats[weapon.stat])
                self.do_damage(damage,[entity])
            else:
                print("Attack doesn't hit!")

    def do_damage(self,damage,entities):
        for entity in entities:
            entity.take_damage(damage,self)

    def take_damage(self,damage,entity):
        print(f"{self.name} takes {damage} damage from {entity.name}")
        if self.health["Temp HP"] > 0:
            if self.health["Temp HP"] < damage:
                damage -= self.health["Temp HP"]
                self.health["Temp HP"] = 0
            else: 
                self.health["Temp HP"] -= damage
                damage = 0
        if self.health["Current HP"] - damage <= 0:
            self.health["Current HP"] = 0
            print(f"{self.name} has died")
        else:
            self.health["Current HP"] -= damage


    def __str__(self):
        name_race_str = f"\n{self.name} the {self.race}:\n"
        role_level_str = f"Level {self.level} {self.role}\n"
        health_str = f"Temp HP: {self.health["Temp HP"]} | Current HP: {self.health["Current HP"]} | Max HP: {self.health["Max HP"]}\n"
        armor_speed_initiative_str = f"Armor: {self.armor} | Speed {self.speed} | Initiative: {self.initiative}\n"
        stats_str = f"Stats:\n    Styrkr: {self.stats["Styrkr"]}\n    Fimr: {self.stats["Fimr"]}\n    Megin: {self.stats["Megin"]}\n    Fjölkyngr: {self.stats["Fjölkyngr"]}\n    Seiðr: {self.stats["Seiðr"]}\n    Galdr: {self.stats["Galdr"]}\n"
        eitr_str = f"Eitr: {self.eitr[0]} / {self.eitr[1]}\n"

        equipment_str = "Equipment:\n"
        for slot in self.equipment:
            if slot == "Rings" and self.equipment[slot] == []:
                equipment_str += str( "    " + str(slot) + ": " + str(None) + "\n")
            else:
                equipment_str += str( "    " + str(slot) + ": " + str(self.equipment[slot]) + "\n")
        
        inventory_str = "Inventory:\n"
        if self.inventory == []:
            inventory_str += "    Empty\n"
        else:
            for item in self.inventory:
                inventory_str += str( "    " + str(item) + "\n")
        
        return name_race_str + role_level_str + health_str + armor_speed_initiative_str + eitr_str + stats_str + equipment_str + inventory_str