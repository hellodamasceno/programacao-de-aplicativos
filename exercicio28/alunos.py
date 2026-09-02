import banco
import sqlite3

def cadastrar_aluno(nome, idade, id_turma):
    
    assert nome.strip() != "", "O nome do aluno não pode ser vazio."
    assert idade >= 3, "A idade mínima para matrícula é de 3 anos."
    assert id_turma > 0, "O ID da turma deve ser maior que zero."
    
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade, id_turma) VALUES (?, ?, ?);", (nome.strip(), idade, id_turma))
    conexao.commit()
    conexao.close()

def listar_alunos():
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos;")
    alunos = cursor.fetchall()
    conexao.close()
    return alunos

def alterar_aluno(id_aluno, novo_nome, nova_idade, novo_id_turma):
    assert id_aluno > 0, "ID do aluno inválido."
    assert novo_nome.strip() != "", "O novo nome não pode ser vazio."
    assert nova_idade >= 3, "A idade do aluno deve ser igual ou superior a 3 anos."
    assert novo_id_turma > 0, "O ID da turma deve ser maior que zero."
    
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE alunos SET nome = ?, idade = ?, id_turma = ? WHERE id = ?;", (novo_nome.strip(), nova_idade, novo_id_turma, id_aluno))
    conexao.commit()
    conexao.close()

def excluir_aluno(id_aluno):
    assert id_aluno > 0, "ID do aluno inválido."
    
    conexao = banco.conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = ?;", (id_aluno,))
    conexao.commit()
    conexao.close()
   
