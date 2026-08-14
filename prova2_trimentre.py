import sqlite3

def criar_tabela_redeoficina():
    try:
        conexao = sqlite3.connect("Oficina.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute('''CREATE TABLE IF NOT EXISTS rede_oficina
                       (id_rede INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT,
                       franquia TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS oficinas
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       cidade TEXT,
                       id_rede INTEGER,
                        FOREIGN KEY (id_rede)  REFERENCES rede_oficina (id_rede))''')
        conexao.commit()
    except sqlite3.Error:
        print("Erro no banco de dados ")
    finally:
        conexao.close()    

def cadastar_rede( nome, franquia):
    try:
        conexao = sqlite3.connect("Oficina.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''INSERT INTO rede_oficina
                       ( nome, franquia) VALUES (?,? ) ''' , (nome, franquia))
        conexao.commit()
        print(f" Rede {nome} cadastrada com a franquia  {franquia} com sucesso! ")
    except sqlite3.Error:
        print("Rede inexistente")
    finally:
        conexao.close()

def cadastar_oficina( cidade, id_rede):
    try:
        conexao = sqlite3.connect("Oficina.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''INSERT INTO oficinas
                       (cidade, id_rede) VALUES (?,? )''', (cidade, id_rede))
        conexao.commit()
        print(f" Oficina na cidade {cidade} cadastrada com  {id_rede} com sucesso! ")
    except sqlite3.Error:
        print("oficina inexistente")
    finally:
        conexao.close()


        
def listar_rede():
    try:
        conexao = sqlite3.connect("Oficina.db")
        cursor = conexao.cursor()
        print("\nLista de redes :")
        cursor.execute("SELECT id_rede, nome, franquia FROM rede_oficina ")
        todos = cursor.fetchall()
        if todos:
            for todo in todos:
                print(f"ID: {todo[0]} | Nome: {todo[1]} | Franquia: {todo[2]}")
    except sqlite3.Error:
            print("Nenhuma rede cadastrada")
    finally:
        conexao.close()

def listar_oficina():
    try:
        conexao = sqlite3.connect("Oficina.db")
        cursor = conexao.cursor()
        print("\nLista de oficinas :")
        cursor.execute("SELECT id, cidade FROM oficinas")
        todoos = cursor.fetchall()
        if todoos:
            for todos in todoos:
                print(f"ID: {todos[0]} | Cidade: {todos[1]} ")
    except sqlite3.Error:
            print("Nenhuma oficina cadastrada")
    finally:
        conexao.close()

def atualizar_redes():
    try:
        id_rede = input("Digite o ID da rede que deseja atualizar: ")
        conexao = sqlite3.connect("Oficina.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, franquia FROM rede_oficina WHERE id_rede = ?", (id_rede,))
        rede_atual = cursor.fetchone()
        if not rede_atual:
            print(f"Nenhuma rede encontrada com o ID {id_rede}.")
            conexao.close()
            return
        novo_nome = input("Digite o novo nome: ")
        nova_franquia = input("Digite a nova franquia: ")
        cursor.execute("""
            UPDATE rede_oficina 
            SET nome = ?, franquia = ? 
            WHERE id_rede = ?
        """, (novo_nome, nova_franquia, id_rede))
        
        conexao.commit()
        print(f"Rede ID {id_rede} atualizada com sucesso!")
    except sqlite3.Error:
        print("Erro ao atualizar")
    finally:
        conexao.close()


def atualizar_oficina():
    try:
        id_oficina = input("Digite o ID da oficina que deseja atualizar: ")
        conexao = sqlite3.connect("Oficina.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT cidade, id_rede FROM oficinas WHERE id = ?", (id_oficina,))
        oficina_atual = cursor.fetchone()
        if not oficina_atual:
            print(f"Nenhuma oficina encontrada com o ID {id_oficina}.")
            conexao.close()
            return
        nova_cidade = input("Digite o nome da nova cidade: ")
        cursor.execute('''
                       UPDATE oficinas
                       SET cidade = ? 
                       WHERE id = ?
                       ''', (nova_cidade, id_oficina))
        
        conexao.commit()
        print(f"Oficina ID {id_oficina} atualizada com sucesso!")
            
    except sqlite3.Error :
        print(f"Erro ao atualizar")
    finally:
        conexao.close()

def excluir_rede():
    try:
        conexao = sqlite3.connect("Oficina.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM rede_oficina ")
        print("Redes cadastrados")
        for rede in cursor.fetchall():
            print(rede)
            id_rede = int(input("Digite o id da rede a ser excluida: "))
            comando_excluir = (f'''DELETE FROM rede_oficina
                           WHERE id_rede = {id_rede}''')
            cursor.execute(comando_excluir)
        conexao.commit()
        print("Rede excluida")
        cursor.execute("SELECT * FROM rede_oficina")
        for redes in cursor.fetchall():
            print(redes)
    finally:
        conexao.close

def excluir_oficina():
    try:
        conexao = sqlite3.connect("Oficina.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM oficinas ")
        print("Oficinas  cadastrados")
        for oficina in cursor.fetchall():
            print(oficina)
            id_oficina = int(input("Digite o id da oficina para excluir: "))
            comando_excluir = (f'''DELETE FROM oficinas
                           WHERE id = {id_oficina}''')
            cursor.execute(comando_excluir)
            conexao.commit()
        print("Oficina excluida com sucesso")
        cursor.execute("SELECT * FROM oficinas")
        for ofc in cursor.fetchall():
            print(ofc)
    finally:
        conexao.close



def menu():
    while True:
        print("Sistema oficina ")
        print("1-Cadastar rede| 2-Cadastrar oficina| 3-Listar redes| 4-Listar oficina| 5-Excluir rede| 6-Excluir oficina| 7-Atualizar rede| 8-Atualizar oficina| 9-Sair")
        opcao = input("Digite a opção: ")
        if opcao == "1" :
            print("Cadastrar rede")
            nome_rede = input("Digite o nome da rede: ")
            franquia = input("Digite o nome da franquia: ")
            cadastar_rede(nome_rede, franquia)
        elif opcao == "2":
            print("Cadastrar oficina")
            nome = input("Digite o nome da cidade: ")
            id_rede = int(input("Digite o numero do ID: "))
            cadastar_oficina(nome, id_rede)
        elif opcao == "3":
            print("Listar redes") 
            listar_rede()
        elif opcao == "4":
            print("Listar oficinas") 
            listar_oficina()
        elif opcao == "5":
            print("Excluir rede")
            excluir_rede()
        elif opcao == "6":
            print("Excluir oficina")
            excluir_oficina()
        elif opcao == "7":
            print("Atualizar rede")
            atualizar_redes() 
        elif opcao == "8":
            print("Atualizar oficina")
            atualizar_oficina()       
        elif opcao == "9":
            print("Saindo do sistema...") 
            break       
criar_tabela_redeoficina()
menu()

