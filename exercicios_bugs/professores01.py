import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    cursor.execute('''
               CREATE TABLE IF NOT EXISTS professores
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               cpf TEXT NOT NULL UNIQUE ) 
               ''')
#Faltava colocar o NOT NULL UNIQUE, isso mostra para o sistema que cada professor tem que ter um unico cpf     
  