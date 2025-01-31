from fighter.fighter import Fighter
from fighter.fighter_controller import FighterController
from fighter.attack import Attack

from player.player import Player

def run():
    first_player = Player('Rafael')
    ryu = Fighter('Ryu', 200, [
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

if __name__ == "__main__":
    run()