
# Maneiras de criar Conjuntos
conjunto = {'Python', 'Infinity School', 3}

# Usando o método construtor
conjunto = set(['Python', 'Infinity School', 3])

# Criando um conjunto usando compreensão
conjunto = {letra for letra in 'Infinity' if letra not in 'aeiou'}
print(conjunto)

#--> Funções para obter informações de conjuntos <--#

# Retorna True se o elemento exsitir naquele conjunto, senão, retorna False
conjunto = {'Python', 'Infinity School', 3}
for elemento in ['a','b','c']:
    print(elemento in conjunto)

# Retorna True se o elemento não exsitir naquele conjunto, senão, retorna False
conjunto = {'Python', 'Infinity School', 3}
for elemento in ['a','b','c']:
    print(elemento not in conjunto)

# Atualiza o conjunto, adicionando os elementos entre parênteses
conjunto = set()
conjunto2 = ('Modulo', 'Python', 'Instituicao', 'Infinity School')
conjunto.update(conjunto2)
print(conjunto)

# Atualiza o conjunto, adicionando os elementos entre parênteses
print(len(conjunto))

# Retorna uma cópia do dicionário
conjunto3 = conjunto.copy()
print(conjunto3)

# Adiciona um elemento ao conjunto
conjunto.add('elemento')
print(conjunto)

# Remove o elemento do conjunto. Uma exceção do tipo KeyError será lançada se o elemento não existir no conjunto
conjunto.remove('elemento')
print(conjunto)

# Remove o elemento se o mesmo existir no conjunto
conjunto.discard('Python')
print(conjunto)

# Remove todos os elementos do conjunto
conjunto.clear()
print(conjunto)
