import sqlite3

conn = sqlite3.connect('database.db') # Criando a minha conexão (é o arquivo)
cursor = conn.cursor() # Criando um cursor (é o que conterá meus dados)

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')') # Adicionando uma tabela ao meu cursor
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Gabriel Rosin", 63.4)') # Adicionando dados na minha tabela
# conn.commit() # Executando as mudanças no meu arquivo
# Depois de criar minha tabela e inserir os dados, não preciso das linhas anteriores, então vou comentar elas


# Como evitar SQL injection (falha de segurança):
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ("Maria", 50))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {"nome": "Pedro","peso": 50.6}) # Outra forma de evitar SQL injection
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {"id": None, "nome": "Denis","peso": 100.6}) # Outra forma de evitar SQL injection
# conn.commit()
#
# Depois de criar minha tabela e inserir os dados, não preciso das linhas anteriores, então vou comentar elas

# Atualizando valores na minha DB:
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
               {'nome': 'Joana', 'id': 2}) # O dado que tinha como primary key 2 será alterado
conn.commit()

cursor.execute('SELECT * FROM clientes') # Mostrando tudo que tem no meu cursor

# Deletando um dado da minha DB (não tem como recuperar):
# cursor.execute('DELETE FROM clientes WHERE id=:id',
#                {'id': 2})
# conn.commit()

# Filtrando dados:
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
               {'peso': 60})

for linha in cursor.fetchall():
    print(linha) # Exibindo as minhas informações no cursor

cursor.close()
conn.close()