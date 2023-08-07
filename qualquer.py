from repositorio_cardapio import RepositorioCardapio
from repositorio_produto import RepositorioProduto

repCardapio = RepositorioCardapio('db.sqlite')
repProduto = RepositorioProduto('db.sqlite')

#--------------------------------------------------------------------------------------
# TESTE DO REPOSITÓRIO CARDÁPIO
#--------------------------------------------------------------------------------------

# Criar cardápio
repCardapio.criar_cardapio('CardapioTeste', 'Cardapio Testes 34', 'Quarto teste de cadastro de cardápio')

# Alterar cardapio
repCardapio.alterar_cardapio('CardapioTeste', 'Cardapio Teste ALTERADO', 'Alteração de teste de cadastro de cardápio')

# Listar cardápio
print(repCardapio.listar_cardapio())

# Consultar cardápio
print(repCardapio.consultar_cardapio('CardapioTeste'))

# Deletar cardápio
print(repCardapio.deletar_cardapio('CardapioTeste'))



#--------------------------------------------------------------------------------------
# TESTE DO REPOSITÓRIO PRODUTO
#--------------------------------------------------------------------------------------

# Criar cardápio
repProduto.criar_produto('ProdutoTeste', 'Produto Teste', 'Descrição do primeiro produto teste', 15.90, 'padrão', 'teste')

# Alterar cardapio
repProduto.alterar_produto('CardapioTeste', 'Produto Teste ALTERADO', 'Alteração de teste do cadastro do produto teste', 10.90, 'vegano', 'teste2')

# Listar cardápio
print(repProduto.listar_produto())

# Consultar cardápio
print(repProduto.consultar_produto('ProdutoTeste'))

# Deletar cardápio
print(repProduto.deletar_produto('ProdutoTeste'))