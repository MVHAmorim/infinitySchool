def cadastro(user_nome:str, user_idade:int) -> str:
    return f"cadastro concluído com sucesso: \n Nome: {user_nome} - Idade: {user_idade}\n"

print(cadastro("José", 30))
print(cadastro("Maria", 25))
print(cadastro("João", 20))

def flor(flor:str = "Rosa", cor:str = "Vermelha") ->str:
    return f"Flor: {flor} - Cor: {cor}"

print(flor())
print(flor("Orquídea", "Azul"))
print(flor("Margarida", "Branca"))

# Funções args
def minha_funcao(*args):
    for arg in args:
        print(arg)
        
minha_funcao("José", "Maria", "João")


# Funções kwargs
def minha_funcao2(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")

minha_funcao2(nome="Rafaela", idade=23, cidade="Salvador")

# Funções args e kwargs em conjunto
def minha_funcao3(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for chave, valor in kwargs.items():
        print(chave, valor)
        
minha_funcao3("Curriculo", "Desenvolvedor", nome="Alice", idade=25)

# Exemplos de funções lambda
quadrado = lambda x : x ** 2
print(quadrado(5))

name_upperCase = lambda n : n.upper()
print(name_upperCase("José"))

