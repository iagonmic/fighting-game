import yaml
from fighter import Fighter, Attack

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

                fighter = Fighter(c_name, c_atts['max_health'])

                for key, value in c_atts['attacks'].items():
                    attack = Attack(key, damage=value['damage'], needed_stamina=value['stamina'])
                    # Fix attack appending issue on characters
                    """
                    [Nome do lutador: Ryu, vida: 200, ataques: [Soco, 20, 20, Bloqueio, 0, 5, Soco, 30, 10, Bloqueio, 0, 5], Nome do lutador: Ken, vida: 200, ataques: [Soco, 20, 20, Bloqueio, 0, 5, Soco, 30, 10, Bloqueio, 0, 5]]
                    """
                    fighter.add_attack(attack)

                if not fighter in self.fighters:
                    self.fighters.append(fighter)

controller = FighterController()
print(controller.fighters)