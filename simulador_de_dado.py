import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

if dado1 == dado2:
    print('dobrado')
    print(dado1, dado2)

else:
    print('\nD1', dado1, '\ne', '\nD2', dado2)