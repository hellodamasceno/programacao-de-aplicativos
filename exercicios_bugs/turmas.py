import sqlite3
def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)",
                (nome, id_serie, id_prof))
    conexao.commit()
    conexao.close()

#O banco não fecha pq se der erro na linha 6 o conexao.close não fecha 
