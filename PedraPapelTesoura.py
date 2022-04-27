import random
def jogar():
    jogador = input(f"Qual é a sua escolha?: 'r' para Pedra, 'p' para Papel, 't' para Tesoura: ")
    oponente = random.choice(['r', 'p', 't'])

    if jogador == oponente:
        return 'Deu um empate!'

    if ganhador(jogador, oponente):
        return 'Você ganhou!'

    if ganhador(oponente, jogador):
        return 'Você perdeu!'

def ganhador(jogador, computador):
    #Retornar true se jogador ganhar
    #logica  Tesoura > Papel;, Pedra > Tesoura;, Papel > Pedra

    if (jogador == 'r' and computador == 't') or (jogador == 't' and computador == 'p') or \
            (jogador == 'p' and computador == 'r'):
        return True

print(jogar())