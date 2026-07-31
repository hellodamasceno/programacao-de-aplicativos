import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

def inserir_escola(nome):
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,))
    conexao.commit()

#Falta o conexao.close 
#e necessario criar a conexao dentro de cada funcao.