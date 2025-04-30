from mysql import connector 
import mysql 

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'aula8'
)

x = conexao.cursor()

#Criando a base de dados 

#x.execute('create database if not exists aula8')

#mostrar toda as bases de dados

#x.execute('show databases')

#for i in x:
    #print(i)

#usando o banco de dados

#x.execute('use aula8')

# x.execute('''create table if not exists aluno(
#           matricula int primary key auto_increment,
#           nome varchar(30) not null,
#           idade int(3),
#           email varchar(60))''')

#mostrar todas as tabelas

# x.execute('show tables')
# for i in x:
#     print(i)

#mostrar todas a descricao da tabela

# x.execute('desc aluno')
# for i in x:
#     print(i)

#inserior dados na tabela

# y = 'insert into aluno(nome,idade,email) values("Rafael",25,"rafaelsobral@gmail.com")'
# x.execute(y)
# conexao.commit()
# print(x.rowcount, 'Registro(s) inserido(s)')

# v = [
#     ("Rafaela",26,"rafaelsobrala@gmail.com"),
#     ("Rafaele",27,"rafaelsobrale@gmail.com"),
#     ("Rafaeli",28,"rafaelsobrali@gmail.com"),
#     ("Rafaelo",29,"rafaelsobralo@gmail.com"),
#     ("Rafaelu",21,"rafaelsobralu@gmail.com"),
#     ("Rafaelao",22,"rafaelsobralao@gmail.com"),
#     ("Rafaelee",23,"rafaelsobralee@gmail.com"),
# ]

# x.executemany('insert into aluno(nome,idade,email) values(%s,%s,%s)',v)
# conexao.commit()

# r = x.fetchone() #tras somente o primeiro dado da tabela

# x.execute('select nome from aluno where idade > 15')
# n = x.fetchall()
# print('Alunos maiores que 15 anos:')
# for i in n:
#     print(i)


# x.execute('select * from aluno order by nome')
# n = x.fetchall()
# print('Todos os dados do aluno:')
# for i in n:
#     print(i)


# x.execute('select nome from aluno order by nome desc')
# n = x.fetchall()
# print('Alunos:')
# for i in n:
#     print(i)







