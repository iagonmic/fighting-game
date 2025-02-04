from fighter.fighter import Fighter
from fighter.fighter_controller import FighterController
from fighter.attack import Attack
from fighter.fighter_rounds import FightRounds

from player.player import Player

def run():
    controller = FighterController()

    first_player_name = input("Digite o nome do primeiro jogador: ")
    second_player_name = input("Digite o nome do segundo jogador: ")    
    
    first_player = Player(first_player_name)
    second_player = Player(second_player_name)

    select_fighter(controller, first_player)
    select_fighter(controller, second_player)

    game = FightRounds(first_player, second_player)
    game.start_round()


def select_fighter(controller:FighterController, player:Player):
    temp_dict = {i: fighter for i, fighter in enumerate(controller.fighters)}

    print("Lutadores disponíveis: ")
    print("-"*60)

    for i, fighter in temp_dict.items():
        print(f"Lutador {i + 1}: {fighter.name}")

    print("-"*60)

    selected_fighter_index = int(input(f"Selecione o lutador do jogador {player.name} (digite o número ao lado dele): "))

    selected_fighter = temp_dict[selected_fighter_index - 1]

    player.add_fighter(selected_fighter)
    controller.remove_fighter(selected_fighter)

    return selected_fighter

if __name__ == "__main__":
    run()