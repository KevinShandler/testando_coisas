import random
import time

morte = 0
bala = random.randint(1, 6)
pontuacao = 0


while morte == 0:
    escolha = input('\nVoce deseja jogar ROLETA RUSSA? S/N: ')
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
            print('Voce morreu, XD.', '\nPontuação: ', pontuacao)
            morte = 1
    elif escolha != 's' and 'S':
        print('Jogo Encerrado.', '\nPontuação: ', pontuacao)
        morte = 1

