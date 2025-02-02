import yaml

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
            for fighter in data.items():
                self.fighters.append(fighter)

#controller = FighterController()
#print(controller.fighters)