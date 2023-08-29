# Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
# O programa deve fornecer as seguintes funcionalidades:
# Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
# Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
# Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.
# O programa deve ser executado em um loop contínuo até que o usuário escolha sair.

dicAlunos = {}
matricula = 0
nome = ""

while True:
    opcao = int(input('''\nEscolha uma opção?\n
    1 - Cadastrar um aluno
    2 - Excluir um aluno
    3 - Listar alunos
    4 - Sair\n    
Digite a sua opção: '''))

    if opcao == 1:        
        matricula = input('\nDigite a matrícula: ')
        nome = input('Digite o nome do aluno: ')
        dicAlunos[matricula] = nome
        print('Aluno matriculado com sucesso.\n')

    elif opcao == 2:
        matricula = input('\nDigite a matrícula que deseja excluir: ')
        retorno = dicAlunos.get(matricula,False)
        if retorno is False:
            print('\nMatrícula não identificada')
        else:
            dicAlunos.pop(matricula)
            print(f'\nA matrícula do aluno {retorno} foi excluída com sucesso!')

    elif opcao == 3:
        print('Matricula | Nome Aluno')
        for chv, vl in dicAlunos.items():
            print(f'        {chv} | {vl}')

    elif opcao == 4:
        print('\nPrograma finalizado pelo usuário. Até mais')
        break

    else:
        print('#####----->>>>> OPÇÃO INVÁLIDA! <<<<<-----#####\n')
