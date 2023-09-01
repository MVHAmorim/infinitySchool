# Considere uma lista de números inteiros numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Utilizando as funções map(), filter() e reduce(), escreva um código que execute as seguintes operações:
# Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
# Função filter() para obter uma nova lista com números pares da lista numeros
# Função reduce()  para obter a soma de todos os números da lista numeros
# Qual o resultado obtido após a execução das operações acima?

from functools import reduce
from operator import add

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função map() para obter uma nova lista com o quadrado de cada número da lista numeros

# Primeira forma
def calcularQuadrado(num)->int:
    return num ** 2

quadrados = list(map(calcularQuadrado, numeros))
print(quadrados)

# Segunda forma
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)


# Função filter() para obter uma nova lista com números pares da lista numeros

# Primeira forma
def filtrarPares(num)->int:
    return num % 2 == 0

pares = list(filter(filtrarPares, numeros))
print(pares)

# Segunda forma
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# Função reduce()  para obter a soma de todos os números da lista numeros

# Primeira forma
def somar(acumulado, proximo):
    return acumulado + proximo

soma = reduce(somar, numeros)
print(soma)

# Segunda forma
soma = reduce(add, numeros)
print(soma)
