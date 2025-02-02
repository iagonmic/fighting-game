class Attack:

    def __init__(self, name, damage, needed_stamina):
        self.name = name
        self.damage = damage
        self.needed_stamina = needed_stamina
    
    def get_damage(self):
        return self.damage
    
    def get_needed_stamina(self):
        return self.needed_stamina
