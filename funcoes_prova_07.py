
def AdicionarAluno(matricula:str, nome:str, dicAlunos:dict)->str:
    dicAlunos[matricula] = nome
    return f'Aluno(a) "{nome}" matriculado(a) com sucesso.\n'


def RemoverAluno(matricula:str, dicAlunos:dict)->str:
    retorno = dicAlunos.get(matricula,False)
    if retorno is False:
        return '\nMatrícula não identificada'

    else:
        dicAlunos.pop(matricula)
        return f'\nA matrícula do aluno "{retorno}" foi excluída com sucesso!'


def AtualizarAluno(matricula:str, dicAlunos:dict)->str:
    retorno = dicAlunos.get(matricula,False)
    if retorno is False:
        return '\nMatrícula não encontrada'
    else:
        nome = input('Digite o novo nome do aluno: ')
        dicAlunos[matricula] = nome
        print(f'\nA matrícula do aluno "{retorno}" foi atualizada com sucesso!')
        print('Matricula | Nome Aluno')
        return f'        {matricula} | {dicAlunos[matricula]}'


def VerAlunos(dicAlunos:dict)->str:
    if len(dicAlunos) > 0:
        print('Matricula | Nome Aluno')
        for chv, vl in dicAlunos.items():
            print(f'        {chv} | {vl}\n')
    else:
        print('Não existem alunos cadastrados.')
