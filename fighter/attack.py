class Attack:
    def __init__(self, name, damage, needed_stamina, accuracy):
        self.__name = name
        self.__damage = damage
        self.__needed_stamina = needed_stamina
        self.__accuracy = accuracy


    # Property para acessar os métodos privados de maneira mais correta e protegida
    @property
    def name(self):
        return self.__name

    @property
    def damage(self):
        return self.__damage

    @property
    def needed_stamina(self):
        return self.__needed_stamina

    # Método set para o needed_stamina caso seja necessária alguma modificação
    @needed_stamina.setter
    def needed_stamina(self, value):
        if value < 0:
            raise ValueError("Stamina cost cannot be negative")
        self.__needed_stamina = value

    @property
    def accuracy(self):
        return self.__accuracy

    def __repr__(self):
        return f"Attack(name={self.name}, damage={self.damage}, stamina={self.needed_stamina}, accuracy={self.accuracy}%)"
