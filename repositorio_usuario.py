import sqlite3
from dtos import Cardapio

class RepositorioUsuario:

    def __init__(self, nome_completo_banco):
        self.nome_completo_banco = nome_completo_banco
        self.connection = None
        self.cursor = None


    def abrir_conexao(self):
        self.connection = sqlite3.connect(self.nome_completo_banco)
        self.cursor = self.connection.cursor()


    def fechar_conexao(self):
        self.cursor.close()        
        self.connection.close()
        self.cursor = None
        self.connection = None


    def criar_usuario(self, nome_usuario: str, nome_completo: str, cargo: str, salt_senha: bytes, hash_senha: bytes):
        sql = "INSERT OR IGNORE INTO usuario (nome_usuario, nome_completo, cargo, salt_senha, hash_senha) VALUES (?, ?, ?, ?, ?);"
        self.abrir_conexao()        
        self.cursor.execute(sql, (nome_usuario, nome_completo, cargo, salt_senha, hash_senha))
        self.connection.commit()
        criados = self.obter_mudancas()
        self.fechar_conexao()
        return criados


    def consultar_usuario(self, nome_usuario: str):
        sql = "SELECT nome_usuario, nome_completo, cargo FROM usuario WHERE nome_usuario = ?;"
        self.abrir_conexao()        
        self.cursor.execute(sql, (nome_usuario,))
        consultado = self.cursor.fetchone()
        self.fechar_conexao()
        return self.montarDTO(consultado)


    def consultar_salt(self, nome_usuario: str):
        sql = "SELECT salt_senha FROM usuario WHERE nome_usuario = ?;"
        self.abrir_conexao()
        self.cursor.execute(sql, (nome_usuario,))
        consultado = self.cursor.fetchone()
        self.fechar_conexao()
        return consultado


    def verificar_credenciais(self, nome_usuario: str, salt_senha: bytes, hash_senha: bytes):
        sql = "SELECT nome_usuario, nome_completo, cargo FROM usuario WHERE nome_usuario = ? AND salt_senha = ? AND hash_senha = ?;"
        self.abrir_conexao()        
        self.cursor.execute(sql, (nome_usuario,))
        consultado = self.cursor.fetchone()
        self.fechar_conexao()
        return self.montarDTO(consultado)


    def obter_mudancas(self):
        self.cursor.execute("SELECT changes();")
        alterados = self.cursor.fetchone()[0]
        return alterados        

    
    def montarDTO(self, tupla):
        nome_usuario, nome_completo, cargo = tupla
        return Cardapio(nome_usuario = nome_usuario, nome_completo = nome_completo, cargo = cargo)