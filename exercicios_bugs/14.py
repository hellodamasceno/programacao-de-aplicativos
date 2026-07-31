import sqlite3

def cadastar_serie_seguro(nome, id_escola):
    conexao = None
    try: 
        conexao = sqlite3.connect('/pasta_protegida/sistema.db') 
        cursor = conexao.cursor() 
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?,?)", (nome, id_escola)) 
        conexao.commit() 
    except sqlite3.Error as e: 
        print("Erro técnico:", e) 
    finally: 
        conexao.close() 
#Faltava o conexao none,que garante que a variavél exista antes de entrar no try 