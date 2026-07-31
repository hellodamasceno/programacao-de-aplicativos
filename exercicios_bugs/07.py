import sqlite3
def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect("escola_demonstracao.db")
    try:
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("INSERT INTO series (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)",
                ( nome,id_serie , id_prof))
        conexao.commit()
    finally:
        conexao.close()

#O banco não fecha pq se der erro na linha 6 o conexao.close não fecha 
        
nome = input("Digite o nome do aluno: ") 
id_serie = int(input("Digite o id da serie: "))
id_prof = int(input("Digite o id do professor: "))
print("Aluno cadastrado! ")
cadastrar_turma(nome, id_serie, id_prof)