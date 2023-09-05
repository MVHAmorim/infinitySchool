# Você está desenvolvendo um programa para gerenciar uma lista de compras. O programa permite adicionar produtos à lista, visualizar a lista de produtos, atualizar as informações de um produto existente e remover produtos da lista. Além disso, o programa calcula o valor total de todos os produtos da lista.
# O programa oferece as seguintes opções:
# Adicionar produtos: O usuário pode adicionar um novo produto à lista informando o nome, a quantidade e o valor unitário do produto. O programa calcula automaticamente o valor total do produto (quantidade * valor unitário) e atualiza o valor total de todos os produtos.
# Ver a lista de produtos: O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto, o valor unitário, a quantidade e o valor total do produto. Além disso, exibe o valor total de todos os produtos da lista.
# Atualizar produtos: O usuário pode atualizar as informações de um produto existente na lista. O programa solicita o nome do produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o valor unitário do produto. O programa recalcula automaticamente o valor total do produto e o valor total de todos os produtos.
# Remover produto: O usuário pode remover um produto da lista informando o nome do produto que deseja remover. O programa atualiza automaticamente o valor total de todos os produtos.
# Encerrar programa: Encerra a execução do programa.
# O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um dicionário com as informações: "produto", "valor", "quantidade" e "total". A variável totalProdutos é utilizada para armazenar o valor total de todos os produtos da lista.
# A cada operação realizada, o programa exibe mensagens indicando o resultado da operação.

from funcoes_prova_08 import *

dicProdutos = {}
nome:str
qtd:float
vlUnit:float

while True:
    opcao = input('''\nEscolha uma opção?\n
    1 - Cadastrar produto
    2 - Alterar produto    
    3 - Listar produtos
    4 - Excluir produto
    5 - Encerrar programa\n    
Digite a sua opção: ''')

    if opcao == '1':
        nome = input('\nDigite o nome do produto: ')
        qtd = float(input('Digite a quantidade: '))
        vlUnit = float(input('Digite o valor unitário: '))
        AdicionarProduto(nome, qtd, vlUnit, dicProdutos)
        print(totalizarLista(dicProdutos))

    elif opcao == '2':
        nome = input('\nDigite o nome do produto que deseja alterar: ')
        novoNome = input('\nDigite o novo nome do produto: ')
        qtd = float(input('Digite a quantidade: '))
        vlUnit = float(input('Digite o valor unitário: '))
        AtualizarProduto(nome, novoNome, qtd,vlUnit, dicProdutos)
        print(totalizarLista(dicProdutos))

    elif opcao == '3':        
        ListarProdutos(dicProdutos)
        print(totalizarLista(dicProdutos))

    elif opcao == '4':
        nome = input('\nDigite o nome do produto que deseja excluir: ')
        print(RemoverProduto(nome, dicProdutos))
        print(totalizarLista(dicProdutos))

    elif opcao == '5':
        print('\nPrograma encerrado pelo usuário. Até mais')
        break

    else:
        print('#####----->>>>> OPÇÃO INVÁLIDA! <<<<<-----#####\n')
