# Escreva um programa em python que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

listNum = []

while True:
    num = int(input('Digite um número inteiro ou zero para encerrar: '))
    if num != 0:
        listNum.append(num)
    else:
        break

digitos = len(listNum)
soma = sum(listNum)
media = soma / digitos

print(f'Números digitados: {digitos}')
print(f'Soma dos números digitados: {soma}')
print(f'Média aritimética dos números digitados: {media}')