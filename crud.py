import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='crudpython',
)

cursor = conexao.cursor ()

nome_produto = "toddynho"
valor = 10
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}" '
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()

#CREATE

#nome_produto = "Ferreiro Rocher"
#valor = 20
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit()

#READ

# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

#UPDATE

# nome_produto = "toddynho"
# valor = 10
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}" '
# cursor.execute(comando)
# conexao.commit()

#DELETE

# nome_produto = "toddynho"
# valor = 10
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}" '
# cursor.execute(comando)
# conexao.commit()




