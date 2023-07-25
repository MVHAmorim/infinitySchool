# Escreva um código em Python que peça três números e determine:
# - O maior número;
# - O menor número;
# - Se existem números iguais e caso exista, quais são os números

n1: int
n2: int
n3: int 
nMax: int
nMin: int
comp: str

print ("Digite 3 números:\n")
n1 = input ("Digite o primeiro número: ")
n2 = input ("Digite o segundo número: ")
n3 = input ("Digite o terceiro número: ")

lista = [n1, n2, n3]
nMax = max(lista)
nMin = min(lista)

if (n1 == n2 == n3):
    comp = f'Números iguais: {n1}, {n2} e {n3}'
elif (n1 == n2):
    comp = f'Números iguais: {n1} e {n2}'
elif (n1 == n3):
    comp = f'Números iguais: {n1} e {n3}'
elif (n2 == n3):
    comp = f'Números iguais: {n2} e {n3}'
else:
    comp = f'Não existem números repetidos.'

print(f"""
      Número mínimo: {nMin}
      Número máximo: {nMax}
      {comp}
      """)