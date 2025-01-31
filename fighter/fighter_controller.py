class FighterController:

    def __init__(self):
        self.fighters = []
        self.load()

    def add_fighter(self, fighter):
        self.fighters.append(fighter)

    def get_fighters(self):
        return self.fighters

    def load():
        pass
