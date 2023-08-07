import sqlite3
from dtos import Cardapio

class RepositorioCardapio:

    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.connection = None
        self.cursor = None


    def abrir_conexao(self):
        self.connection = sqlite3.connect(self.nome_banco)
        self.cursor = self.connection.cursor()


    def fechar_conexao(self):
        self.cursor.close()        
        self.connection.close()
        self.cursor = None
        self.connection = None

    def criar_cardapio(self, codigo: str, nome: str, descricao: str):
        sql = "INSERT OR IGNORE INTO cardapio (codigo, nome, descricao) VALUES (?, ?, ?)"
        self.abrir_conexao()        
        self.cursor.execute(sql, (codigo, nome, descricao))
        self.connection.commit()
        criados = self.obter_mudancas()
        self.fechar_conexao()
        return criados


    def alterar_cardapio(self, codigo: str, nome: str, descricao: str):
        sql = "UPDATE cardapio SET nome = ?, descricao = ? WHERE codigo = ? "
        self.abrir_conexao()        
        self.cursor.execute(sql, (nome, descricao, codigo))
        self.connection.commit()        
        alterados = self.obter_mudancas()
        self.fechar_conexao()
        return alterados


    def deletar_cardapio(self, codigo: str):
        sql = "DELETE FROM cardapio WHERE codigo = ? "
        self.abrir_conexao()
        self.cursor.execute(sql, (codigo,))
        self.connection.commit()
        deletados = self.obter_mudancas()
        self.fechar_conexao()
        return deletados


    def listar_cardapio(self):
        sql = "SELECT codigo, nome, descricao FROM cardapio"
        self.abrir_conexao()        
        self.cursor.execute(sql)
        consultados = self.cursor.fetchall()
        self.fechar_conexao()
        return [self.montarDTO(consultado) for consultado in consultados]


    def consultar_cardapio(self, codigo: str):
        sql = "SELECT codigo, nome, descricao FROM cardapio WHERE codigo = ? "
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
        codigo, nome, descricao = tupla
        return Cardapio(codigo = codigo, nome = nome, descricao = descricao)