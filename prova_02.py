# Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. 
# Em seguida, o programa deve separar os números pares e ímpares em listas diferentes.
# Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares 
# e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.

lista = []
lstPares = []
lstImpares = []
tupla = ()

print('Digite uma sequência de 10 números inteiros: \n\n')
for i in range(1,11):
    n = int(input(f'Digite o número {i}: '))
    lista.append(n)

for n in lista:
    if (n % 2 == 0):
        lstPares.append(n)

    else:
        lstImpares.append(n)

tplPares = tuple(lstPares)
qtdPares = len(lstPares)
sPares = sum(tplPares)

tplImpares = tuple(lstImpares)
qtdImpares = len(lstImpares)
sImpares = sum(tplImpares)

print('\nNúmeros Pares:\n----------------------------------')
print(f'Tupla: {tplPares}')
print(f'Quantidade de números: {qtdPares}')
print(f'Soma dos termos: {sPares}')

print('\nNúmeros Ímpares:\n----------------------------------')
print(f'Números ímpares: {tplImpares}')
print(f'Quantidade de números: {qtdImpares}')
print(f'Soma dos termos: {sImpares}')