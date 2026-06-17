import sqlite3 

def cadastrar_aluno():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    nome_aluno= input("Digite o nome do aluno: ")
    telefone_aluno= input("Digite o telefone do aluno: ")
    turma_aluno= input("Digite a turma do aluno: ")
    idade_aluno = int(input("Digite a idade do aluno: "))
    cpf_aluno =input("Digite o CPF do aluno: ")
    id_professor = int(input("Digite o ID do professor responsavél: "))


    cursor.execute ('''
                CREATE TABLE IF NOT EXISTS ESCOLA_DEMONSTRACAO
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    turma TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE,
                    id_professor INTEGER,
                    FOREIGN KEY (id_professor) REFERENCES professores(id)
                )''')


    comando_inserir = (f'''
                        insert into escola_demonstracao
                        (nome, telefone, turma, idade, cpf, id_professor)
                        values('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}',
                        {idade_aluno}, '{cpf_aluno}', {id_professor})''')
    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()


def listar_aluno():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ESCOLA_DEMONSTRACAO")
    for aluno in cursor.fetchall():
        print(aluno)

    conexao.close()

def listar_professor():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM professores")

    for p in cursor.fetchall():
        print(p)

    cursor.execute("""
        SELECT
        ESCOLA_DEMONSTRACAO.nome,
        ESCOLA_DEMONSTRACAO.turma,
        professores.nome
        FROM ESCOLA_DEMONSTRACAO
        INNER JOIN professores
        ON ESCOLA_DEMONSTRACAO.id_professor = professores.id
        """)

    for registro in cursor.fetchall():
        print(
            "Aluno:", registro[0],
            "- Turma:", registro[1],
            "- Professor responsável:", registro[2]
        )
    conexao.close()

def alterar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    ID_atual = int(input("Digite o ID atual: "))
    cursor.execute(f''' SELECT * FROM alunos WHERE ID={ID_atual}''')
    aluno= cursor.fetchone()
    if not aluno:
        print("aluno não encontrado")
        conexao.close()       

        return

    else:
        novo_nome=input("Digite o novo nome: ")
        nova_idade = input("Digite a nova idade: ")
        novo_tel = input("Digite o novo telefone: ")
        nova_idade = int(input("Digite a nova idade: "))
        nova_turma = input("Digite a nova turma: ")
        novo_cpf = input("Digite o novo cpf: ")

    comando= f''' UPDATE alunos SET nome= '{novo_nome}',
                idade={nova_idade}, telefone= '{novo_tel}', idade='{nova_idade}',
                turma = '{nova_turma}', cpf= '{novo_cpf}' WHERE id={ID_atual}'''
    cursor.execute(comando)
    conexao.commit()
    conexao.close()



#EXCLUIR 
def excluir_aluno():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    listar_aluno ()

    id_aluno = int(input("Digite o ID do aluno: "))
    cursor.execute(f''' DELETE FROM  alunos 
                    WHERE id = {id_aluno}''') 
    print("aluno excluido com sucesso! ")
    conexao.commit()
    conexao.close()  
