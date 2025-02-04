from fighter.fighter import Fighter
from fighter.fighter_controller import FighterController
from fighter.attack import Attack
from fighter.fighter_rounds import FightRounds

from player.player import Player

def run():
    controller = FighterController()

    fp_name = input("Digite o nome do primeiro jogador: ")    

    print("Selecione o lutador do primeiro jogador: ")

    print(controller.keys())

    fp_fighter = 
    
    fp = Player(fp_name)

    first_player_fighter = Fighter('Ryu', 200, [
        Attack('Bloqueio', damage=0, needed_stamina=5),
        Attack('Soco', damage=20, needed_stamina=20)
    ])
    first_player.add_fighter(ryu)

    second_player = Player('Cauã')
    ken = Fighter('Ken', 200, [
        Attack('Bloqueio', damage=0, needed_stamina=3),
        Attack('Soco', damage=30, needed_stamina=10)
    ])
    second_player.add_fighter(ken)

    game = FightRounds(first_player, second_player)
    game.start_round()

if __name__ == "__main__":
    run()