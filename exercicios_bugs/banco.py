import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
               CREATE TABLE IF NOT EXISTS escolas (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL
               )''')  
    conexao.commit() 
    conexao.close()
inicializar_banco()
#NÃO ESTÁ SALVANDO PQ ESTA FALTANDO O CONEXÃO COMMIT
