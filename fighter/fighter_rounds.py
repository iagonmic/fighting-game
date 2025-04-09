from player.player import IPlayer
from abc import ABC, abstractmethod

import sys
import os

class IFightRounds(ABC):
    @abstractmethod
    def start_round(self):
        pass

    @abstractmethod
    def regen_stamina(self, player):
        pass

    @abstractmethod
    def clear_screen(self):
        pass

class FightRounds(IFightRounds):

    def __init__(self, player1: IPlayer, player2: IPlayer): #
        self.__player1 = player1
        self.__player2 = player2
        self.__rounds = 0

    # Encapsulamento dos atributos certos via property
    @property
    def player1(self):
        return self.__player1

    @property
    def player2(self):
        return self.__player2

    @property
    def rounds(self):
        return self.__rounds
        
    ### Método de instância
    def regen_stamina(self, player):
        regen_amount = 10
        try:
            player.stamina = min(30, player.stamina + regen_amount)
            print(f"{player.name} regenerou {regen_amount} de stamina. Stamina atual: {player.stamina}")

        # Caso o jogador não tenha o atributo stamina 
        except AttributeError:
            print("Erro: o jogador não possui um atributo de stamina.")

    def clear_screen(self):
        try:
            if sys.platform == 'win32':
                os.system('cls')
            else:
                os.system('clear')
        ###
        except Exception as e:
            print(f"Erro ao limpar a tela: {e}")

    def start_round(self):
        while True:
            round_pair = self.__rounds % 2 == 0

            current_player = self.__player1 if round_pair else self.__player2
            opponent = self.__player2 if round_pair else self.__player1

            print("-" * 60)
            print(f"{current_player.name}, é o seu turno")

            try:
                fighter = current_player.get_active_fighter()
                if fighter is None:
                    # Tratamento de erro em relação a não encontrar lutador ativo nem jogador
                    raise ValueError("Erro: Nenhum lutador ativo encontrado")
            ###
            except AttributeError:
                print("Erro: o jogador não possui um lutador ativo")
                break

            print("Escolha uma ação: ")
            for i, attack in enumerate(fighter.attacks):
                print(f"{i}: {attack.name} (Dano: {attack.damage}, Stamina: {attack.needed_stamina})")
        
            while True:
                try:
                    choice = int(input("Digite uma ação: "))
                    if 0 <= choice < len(fighter.attacks):  # Verifica se está no intervalo correto
                        action = fighter.get_attack(choice)
                        if action and current_player.has_stamina(action.needed_stamina):
                            break  # Se o ataque for válido, sai do loop
                        else:
                            print("Stamina insuficiente para este ataque.")
                    else:
                        print("Escolha inválida, selecione um número da lista.")
                ###
                except ValueError:
                    print("Entrada inválida, por favor digite um número.")
            
            ###
            try:
                fighter.attack(current_player, opponent, action)
            except Exception as e:
                print(f"Erro ao executar o ataque: {e}")
                continue  # Pula para a próxima iteração caso o ataque falhe

            opponent_fighter = opponent.get_active_fighter()
            self.clear_screen()
            print(f"{opponent_fighter.name} tem {opponent_fighter.health} de vida")
            if opponent_fighter.is_dead():
                print(f"{opponent_fighter.name} foi derrotado! {current_player.name} vence!")
                break
            
            self.regen_stamina(current_player)
            self.__rounds += 1
