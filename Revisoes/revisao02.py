import sqlite3

def criar_tabela():
    try:
        conexao = sqlite3.connect("hospital.db")
        cursor = conexao.cursor
        cursor.execute("PRAGMA foreing_keys = ON;")
        cursor.execute ('''CREATE TABLE IF NOT EXISTS cinemas 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        shopping TEXT,)''')
        cursor.execute ('''CREATE TABLE IF NOT EXISTS salas
                        (id_cinema INTEGER PRIMARY KEY AUTOINCREMENT,
                        numero TEXT,
                        capacidade INTEGER,
                    )''')
    finally:
        conexao.close()    
def cadastrar(numero, capacidade):
    try:
        conexao = sqlite3.connect("hospital.db")
        cursor = conexao.cursor
        cursor.execute("PRAGMA foreing_keys = ON;")
        cursor.execute('''INSERT INTO salas
                       (id, numero_sala, capacidade) VALUES (?, ?, ?)''', (id, numero, capacidade))
        conexao.commit()
        print(f"Sala{numero} cadastrada com sucesso! ")
    except sqlite3.IntegrityError:
        print("Sala inexistente")
    finally:
        conexao.close()

def listar():
    try:
        conexao = sqlite3.connect("hospital.db")
        cursor = conexao.cursor
        cursor.execute("PRAGMA foreing_keys = ON;")
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


while True:
    print("-----Sistema de cinema-----")
    print("1-CADASTRAR | 2-LISTAR")
    opcao = int(input("Digite a opção: "))
    if opcao == "1"