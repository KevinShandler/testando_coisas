nome = 'Kevin Shandler'
idade = 28
altura = 1.76
peso = 104.3
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} de idade, mede {altura} de altura, pesa {peso} kg, seu imc é {imc:.2f} e seu ano de '
      f'nascimento é {ano_nascimento}.')
