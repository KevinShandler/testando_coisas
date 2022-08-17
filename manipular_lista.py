# acabou virando uma lista :)
produtos = ['TESTE']
produto = ''
sair = 0
escolha = int(input('----------Menu----------\n'
                    '1 - Listar Produtos\n'
                    '2 - Cadastrar Produto\n'
                    '3 - Remover Produto\n'
                    '4 - Sair\n'
                    '------------------------\n'))

while sair < 1:
    if escolha == 1:
        if not produtos:
            print('\nNenhum item cadastrado\n')
            escolha = int(input('----------Menu----------\n'
                                '1 - Listar Produtos\n'
                                '2 - Cadastrar Produto\n'
                                '3 - Remover Produto\n'
                                '4 - Sair\n'
                                '------------------------\n'))
        else:
            print('\n')
            print(produtos)
            print('Total de itens: ', len(produtos))
            print('\n')
            escolha = int(input('----------Menu----------\n'
                                '1 - Listar Produtos\n'
                                '2 - Cadastrar Produto\n'
                                '3 - Remover Produto\n'
                                '4 - Sair\n'
                                '------------------------\n'))
    elif escolha == 2:
        produto = str(input('Nome do produto: ', ))
        produtos.append(produto.upper())
        print('Produto cadastrado com sucesso.\n')
        escolha = int(input('----------Menu----------\n'
                            '1 - Listar Produtos\n'
                            '2 - Cadastrar Produto\n'
                            '3 - Remover Produto\n'
                            '4 - Sair\n'
                            '------------------------\n'))
    elif escolha == 3:
        produto = input('Qual produto deseja remover: ')
        produtos.remove(produto.upper())
        print('\nItem removido com sucesso\n')
        escolha = int(input('----------Menu----------\n'
                            '1 - Listar Produtos\n'
                            '2 - Cadastrar Produto\n'
                            '3 - Remover Produto\n'
                            '4 - Sair\n'
                            '------------------------\n'))
    elif escolha == 4:
        sair = 2

    else:
        print('\nOpção invalida\n')
        escolha = int(input('----------Menu----------\n'
                            '1 - Listar Produtos\n'
                            '2 - Cadastrar Produto\n'
                            '3 - Remover Produto\n'
                            '4 - Sair\n'
                            '------------------------\n'))
