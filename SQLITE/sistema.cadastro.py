import sqlite3 
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()
nome_aluno= input("Digite o nome do aluno: ")
telefone_aluno= input("Digite o telefone do aluno: ")
turma_aluno= input("Digite a turma do aluno: ")
idade_aluno = int(input("Digite a idade do aluno: "))
cpf_aluno =input("Digite o CPF do aluno: ")


cursor.execute ('''
               CREATE TABLE IF NOT EXISTS ESCOLA_DEMONSTRACAO
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               telefone TEXT,
                turma TEXT,
               idade INTEGER,
               cpf TEXT UNIQUE)''')


comando_inserir = (f'''
                    insert into escola_demonstracao
                    (nome, telefone, turma, idade, cpf)
                    values('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}',
                    {idade_aluno}, '{cpf_aluno}')''')
cursor.execute(comando_inserir)
conexao.commit()

cursor.execute("SELECT * FROM ESCOLA_DEMONSTRACAO")
for aluno in cursor.fetchall():
    print(aluno)

conexao.close()