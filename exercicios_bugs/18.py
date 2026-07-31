import sqlite3 
 
def cadastrar_lista_alunos(): 
    lista_alunos =[
    ("Ana", 1), 
    ("Carlos", 1), 
    ("Beatriz", 2)
    ]
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
    cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", lista_alunos) 
     
    conexao.commit() 
    conexao.close()

    #Para passar a lista tem que ser usando o comando executemany e colocando uma tupla de dados por vez 