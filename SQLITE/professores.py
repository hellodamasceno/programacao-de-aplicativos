import sqlite3


def criar_tabela():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    nome_professora= input("Digite o nome completo da professora: ")
    tel_professor = input("Digite o telefone: ")
    materia_professor = input("Digite a materia: ")
    idade = int(input("Digite a idade: "))
    salario = input("Digite o salário: ")
    endereco_professor = input("Digite o endereço do professor: ")
    nome_escola = input("Digite o nome da escola pretendente: ")

    cursor.execute ('''
                CREATE TABLE IF NOT EXISTS professores
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    materia TEXT,
                    idade INTEGER,
                    salario TEXT,
                    endereco TEXT,
                    nome_escola  TEXT )''')

    comando_inserir = (f'''
                        INSERT INTO professores
                        (nome, telefone, materia, idade, salario,  endereco , nome_escola)
                        VALUES('{nome_professora}', '{tel_professor}', '{materia_professor}',
                        {idade}, '{salario}' , '{endereco_professor}', '{nome_escola}')''')
    cursor.execute(comando_inserir)
    conexao.commit()
    cursor.execute("SELECT * FROM professores")
    for professora in cursor.fetchall():
        print(professora)
    conexao.close()

def listar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM professores")
    for aluno in cursor.fetchall():
        print(aluno)
    conexao.close()        




def alterar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    id_atual = int(input("Digite o ID que deseja alterar: ")) 

    cursor.execute(f''' SELECT * FROM professores WHERE ID={id_atual}''')
    professora= cursor.fetchone()
    if not professora:
        print("professor não encontrado")
    else:    
        novo_nome = input("Novo nome: ")
        novo_telefone = input("Novo telefone: ") 
        novo_endereco = input("Digite o novo endereço: ")
        cursor.execute(f'''UPDATE professores SET nome= '{novo_nome}', telefone='{novo_telefone}', endereco = '{novo_endereco}'
                   WHERE id= {id_atual} ''')  
    conexao.commit()
    print("Professor alterado com sucesso!")
    conexao.close()



def excluir():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    listar()
    id_professor = int(input("Digite o ID que deseja excluir: "))
    cursor.execute(f''' DELETE FROM  professores 
                   WHERE id = {id_professor}''') 
    print("Professor excluido com sucesso! ")
    conexao.commit()
    conexao.close()


while True:
    print("1-CADASTRAR | 2- LISTAR | 3- ALTERAR | 4- EXCLUIR | 5- SAIR ")
    opcao = input("Digite a opção: ")
    if opcao == "1" : criar_tabela()
    elif opcao =="2": listar()
    elif opcao =="3": alterar()
    elif opcao== "4": excluir()
    elif opcao == "5": break