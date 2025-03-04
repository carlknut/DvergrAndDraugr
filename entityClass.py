class Entity():
    
    health_dict = {  
                "Temp HP" : 0,
                "Current HP" : 0,
                "Max HP" : 0           
    }
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

    def __init__( self, 
            name = "",
            type = None,                    # can be creature, race, etc.
            level = int(),
            role = None,
            health = health_dict,
            armor = int(), 
            speed = int(), 
            initiative = int(), 
            stats = stats_dict, 
            equipment = equipment_dict,
            inventory = inventory_list
    ):
        self.name = name
        self.type = type
        self.level = level
        self.role = role
        self.health = health
        self.armor = armor
        self.speed = speed
        self.initiative = initiative
        self.stats = stats
        self.equipment = equipment
        self.inventory = inventory

    def __str__(self):
        name_type_str = f"\n{self.name} the {self.type}:\n"
        role_level_str = f"Level {self.level} {self.role}\n"
        health_str = f"Temp HP: {self.health["Temp HP"]} | Current HP: {self.health["Current HP"]} | Max HP: {self.health["Max HP"]}\n"
        armor_speed_initiative_str = f"Armor: {self.armor} | Speed {self.speed} | Initiative: {self.initiative}\n"
        stats_str = f"Stats:\n    Styrkr: {self.stats["Styrkr"]}\n    Fimr: {self.stats["Fimr"]}\n    Megin: {self.stats["Megin"]}\n    Fjölkyngr: {self.stats["Fjölkyngr"]}\n    Seiðr: {self.stats["Seiðr"]}\n    Galdr: {self.stats["Galdr"]}\n"
        
        equipment_str = "Equipment:\n"
        for slot in self.equipment:
            if slot == "Rings" and self.equipment[slot] == []:
                equipment_str += str( "    " + str(slot) + ": " + str(None) + "\n")
            else:
                equipment_str += str( "    " + str(slot) + ": " + str(self.equipment[slot]) + "\n")
        
        inventory_str = "Inventory:\n"
        if self.inventory == []:
            inventory_str += str( "    Empty\n")
        else:
            for item in self.inventory:
                inventory_str += str( "    " + str(item) + "\n")
        
        return name_type_str + role_level_str + health_str + armor_speed_initiative_str + stats_str + equipment_str + inventory_str