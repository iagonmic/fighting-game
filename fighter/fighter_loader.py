import yaml
from fighter.fighter import Fighter, Attack

class FighterLoader:
    def load_fighters(self, file_path: str) -> list[Fighter]:
        fighters = []
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)

                for c_name, c_atts in data.items():
                    fighter = Fighter(c_name, c_atts['max_health'], attacks=[])
                    for key, value in c_atts['attacks'].items():
                        attack = Attack(
                            name=key,
                            damage=value['damage'],
                            needed_stamina=value['stamina'],
                            accuracy=value['accuracy'] * 100
                        )
                        fighter.add_attack(attack)
                    fighters.append(fighter)
        except Exception as e:
            print(f"Erro ao carregar lutadores: {e}")
        return fighters