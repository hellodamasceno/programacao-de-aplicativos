import sqlite3

def verificar_registros():
    conexao = sqlite3.connect("Escola_demonstracao.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos ")
    registros = cursor.fetchall()
    print("Primeiro print:", registros)
    print("Segundo print:", registros)

    conexao.close ()

    #pq no primeiro fetchall ele ja le todas as linhas netao no segundo não vai ter mais nada para aparecer no terminal 
