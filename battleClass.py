from diceRoll import diceRoll
from entityClass import Entity
from weaponClass import Weapon
import copy
from random import randint

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

    def dice_roll_for_initiative(self,entity,number,d):
        roll = 0
        for die in range(number):
            roll += randint(1,d)
        print(f"{entity.name} rolled {number}d{d} for {roll}")
        return roll


    def roll_initiative(self):
        
        initiative_rolls = []
        for entity in self.entities_in_initiative:
            initiative_roll = entity.initiative + self.dice_roll_for_initiative(entity,1,20)
            input(f"...and got a {initiative_roll} for initiative.")
            
            initiative_rolls.append( (entity, initiative_roll, entity.initiative, entity.stats["Fimr"] ) )
        
        initiative_rolls.sort(reverse = True, key = lambda x: (x[1], x[2], x[3]) )     # sort list first by initiative roll, then by base initiative, then by "Fimir" stat
        #print(initiative_rolls)
        self.entity_order = []
        for entity in initiative_rolls:
            self.entity_order.append(entity[0])
        initiative_string = '\nInitiative order: '
        for entity in self.entity_order:
            initiative_string += f"| {entity.name} |"
        input(initiative_string)
        self.in_initiative = True
        
    def initiative(self):
        while self.in_initiative:
            for entity in self.entity_order:
                self.turn(entity)
                if self.initiative == False:
                    break
                
    def check_dead(self):
        for entity in self.entity_order:
            if entity.get_health() == 0:
                self.entity_order.remove(entity)
        if len(self.entity_order) < 2:                      #temporary for one on one battles
            self.in_initiative = False
            input("Battle DONE!")   

    def turn(self, entity):
        actions_list = ['Main Hand', 'Off-Hand', 'Grapple', 'Shove', 'Cantrip', 'Spell 1','Spell 2','Spell 3','Move','Health Potion','Mana Potion']
        temp_choice_list = [1,2,3,4,5,6,7,8,9,10,11,12]

        if entity.equipment['Off-Hand'] == None:       # removes off-hand from lists if 2-handed weapon
            actions_list.remove('Off-Hand')
            temp_choice_list.remove(2)

        temp_action_dict = copy.deepcopy(entity.action_dict)
        
        turn_bool = True
        while turn_bool:                
            
            self.print_turn_menu(temp_action_dict,entity)

            choice = input("Choose Action: ")

            if choice.isnumeric() and int(choice) in temp_choice_list:
                choice = int(choice)

                # Main Hand and Off-Hand Attack
                if choice in [1,2]:
                    action_index = temp_choice_list.index(choice)
                    temp_action_dict["Number of Actions"] -= 1

                    temp_bool = True
                    while temp_bool:
                        target_list = [ entity.name for entity in self.entity_order ]
                        target_list.remove(entity.name)
                        print(f"\nTargets: {target_list}")
                        target_name = input("Choose target: ")
                        if target_name in target_list:
                            temp_bool = False
                            for other_entity in self.entity_order:
                                if other_entity.name == target_name:
                                    target = other_entity
                            entity.weapon_attack(
                                target,
                                entity.equipment[actions_list[action_index]],
                                entity.advantage_disadvantage[0],
                                entity.advantage_disadvantage[1]                                    
                            )
                            input("\nEnter to continue...")
                        else:
                            input("Choose a valid target...Enter to contiue...")

                    if choice == 1:
                        temp_action_dict["Attack Actions"]['Main Hand Attack'] -= 1
                        if temp_action_dict["Attack Actions"]['Main Hand Attack'] == 0:
                            actions_list.remove('Main Hand')
                            temp_choice_list.remove(1)
                    if choice == 2:
                        temp_action_dict["Attack Actions"]['Off-Hand Attack'] -= 1
                        if temp_action_dict["Attack Actions"]['Off-Hand Attack'] == 0:
                            actions_list.remove('Off-Hand')
                            temp_choice_list.remove(2)
                
                if choice in [3,4]:
                    pass
                
                if choice == 12:
                    input(f"\n{entity.name} passes their turn.")
                    turn_bool = False

            elif choice.isnumeric() and int(choice) not in temp_choice_list:
                print(f"Choices: {temp_choice_list}")
                input("Any key to continue...")
            else:
                input("Please choose a valid number...Any key to continue...")

            self.check_dead()               
            if self.in_initiative == False:          # breaks turn loop if all dead
                turn_bool = False



    def print_turn_menu(self, temp_action_dict, entity):
        if entity.equipment['Off-Hand'] != None:
            off_hand_str = f": ({temp_action_dict["Attack Actions"]['Off-Hand Attack']}/{entity.action_dict["Attack Actions"]['Off-Hand Attack']}): {entity.equipment['Off-Hand'].name}"
        else:
            off_hand_str = ":"


        print("\n" + entity.name + "'s turn:")
        print(f"  Number of Actions: ({temp_action_dict["Number of Actions"]}/{entity.action_dict['Number of Actions']})")
        print(f"    Attack Action:")
        print(f"        1. Main Hand ({temp_action_dict["Attack Actions"]['Main Hand Attack']}/{entity.action_dict["Attack Actions"]['Main Hand Attack']}): {entity.equipment['Main Hand'].name}")
        print(f"        2. Off-Hand{off_hand_str}")
        print(f"        3. Grapple")
        print(f"        4. Shove")
        print(f"    Magic Action:")
        print(f"        5. Cantrip: {temp_action_dict['Magic Actions']['Cantrip']}")
        print(f"        6. Spell 1: {temp_action_dict['Magic Actions']['Spell 1']}")
        print(f"        7. Spell 2: {temp_action_dict['Magic Actions']['Spell 2']}")
        print(f"        8. Spell 3: {temp_action_dict['Magic Actions']['Spell 3']}")
        print(f"    9. Move: {temp_action_dict['Move']}")
        print(f"    Use Item:")
        print(f"        10. Health Potion")
        print(f"        11. Mana Potion")
        print(f"    12. Pass Turn")
        

    def turn2(self,entity):      
        print("\n" + entity.name + "'s turn:")
        
        temp_actions = entity.actions
        for number in range(len(entity.actions)):
            
            # Printing Action options:
            n = 1
            action_choice_range = [str(n)]
            for action in temp_actions: 
                print(f"    {n}: {action}")
                n += 1
                action_choice_range.append(str(n))
            print(f"    {n}: Pass Turn\n")
            
            # Request input until option chosen:
            action_choice = input("Choose Action: ")
            while action_choice not in action_choice_range:
                print(f"Select 1 - {len(temp_actions)+1}!")
                action_choice = input("Choose Action: ")
                
            action_choice = int(action_choice) - 1         # sets to index value
            
            # exits turn function if chose pass turn
            if action_choice == ( len(temp_actions) + 2 ):
                print(f"{entity.name} passed turn!")
                return

            if action_choice == temp_actions.index("Main Hand") or action_choice == temp_actions.index("Off-Hand") :
                action = temp_actions[action_choice]
                temp_actions.pop(action_choice)
                if entity.equipment[action] != ( None or "Shield" ) :
                    target_name = input("Choose Target: ")
                    for other in self.entity_order:
                        if other.name == target_name:
                            target = other
                    #print(entity)
                    entity.weapon_attack(
                                         target,
                                         entity.equipment[action],
                                         entity.advantage_disadvantage[0],
                                         entity.advantage_disadvantage[1]                                    
                                        )
