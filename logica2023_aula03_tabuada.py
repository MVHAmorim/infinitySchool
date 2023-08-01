num = int(input('Escolha um número inteiro entre 1 e 10 para gerar a tabuada: '))

print(f'Tabuada de {num}: \n')
for i in range(1, 11):
    resp = num * i    
    print(f'{num} x {i} = {resp}')