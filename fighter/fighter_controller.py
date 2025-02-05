import yaml
from fighter.fighter import Fighter, Attack

class FighterController:

    def __init__(self):
        self.fighters = []
        self.load()

    def add_fighter(self, fighter):
        self.fighters.append(fighter)

    def get_fighters(self):
        return self.fighters

    def load(self):
        with open('fighters.yml', 'r') as f:
            data = yaml.safe_load(f)
            for character in data.items():
                c_name = character[0]
                c_atts = character[1]

                fighter = Fighter(c_name, c_atts['max_health'], attacks = [])

                for key, value in c_atts['attacks'].items():
                    attack = Attack(key, damage=value['damage'], needed_stamina=value['stamina'])
                    fighter.add_attack(attack)

                if not fighter in self.fighters:
                    self.fighters.append(fighter)
    
    def remove_fighter(self, fighter_name):
        for i, fighter in enumerate(self.fighters):
            if fighter.name == fighter_name:
                print('feito')
                del self.fighters[i]
                return True
        return False

#controller = FighterController()
#print(controller.fighters)