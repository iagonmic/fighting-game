from fighter.attack import Attack

import random

class Fighter:
    ### Tornando os atributos privados
    def __init__(self, name: str, max_health: int, attacks: list[Attack]):
        self.__name = name
        self.__max_health = max_health if max_health > 0 else 100  # Saúde mínima padrão
        self.__health = self.__max_health
        self.__attacks = attacks if isinstance(attacks, list) else []  # Garante que seja uma lista

    ### Usando property para proteger corretamente os métodos
    @property
    def name(self):
        return self.__name
    
    @property
    def max_health(self):
        return self.__max_health
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        if not isinstance(value, (int, float)):
            ###
            raise ValueError("O valor da saúde deve ser um número.")
        self.__health = max(0, min(self.__max_health, value))

    @property
    def attacks(self):
        return self.__attacks

    def get_health(self):
        return self.__health

    def damage(self, damage: int):
        try:
            if damage < 0:
                ###
                raise ValueError("O dano não pode ser negativo.")
            self.health -= damage
            ###
        except ValueError as e:
            print(f"Erro ao aplicar dano: {e}")


    def is_dead(self):
        return self.__health <= 0

    def get_attack(self, index: int):
        try:
            if not isinstance(index, int):
                ###
                raise ValueError("O índice deve ser um número inteiro.")
            return self.__attacks[index] if 0 <= index < len(self.__attacks) else None
        ### 
        except IndexError:
            print("Erro: O índice do ataque está fora dos limites.")
            return None
        ###
        except ValueError as e:
            print(f"Erro: {e}")
            return None
    
    def attack(self, actor, enemy, attack: Attack) -> bool:
        """Executa o ataque no inimigo, considerando precisão e consumo de stamina."""
        try:
            if attack not in self.__attacks:
                raise ValueError("O ataque não pertence a este lutador.")

            stamina_needed = attack.needed_stamina
            if not actor.has_stamina(stamina_needed):
                print("Stamina insuficiente para este ataque.")
                return False

            if random.randint(0, 100) > attack.accuracy:
                print("O oponente esquivou do ataque!")
                return False

            actor.consume_stamina(stamina_needed)

            enemy_fighter = enemy.get_active_fighter()
            enemy_fighter.damage(attack.damage)

            return enemy_fighter.is_dead()

        ###
        except AttributeError as e:
            print(f"Erro ao executar ataque: {e}")
            return False
        except ValueError as e:
            print(f"Erro: {e}")
            return False
    
    def add_attack(self, attack: Attack):
        try:
            if not isinstance(attack, Attack):
                raise TypeError("O ataque deve ser uma instância de Attack.")
            
            if attack not in self.__attacks:
                self.__attacks.append(attack)
        ###
        except TypeError as e:
            print(f"Erro ao adicionar ataque: {e}")

    def __repr__(self):
        return f'Lutador: {self.__name}, Vida: {self.__health}, Ataques: {self.__attacks}'