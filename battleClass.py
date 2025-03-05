from diceRoll import diceRoll
from entityClass import Entity
from weaponClass import Weapon

class Battle():
    def __init__(self,
                 entities_in_initiative = [],
                 entity_order = [],
                 in_initiative = False
                 ):
        self.entities_in_initiative = entities_in_initiative
        self.entity_order = entity_order
        self.in_initiative = in_initiative

        self.begin_battle()

    def begin_battle (self):
        self.roll_initiative()
        self.initiative() 

    def roll_initiative(self):
        initiative_rolls = []
        for entity in self.entities_in_initiative:
            initiative_roll = entity.initiative + diceRoll(1,20)
            print(initiative_roll)
            initiative_rolls.append( (entity, initiative_roll) )
        initiative_rolls.sort(reverse = True, key = lambda x: x[1])
        print(initiative_rolls)
        self.entity_order = []
        for entity in initiative_rolls:
            self.entity_order.append(entity[0])
        self.in_initiative = True
        
    def initiative(self):
        while self.in_initiative:
            for entity in self.entity_order:
                self.turn(entity)
                for other_entity in self.entity_order:
                    if other_entity.get_health() == 0:
                        self.entity_order.pop(other_entity)
                        if len(self.entity_order) < 2:                      #temporary for one on one battles
                            in_initiative = False     

    def turn(self,entity):      
        print("\n" + entity.name + "'s turn:")
        
        temp_actions = entity.actions
        for number in range(len(entity.actions)):
            n = 1
            action_choice_range = [str(n)]
            # Printing Action options:
            for action in temp_actions: 
                print(f"    {n}: {action}")
                n += 1
                action_choice_range.append(str(n))
            print(f"    {n}: Pass Turn\n")
            
            # Request inout until option chosen:
            action_choice = input("Choose Action: ")
            while action_choice not in action_choice_range:
                print(f"Select 1 - {len(temp_actions)+1}!")
                action_choice = input("Choose Action: ")
                
            action_choice = int(action_choice) - 1         # sets to index value
            
            # exits turn function if chose pass turn
            if action_choice == ( len(temp_actions) + 2 ):
                print(f"{entity.name} passed turn!")
                return

            if action_choice == ( temp_actions.index("Main Hand") or temp_actions.index("Off-Hand") ):
                action = temp_actions[action_choice]
                if entity.equipment[str(action)] != ( None or "Shield" ) :
                    target_name = input("Choose Target: ")
                    for entity in self.entity_order:
                        if entity.name == target_name:
                            target = entity
                    entity.weapon_attack(
                                         entity.advantage_disadvantage[0],
                                         entity.advantage_disadvantage[1],
                                         target,
                                         entity.equipment[str(action)]
                                        )
