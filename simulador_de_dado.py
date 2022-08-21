import random

jogada = input('Qual dado voce deseja jogar?\n'
               '2-d2\n'
               '4-d4\n'
               '6-d6\n'
               '20-d20\n')
quant_dados = input('Quantos dados deseja jogar: \n'
                        '1 ou 2\n')


def dados(jogada, quant_dados):
    if jogada == '2':
        d2 = random.randint(1, 2)
        d2_1 = random.randint(1, 2)
        if quant_dados == '1':
            print('Voce jogou um D2 = ', d2)
        elif quant_dados == '2':
            print('Primeiro D2 = ', d2)
            print('Segundo D2 = ', d2_1)

    elif jogada == '4':
        d4 = random.randint(1, 4)
        d4_1 = random.randint(1, 4)
        if quant_dados == '1':
            print('Voce jogou um D4 = ', d4)
        elif quant_dados == '2':
            print('Primeiro D4 = ', d4)
            print('Segundo D4 = ', d4_1)

    elif jogada == '6':
        d6 = random.randint(1, 6)
        d6_1 = random.randint(1, 6)
        if quant_dados == '1':
            print('Voce jogou um D6 = ', d6)
        elif quant_dados == '2':
            print('Primeiro D6 = ', d6)
            print('Segundo D6 = ', d6_1)

    elif jogada == '20':
        d20 = random.randint(1, 20)
        d20_1 = random.randint(1, 20)
        if quant_dados == '1':
            print('Voce jogou um D20 = ', d20)
        elif quant_dados == '2':
            print('Primeiro D20 = ', d20)
            print('Segundo D20 = ', d20_1)

    else:
        print('Digite uma opção valida.')


dados(jogada, quant_dados)

'''
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

if dado1 == dado2:
    print('dobrado')
    print(dado1, dado2)

else:
    print('\nD1', dado1, '\ne', '\nD2', dado2)
'''
