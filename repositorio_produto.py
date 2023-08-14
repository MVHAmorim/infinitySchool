import sqlite3
from dtos import Produto

class RepositorioProduto:

    def __init__(self, nome_banco) -> None:
        self.nome_banco = nome_banco
        self.connection = None
        self.cursor = None


    def abrir_conexao(self) -> None:
        self.connection = sqlite3.connect(self.nome_banco)
        self.cursor = self.connection.cursor()


    def fechar_conexao(self):
        self.cursor.close()        
        self.connection.close()
        self.cursor = None
        self.connection = None


    def criar_produto(self, codigo:str, nome: str, descricao: str, preco: float, restricao: str, cardapio: str):
        sql = "INSERT OR IGNORE INTO produto (codigo, nome, descricao, preco, restricao, cardapio) VALUES (?, ?, ?, ?, ?, ?)"
        self.abrir_conexao()        
        self.cursor.execute(sql, (codigo, nome, descricao, preco, restricao, cardapio))
        self.connection.commit()
        criados = self.obter_mudancas()
        self.fechar_conexao()
        return criados


    def alterar_produto(self, codigo:str, nome: str, descricao: str, preco: float, restricao: str, cardapio: str):
        sql = "UPDATE produto SET nome = ?, descricao = ?, preco = ?, restricao = ?, cardapio = ? WHERE codigo = ? "
        self.abrir_conexao()
        self.cursor.execute(sql, (nome, descricao, preco, restricao, cardapio, codigo))
        self.connection.commit()
        alterados = self.obter_mudancas()
        self.fechar_conexao()
        return alterados


    def alterar_preco_produto(self, codigo:str, preco: float):
        sql = "UPDATE produto SET preco = ? WHERE codigo = ? "
        self.abrir_conexao()
        self.cursor.execute(sql, (preco, codigo))
        self.connection.commit()
        alterados = self.obter_mudancas()
        self.fechar_conexao()
        return alterados


    def deletar_produto(self, codigo: str):
        sql = "DELETE FROM produto WHERE codigo = ? "
        self.abrir_conexao()
        self.cursor.execute(sql, (codigo,))
        self.connection.commit()
        deletados = self.obter_mudancas()
        self.fechar_conexao()
        return deletados


    def listar_produto(self):
        sql = "SELECT codigo, nome, descricao, preco, restricao, cardapio FROM produto"
        self.abrir_conexao()        
        self.cursor.execute(sql)
        consultados = self.cursor.fetchall()
        self.fechar_conexao()
        return [self.montarDTO(consultado) for consultado in consultados]


    def consultar_produto(self, codigo: str):
        sql = "SELECT codigo, nome, descricao, preco, restricao, cardapio FROM produto WHERE codigo = ? "
        self.abrir_conexao()        
        self.cursor.execute(sql, (codigo,))
        consultado = self.cursor.fetchone()
        self.fechar_conexao()
        return self.montarDTO(consultado)


    def obter_mudancas(self):
        self.cursor.execute("SELECT changes();")
        alterados = self.cursor.fetchone()[0]
        return alterados        

    
    def montarDTO(self, tupla):
        codigo, nome, descricao, preco, restricao, cardapio = tupla
        return Produto(codigo = codigo, nome = nome, descricao = descricao, preco = preco, restricao = restricao, cardapio = cardapio)