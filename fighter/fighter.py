from .attack import Attack

class Fighter:

    def __init__(self, name: str, max_health: int, attacks: list[Attack]):
        self.name = name
        self.health = max_health
        self.max_health = max_health
        self.attacks = attacks

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = max(0, min(self.max_health, health))

    def damage(self, damage):
        self.set_health(self.get_health() - damage)

    def is_dead(self):
        return self.health <= 0

    def get_attack(self, index):
        if len(self.attacks) == 0 or index >= len(self.attacks):
            return None

        return self.attacks[index]
    
    def attack(self, actor, enemy, attack: Attack) -> bool:
        if not attack in self.attacks:
            return False
        
        stamina = attack.get_needed_stamina()
        if not actor.has_stamina(stamina):
            return False

        actor.consume_stamina(stamina)
        damage = attack.damage

        enemy_fighter = enemy.get_active_fighter()
        enemy_fighter.damage(damage)

        return enemy_fighter.is_dead()
    
    def add_attack(self, attack: Attack):
        if not attack in self.attacks:
            self.attacks.append(attack)

    def __repr__(self):
        return f'Nome do lutador: {self.name}, vida: {self.health}, ataques: {self.attacks}'