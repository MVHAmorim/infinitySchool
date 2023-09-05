from funcoes_prova_07 import *

dicAlunos = {}
matricula = 0
nome = ""

while True:
    opcao = input('''\nEscolha uma opção?\n
    1 - Cadastrar aluno
    2 - Alterar aluno    
    3 - Listar alunos
    4 - Excluir aluno
    5 - Sair\n    
Digite a sua opção: ''')

    if opcao == '1':
        matricula = input('\nDigite a matrícula: ')
        nome = input('Digite o nome do aluno: ')
        print(AdicionarAluno(matricula, nome, dicAlunos))

    elif opcao == '2':
        matricula = input('\nDigite a matrícula que deseja alterar: ')
        print(AtualizarAluno(matricula, dicAlunos))

    elif opcao == '3':        
        VerAlunos(dicAlunos)

    elif opcao == '4':
        matricula = input('\nDigite a matrícula que deseja excluir: ')
        print(RemoverAluno(matricula, dicAlunos))

    elif opcao == '5':
        print('\nPrograma finalizado pelo usuário. Até mais')
        break

    else:
        print('#####----->>>>> OPÇÃO INVÁLIDA! <<<<<-----#####\n')
