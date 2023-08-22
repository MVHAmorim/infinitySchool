
# Maneiras de criar dicionários
dicionario = {}
dicionario = dict(Modulo = 'Python', Instituicao = 'Infinity School')
dicionario = dict({'Modulo': 'Python', 'Instituicao': 'InfinitySchool'}, Modulo = 'Lógica de Programação')

# Criando dicionário usando compreensão
dicionario = {num: num * 10 for num in range(1,11)}

#--> Funções para obter informações de dicionários <--#

# Retorna uma lista com todas as chaves usadas no dicionário
dicionario = dict(Modulo = 'Python', Instituicao = 'Infinity School')
print(list(dicionario))

# Retorna o valor da chave especificada entre colchetes. Caso a chave não exista, 
# uma exceção do tipo KeyError será lançada (print(dicionario[Chave]))
dicionario = dict(Modulo = 'Python', Instituicao = 'Infinity School')
print(dicionario['Modulo'])

# Remove a chave e seu respectivo valor do dicionario (dicionario.pop(Chave) )
dicionario = dict(Modulo = 'Python', Instituicao = 'Infinity School')
del dicionario['Modulo'] #Essa forma de exclusão está depreciada e devemos evitar utilizá-la
# dicionario.pop('Modulo') 

# Retorna o número de itens de um dicionário
print(len(dicionario))

# Atualizar valores das chaves de um dicionário (dicionario[chave] = valor)
dicionario = dict(Modulo = 'Python', Instituicao = 'Infinity School')
dicionario['Modulo'] = 'Curso de Python'

# Verificar se uma determinada chave existe no dicionário (chave in dicionario)
dicionario = dict(Modulo = 'Python', Instituicao = 'Infinity School')
print('Modulo' in dicionario)

# Verificar se uma determinada chave NÃO existe no dicionário (chave not in dicionario)
dicionario = dict(Modulo = 'Python', Instituicao = 'Infinity School')
print('Matéria' not in dicionario)

# Remove todos os itens do dicionário
dicionario = {num: num * 10 for num in range(1,11)}
dicionario.clear()
print(dicionario)

# Cria um dicionário usando uma lista de chaves com valores None (dict.fromkeys(iteravel))
dicionario =['Modulo', 'Instituicao']
print(dict.fromkeys(dicionario))

# Retorna um iterador para as chaves do dicionário. Retorna o mesmo que dicionario.keys() (iter(dicionario))
print(iter(dicionario))

# Retorna uma cópia do dicionário
dicionario2 = dicionario.copy()
print(dicionario2)

# Retorna o valor para a chave especificada se esta existir no dicionário, senão, será retornado um valor padrão definido. 
# Caso este valor não seja definido, a função retornará None (dicionario.get(chave, valor padrão))
dicionario = dict({'Modulo': 'Python', 'Instituicao': 'InfinitySchool'})
print(dicionario.get('Modulo', 'Não Existe'))

# Retorna uma lista contendo pares de tuplas, onde, em cada uma dessas tuplas,
# o primeiro elemento será a chave do dicionário e o segundo elemento o valor (dicionario.items())
print(dicionario.items())

# Retorna uma lista dos valores do dicionário
print(dicionario.values())

# Atualiza o dicionário com os elementos de outro objeto de dicionário ou de um iterável de pares chave / valor. dicionario.update(dicionario)
dicionario = {}
dicionario2 = {'Modulo': 'Python', 'Instituicao': 'Infinity School'}
dicionario.update(dicionario2)
print(dicionario)

# Retorna uma lista das chaves do dicionário (dicionario.keys())
print(dicionario.keys())


# Remove a chave se esta existir no dicionário, senão, retornará o valor padrão.
# Caso a chave não exista e não existir um valor padrão, um erro do tipo KeyError será lançado (dicionario.pop(chave, valor padrao))
dicionario = {'Modulo': 'Python', 'Instituicao': 'Infinity School'}
dicionario.pop('Modulo', 'Valor')
print(dicionario)