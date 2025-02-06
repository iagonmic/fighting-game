class Attack:

    def __init__(self, name, damage, needed_stamina, accuracy):
        self.name = name
        self.damage = damage
        self.needed_stamina = needed_stamina
        self.accuracy = accuracy
    
    def get_damage(self):
        return self.damage
    
    def get_needed_stamina(self):
        return self.needed_stamina
    
    def get_accuracy(self):
        return self.accuracy
    
    def __repr__(self):
        return f"Nome do ataque: {self.name}, dano: {self.damage}, stamina: {self.needed_stamina}"
