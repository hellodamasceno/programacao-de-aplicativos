import sqlite3

def criar_tabela():
    try:
        conexao = sqlite3.connect("hospital.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute ('''CREATE TABLE IF NOT EXISTS cinemas 
                        (id_cinema INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        shopping TEXT
                        )''')
        cursor.execute ('''CREATE TABLE IF NOT EXISTS salas
                        (id_cinema INTEGER PRIMARY KEY AUTOINCREMENT,
                        numero TEXT,
                        capacidade INTEGER,
                        FOREIGN KEY (id_cinema) REFERENCES cinemas(id)
                    )''')
        conexao.commit()
    finally:
        conexao.close()   



def cadastrar(numero, capacidade, id_cinema):
    try:
        conexao = sqlite3.connect("hospital.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''INSERT INTO salas
                       (numero_sala, capacidade, id_cinema) VALUES (?, ?, ?)''', (numero_sala, capacidade, id_cinema))
        conexao.commit()
        print(f"Sala{numero} cadastrada com sucesso! ")
    except sqlite3.IntegrityError:
        print("Sala inexistente")
    finally:
        conexao.close()

def listar():
    try:
        conexao = sqlite3.connect("hospital.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        print("Lista das salas ")
        cursor.execute(''' SELECT id, numero_sala, capacidade, id_cinema FROM salas''')
        todas_salas = cursor.fetchall()
        if todas_salas:
            for sala in todas_salas:
                print(f"ID registro: {sala[0]} | sala N: {sala[1]} | capacidade: {sala[2]} lugares | id cinema {sala[3]}")
    except sqlite3.IntegrityError:
        print("Nenhuma sala cadastrada! ")
    finally:
        conexao.close()     

def menu():
    while True:
        print("-----Sistema de cinema-----")
        print("1-CADASTRAR | 2-LISTAR | 3-SAIR")
        opcao = int(input("Digite a opção: "))
        if opcao == 1 :
            print("----1 CADASTRO-----")
            numero = int(input("Digite o numero da sala: "))
            capacidade = int(input("Digite a capacidade da sala: "))
            id_cinema = int(input("Digite o ID do cinema: "))
            cadastrar(numero, capacidade, id_cinema)

        elif opcao == 2:
            print("----2 LISTA DE SALAS----")
            listar()
        elif opcao == 3:
            print("Saindo do sistema...") 
            break 

criar_tabela()  
menu()
