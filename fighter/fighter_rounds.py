from fighter.fighter import Fighter
from fighter.attack import Attack
from player.player import Player

class FightRounds:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.rounds = 0
        
    def regen_stamina(self, player):
        regen_amount = 10  
        player.stamina = min(30, player.stamina + regen_amount)
        print(f"{player.name} regenerou {regen_amount} de stamina. Stamina atual: {player.stamina}")

    def start_round(self):
        while True:
            round_pair = self.rounds % 2 == 0

            current_player = self.player1 if round_pair else self.player2
            opponent = self.player2 if round_pair else self.player1

            print("-" * 60)
            print(f"{current_player.name}, é o seu turno")
            fighter = current_player.get_active_fighter()

            print("Escolha uma ação: ")
            for i, attack in enumerate(fighter.attacks):
                print(f"{i}: {attack.name} (Dano: {attack.damage}, Stamina: {attack.needed_stamina})")
        
            while True:
                try:
                    choice = int(input("Digite uma ação: "))
                    action = fighter.get_attack(choice)
                    if action and current_player.has_stamina(action.needed_stamina):
                        break
                    else:
                        print("Ataque não existe ou Stamina insuficiente.")
                except ValueError:
                    print("Entrada inválida, escolha novamente.")
            
            fighter.attack(current_player, opponent, action)

            opponent_fighter = opponent.get_active_fighter()
            print(f"{opponent_fighter.name} tem {opponent_fighter.health} de vida")

            if opponent.get_active_fighter().is_dead():
                print(f"{opponent.get_active_fighter().name} foi derrotado! {current_player.name} vence!")
                break
            
            self.regen_stamina(current_player)
            self.rounds += 1

    


