from repositorio_produto import RepositorioProduto
from repositorio_cardapio import RepositorioCardapio
from dotenv import dotenv_values

ENV = dotenv_values()

def obter_repo_cardapio():
    return RepositorioCardapio(ENV['NOME_DB'])


def obter_repo_produto():
    return RepositorioProduto(ENV['NOME_DB'])