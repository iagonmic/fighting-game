class Move:
    """Superclasse genérica para qualquer tipo de movimento no jogo (ataques, magias, defesas)."""
    def __init__(self, name: str, damage: int, accuracy: float):
        self.__name = name
        self.__damage = damage
        self.__accuracy = accuracy

    @property
    def name(self):
        return self.__name

    @property
    def damage(self):
        return self.__damage

    @property
    def accuracy(self):
        return self.__accuracy

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__name} (Dano: {self.__damage}, Precisão: {self.__accuracy}%)"

    
class Attack(Move):  ### Herança e Polimorfismo -> Attack herda de move
    def __init__(self, name: str, damage: int, needed_stamina: int, accuracy: float):
        super().__init__(name, damage, accuracy)  # Chama o construtor da superclasse
        self.__needed_stamina = needed_stamina

    @property
    def needed_stamina(self):
        return self.__needed_stamina

    def __add__(self, other): ### Sobrecarga de operadores -> Soma de dois ataques através do dano causado
        if isinstance(other, Attack):
            new_damage = self.damage + other.damage
            new_stamina = max(self.needed_stamina, other.needed_stamina)  ### Usa a maior stamina necessária
            new_accuracy = (self.accuracy + other.accuracy) / 2  ### Média de precisão
            return Attack(f"{self.name} + {other.name}", new_damage, new_stamina, new_accuracy)
        return NotImplemented

    def __repr__(self):
        return f"Ataque: {self.name} (Dano: {self.damage}, Stamina: {self.needed_stamina}, Precisão: {self.accuracy}%)"

class Magic(Move):
    def __init__(self, name: str, damage: int, mana_cost: int, accuracy: float):
        super().__init__(name, damage, accuracy)
        self.__mana_cost = mana_cost

    @property
    def mana_cost(self):
        return self.__mana_cost

    def __repr__(self):
        return f"Magia: {self.name} (Dano: {self.damage}, Mana: {self.mana_cost}, Precisão: {self.accuracy}%)"

