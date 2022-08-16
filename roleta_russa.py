import random
import time

escolha = input('Voce deseja jogar ROLETA RUSSA? S/N: ')
morte = 0
bala = random.randint(1, 6)
pontuacao = 0


while morte == 0:

    if escolha == 's' and 'S':
        print('Posição da bala:', bala)
        time.sleep(1)
        print('Fogo!')
        resultado = random.randint(1, 6)
        print('Resultado: ', resultado)
        if resultado != bala:
            print('Falhou.')
            pontuacao = pontuacao + 1
        elif resultado == bala:
            print('Voce morreu, XD.')
            morte = 1
            print('Pontuação: ', pontuacao)
    elif escolha != 's' and 'S':
        print('Jogo Encerrado.')
        morte = 1
