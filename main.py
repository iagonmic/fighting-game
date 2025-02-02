from fighter.fighter import Fighter
from fighter.fighter_controller import FighterController
from fighter.attack import Attack

from player.player import Player

def run():
    controller = FighterController()

    fp_name = input("Digite o nome do primeiro jogador: ")    

    print("Selecione o lutador do primeiro jogador: ")

    fp_fighter = 
    
    fp = Player(fp_name)
    
    print(controller.keys())
    first_player_fighter = input("Selecione o seu pr")

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

    print(ken.get_health())

    soco_ryu = ryu.get_attack(1)
    ryu.attack(first_player, second_player, soco_ryu)

    print(ken.get_health())

def select_fighter(controller: FighterController):
    print("Os lutadores disponíveis são:")

    for i, fighter in enumerate(controller.fighters):
        print(f"{i}: {fighter}")

if __name__ == "__main__":
    run()