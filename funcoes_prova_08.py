def AdicionarProduto(nome:str, qtd:float, vlUnit:float, dicProdutos:dict)->str:
    vlTotal = qtd * vlUnit
    dicProdutos[nome] = [qtd, vlUnit, vlTotal]
    return vlTotal


def RemoverProduto(nome:str, dicProdutos:dict)->str:
    retorno = dicProdutos.get(nome,False)
    if retorno is False:
        return '\nProduto não encontrado'

    else:
        dicProdutos.pop(nome)
        return f'\nO produto "{nome}" foi excluído com sucesso!'


def AtualizarProduto(nome:str, novoNome:str, qtd:float, vlUnit:float, dicProdutos:dict)->str:
    retorno = dicProdutos.get(nome,False)
    if retorno is False:
        return '\nProduto não encontrado'
    else:
        dicProdutos.pop(nome)
        vlTotal = qtd * vlUnit
        dicProdutos[novoNome] = [qtd, vlUnit, vlTotal]        
        print(f'\nO cadastro do produto "{nome}" foi atualizado para "{novoNome}" com sucesso!')
        print('\nProduto [Qtd, vlUnit, vlTotal]')
        print(f'{novoNome} {dicProdutos[novoNome]}')


def ListarProdutos(dicProdutos:dict)->str:
    if len(dicProdutos) > 0:
        print('\nProduto [Qtd, vlUnit, vlTotal]')
        for chv, lst in dicProdutos.items():
            print(f'{chv} {lst}')
    else:
        print('Não existem produtos na lista.')


def totalizarLista(dicProdutos:dict)->float:
    totalLst = 0

    for lst in dicProdutos.values():
        totalLst += lst[2]

    return f'\nO valor total da lista está em: R$ {totalLst}'
