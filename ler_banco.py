import sqlite3

# Conectar ao banco de dados
connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()

# Fazer leitura para pegar todos
cursor.execute('SELECT * FROM produto;')

produtos = cursor.fetchall()
print('\n', produtos , '\n')

# Fazer leitura para pegar apenas um
cursor.execute('SELECT * FROM cardapio WHERE codigo = "bebida" LIMIT 1;')

cardapio = cursor.fetchone()
print('\n', cardapio , '\n')


# Checar linhas alteradas
cursor.execute("INSERT INTO cardapio (codigo, nome, descricao) VALUES ('sobremesas', 'Sobremesas', 'Sobremesas da casa')")
cursor.execute("SELECT changes();")
alterados = cursor.fetchone()[0]
print(f'O número de linhas alteradas foi: {alterados}')


# Refletir as mudanças no banco
connection.commit()

# Fechar o cursor e a conexão
cursor.close()
connection.close()
