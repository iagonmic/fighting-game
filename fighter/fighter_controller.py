import yaml
from fighter.fighter import Fighter, Attack

class FighterController:

    def __init__(self):
        self.__fighters = [] # Tornamos o método privado, impedindo de ser modificado diretamente
        self.load()

    @property
    def fighters(self):
        return list(self.__fighters) # Decorador para poder acessar de maneira segura o atributo fighters

    def add_fighter(self, fighter):
        if fighter not in self.__fighters:
            self.__fighters.append(fighter)

    def get_fighters(self):
        return self.__fighters

    def load(self):
        try:
            with open('fighters.yml', 'r') as f:
                data = yaml.safe_load(f)

                if not isinstance(data, dict):
                    raise ValueError("Invalid data format in YAML file") # Aqui elevamos um erro caso o YAML não seja lido corretamente

                for c_name, c_atts in data.items():
                    try:
                        fighter = Fighter(c_name, c_atts['max_health'], attacks = [])

                        for key, value in c_atts['attacks'].items():
                            attack = Attack(
                                name=key, 
                                damage=value['damage'], 
                                needed_stamina=value['stamina'],
                                accuracy=value['accuracy'] * 100
                            )
                            fighter.add_attack(attack)

                        self.add_fighter(fighter)

                    # Tratamento para erros sobre o nome ou atributo dos personagens
                    except (KeyError, TypeError) as e:
                        print(f"Skipping fighter {c_name} due to missing or invalid attributes: {e}")

        # Tratamento para caso o arquivo não seja encontrado
        except FileNotFoundError:
            print("fighters.yml file not found. No fighters loaded.")

        # Tratamento para leitura do arquivo YAML
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")

        # Tratamento para qualquer outro tipo de erro
        except Exception as e:
            print(f"Unexpected error loading fighters: {e}")
    
        
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
        
