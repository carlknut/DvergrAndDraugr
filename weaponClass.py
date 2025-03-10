melee_types = ['sword','axe','spear','greataxe','fists']
bow_types = ['bow','longbow']

melee_rank = ['bronze','iron','bone steel','dvergr steel']
bow_rank = ['wood','refined wood','elven','yggwood']

class Weapon():
    def __init__(self,
                 name = str(),  # can be empty string
                 type = str(),  # must have a type. either melee, bow, or magical
                 dice = (0,0),  # must have a damage dice. for magical its just the blunt weapon damage i.e. not high
                 stat = str(),  # 
                 rank = 0,
                 range = 1,
                 attacks = 1,
                 hands = 1
                ):
        self.name = name
        self.type = type
        self.dice = dice
        self.stat = stat
        self.rank = rank
        self.range = range
        self.attacks = attacks
        self.hands = hands

        if name == '':
            if self.type in melee_types:
                self.name = str(melee_rank[self.rank]).capitalize() + ' ' + self.type.capitalize()
            elif self.type in bow_types:
                self.name = str( bow_rank[self.rank] + self.type )

    def upgrade_weapon(self):
        self.rank +=1
        if self.type in melee_types:
            new_name = str( melee_rank[self.rank]).capitalize() + ' ' + self.type.capitalize()
        if self.type in bow_types:
            new_name = str( bow_rank[self.rank] + self.type )
        self.set_name(new_name)

    def set_name(self, new_name):
        print(f"{self.name} renamed to {new_name}.")
        self.name = new_name