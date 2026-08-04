import sqlite3

# def iniciar_banco():
#     try:
#         conexao = sqlite3.connect("hospital.db")
#         cursor = conexao.cursor()
#         cursor.execute("PRAGMA foreing_keys = ON;")
#         cursor.execute('''CREATE TABLE IF NOT EXISTS
#                     hospitais (
#                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                         nome TEXT NOT NULL,
#                         cidade TEXT
#                     )''')
#         cursor.execute('''CREATE TABLE IF NOT EXISTS
#                     medicos (
#                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                         nome TEXT, 
#                         crm TEXT NOT NULL,
#                         id_hospital INTEGER NOT NULL,
#                         FOREIGN KEY (id_hospital) REFERENCES hospitais(id) 
#                     )''')
#         conexao.commit()
#         print("Tabelas criada com sucesso! ")
#     finally:
#         conexao.close()       

# iniciar_banco()



def cadastrar_hospital (nome, cidade):
    try:
        conexao = sqlite3.connect("hospital.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON; ")
        cursor.execute('''INSERT INTO hospitais
                       (nome, cidade) VALUES (?, ? )''', (nome, cidade))
        conexao.commit()
        print(f"Hospital {nome} cadrastado ")
    except sqlite3.IntegrityError:
        print("O hospital não existe")
    finally:
        conexao.close()



def cadastrar_medico(nome, crm, id_hospital):
    try:
        conexao = sqlite3.connect("hospital.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON; ")
        cursor.execute(''' INSERT INTO medicos
                       (nome, crm, id_hospital)
                       VALUES (?, ?, ? )''', (nome, crm, id_hospital))
        conexao.commit()
        print(f"Médico(a) {nome} cadastrado com sucesso! ")
    except sqlite3.IntegrityError:
        print(f"Erro: O hospital com o ID {id_hospital} não existe no sistema! ")
    finally:
        conexao.close()
      




def menu():
    while True:
        print("----Sistema Hospital------")
        print("1-Cadastrar hospital")
        print("2-Cadastar Medico")
        opcao = input("Digite a opçao desejada: ")

        if opcao == "1":
            print("-----CADASTRO HOSPITAL-------")
            nome_hospital = input("Digite o nome do hospital: ")
            cidade = input("Digite a cidade do hospital: ")
            cadastrar_hospital(nome_hospital, cidade,)
        elif opcao == "2":
            print("---------CADASTRO DE MEDICOS-------")
            nome_medico = input("Digite o nome do medico(a): ")
            crm = input("Digite o CRM: ")
            id_hospital = int(input("Digite o ID do hospital: "))
            cadastrar_medico(nome_medico, crm, id_hospital)
        elif opcao == "3":
            print("Saindo do sistema ")
            break  
        else:
            print("Opcao errada ")
            
menu()            