# acabou virando uma lista :)
produtos = ['TESTE']
produto = ''
sair = 0

while sair < 1:
    escolha = int(input('----------Menu----------\n'
                        '1 - Listar Produtos\n'
                        '2 - Cadastrar Produto\n'
                        '3 - Remover Produto\n'
                        '4 - Sair\n'
                        '------------------------'))
    if escolha == 1:
        if not produtos:
            print('\nNenhum item cadastrado\n')
        else:
            print('\n')
            print(produtos)
            print('Total de itens: ', len(produtos))
            print('\n')
    elif escolha == 2:
        produto = str(input('Nome do produto: ', ))
        produtos.append(produto.upper())
        print('Produto cadastrado com sucesso.\n')
    elif escolha == 3:
        produto = input('Qual produto deseja remover: ')
        produtos.remove(produto.upper())
        print('\nItem removido com sucesso\n')
    elif escolha == 4:
        sair = 2
    else:
        print('\nOpção invalida\n')
