from abc import ABC, abstractmethod
from fighter.fighter_loader import FighterLoader

class IFighterController(ABC): ## Interface para o controlador de lutadores, permitindo a implementação de diferentes controladores
    @property
    @abstractmethod
    def fighters(self):
        pass

    @abstractmethod
    def add_fighter(self, fighter):
        pass

    @abstractmethod
    def remove_fighter(self, fighter_name: str):
        pass

    @abstractmethod
    def load(self):
        pass

class FighterController(IFighterController):

    def __init__(self):
        self.__fighters = [] # Tornamos o método privado, impedindo de ser modificado diretamente
        self.__loader = FighterLoader()
        self.load()

    @property
    def fighters(self):
        return list(self.__fighters) # Decorador para poder acessar de maneira segura o atributo fighters

    def add_fighter(self, fighter):
        if fighter not in self.__fighters:
            self.__fighters.append(fighter)

    def load(self):
        self.__fighters = self.__loader.load_fighters('fighters.yml')
    
        
    def remove_fighter(self, fighter_name):
        try:
            for i, fighter in enumerate(self.__fighters):
                if fighter.name == fighter_name:
                    del self.fighters[i]
                    return True
            # Caso o lutador não seja encontrado
            raise ValueError(f"Fighter '{fighter_name}' not found")
        
        # Outros tipos de erros
        except ValueError as e:
            print(e)
            return False

