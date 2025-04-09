from fighter.fighter import Fighter
from abc import ABC, abstractmethod

class IPlayer(ABC): ## Implementando a interface para a terceira unidade, deixando a classe Player mais limpa e fácil de entender
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @abstractmethod
    def has_stamina(self, stamina: int) -> bool:
        pass

    @abstractmethod
    def consume_stamina(self, stamina: int):
        pass

    @abstractmethod
    def add_fighter(self, fighter):
        pass

class Player(IPlayer):
    def __init__(self, name: str):
        self.__name = name
        self.__stamina = 30
        self.__active_fighter: Fighter = None ### Composição
        self.__fighters = []

    @property
    def name(self):
        return self.__name

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        """Define a stamina do jogador garantindo que não seja menor que 0 nem maior que 30."""
        if not isinstance(value, (int, float)):
            raise ValueError("A stamina deve ser um número.")
        self.__stamina = max(0, min(30, value))

    @property
    def active_fighter(self):
        return self.__active_fighter

    @active_fighter.setter
    def active_fighter(self, fighter: Fighter):
        """Define o lutador ativo, garantindo que seja uma instância de Fighter."""
        if not isinstance(fighter, Fighter):
            raise TypeError("O lutador ativo deve ser uma instância de Fighter.")
        self.__active_fighter = fighter

    @property
    def fighters(self):
        return self.__fighters

    def has_stamina(self, stamina: int):
        """Verifica se o jogador tem stamina suficiente para um ataque."""
        if not isinstance(stamina, (int, float)) or stamina < 0:
            raise ValueError("A stamina necessária deve ser um número positivo.")
        return self.__stamina >= stamina

    def consume_stamina(self, stamina: int):
        """Consome a stamina do jogador se ele tiver o suficiente."""
        try:
            if not self.has_stamina(stamina):
                raise ValueError("Stamina insuficiente para essa ação.")
            self.stamina -= stamina
        except ValueError as e:
            print(f"Erro: {e}")

    def get_active_fighter(self):
        """Retorna o lutador ativo do jogador."""
        return self.__active_fighter

    def add_fighter(self, fighter: Fighter):
        """Adiciona um lutador ao jogador e define como ativo se for o primeiro."""
        try:
            if not isinstance(fighter, Fighter):
                raise TypeError("O objeto deve ser uma instância de Fighter.")
            if fighter not in self.__fighters:
                self.__fighters.append(fighter)
                if self.__active_fighter is None:
                    self.__active_fighter = fighter
        except TypeError as e:
            print(f"Erro ao adicionar lutador: {e}")

    def __repr__(self):
        return f"Jogador: {self.__name}, Stamina: {self.__stamina}, Lutadores: {[f.name for f in self.__fighters]}"
