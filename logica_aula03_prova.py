# Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas. No final do programa, exiba:

# - A média de idade de todo o grupo.
# - Qual o nome da pessoa mais velha.
# - Quantas pessoas têm menos de 20 anos.
# - Quantas pessoas têm mais de 40 anos.
# - Qual o sexo da pessoa mais nova.

nomes = []
idades = []
sexos = []
menos20 = 0
mais40 = 0

for i in range(5):
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo: ')        
    print('----------------------\n')
    
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

mediaIdade = sum(idades) / 5
nomeMaisVelho = nomes[idades.index(max(idades))]
sexoMaisNovo = sexos[idades.index(min(idades))]

for item in idades:
    if item < 20:          
        menos20 = menos20 + 1
    elif item > 40:          
        mais40 = mais40 + 1

print(f'A média de idade do grupo é de: {mediaIdade}')
print(f'O nome da pessoa mais velha é: {nomeMaisVelho}')
print(f'A quantidade de pessoas com menos de 20 anos é de: {menos20}')
print(f'A quantidade de pessoas com mais de 40 anos é de: {mais40}')
print(f'O sexo da pessoa mais nova é: {sexoMaisNovo}')