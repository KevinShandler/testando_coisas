# imprimir uma etiqueta

produtos = ['FACA', 'COLHER', 'GARFO', 'FEIJÃO', 'ARROZ', 'AÇUCAR']
produto = ''
sair = 0
escolha = int(input('Escolha uma opção: \n1-Listar Produtos\n2-Cadastrar Produto'
                    '\n3-Remover Produto \n4-Sair\n'))

while sair <= 1:
    if escolha == 1:
        print('\n')
        print(produtos)
        print('\n')
        escolha = int(input('Escolha uma opção: \n1-Listar Produtos\n2-Cadastrar Produto'
                            '\n3-Remover Produto \n4-Sair\n'))
    elif escolha == 2:
        produto = str(input('Nome do produto: ', ))
        produtos.append(produto.upper())
        print('Produto cadastrado com sucesso.')
        escolha = int(input('Escolha uma opção: \n1-Listar Produtos\n2-Cadastrar Produto'
                            '\n3-Remover Produto \n4-Sair\n'))
    elif escolha == 3:
        produto = input('Qual produto deseja remover: ')
        produtos.remove(produto.upper())
        escolha = int(input('Escolha uma opção: \n1-Listar Produtos\n2-Cadastrar Produto'
                            '\n3-Remover Produto \n4-Sair\n'))
    elif escolha == 4:
        sair = 2
