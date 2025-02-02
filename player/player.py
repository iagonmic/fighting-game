from fighter.fighter import Fighter

class Player:

    def __init__(self, name: str):
        self.name = name
        self.stamina = 30
        self.active_fighter: Fighter = None
        self.fighters = []

    def has_stamina(self, stamina):
        return self.stamina >= stamina

    def get_stamina(self):
        return self.stamina
    
    def consume_stamina(self, stamina):
        self.stamina = max(0, self.stamina - stamina)
    
    def get_active_fighter(self):
        return self.active_fighter

    def add_fighter(self, fighter: Fighter):

        if self.active_fighter is None:
            self.active_fighter = fighter

        self.fighters.append(fighter)
