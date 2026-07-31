import sqlite3
def listar_alunos_e_turmas():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT alunos.nome, turmas.nome_turma"   
                    "FROM alunos INNER JOIN turmas" 
                    " ON turmas"
                    "ON alunos.id_turma = turmas.id_turma")   
    for linha in cursor.fetchall():
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}")
    conexao.commit()
    conexao.close()    


#Faltava coloca o "ON" que define como as tabelas deve ser relacionadas
#Faltava o conexao commit 