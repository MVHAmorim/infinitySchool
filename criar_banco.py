import sqlite3

# Ler o código SQL do arquivo
with open('db.sql', 'r', encoding='UTF-8') as file:
    sql_code = file.read()

# Conectar ao banco de dados
connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()

# Executar código
cursor.executescript(sql_code)

# Refletir as mudanças no banco
connection.commit()

# Fechar o cursor e a conexão
cursor.close()
connection.close()
