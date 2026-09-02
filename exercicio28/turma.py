import banco
import sqlite3

def cadastrar_turma(nome_turma, id_escola):
    
    assert nome_turma.strip() != "", "O nome da turma não pode ser vazio."
    assert id_escola > 0, "O ID da escola deve ser maior que zero."
    
    conn = banco.conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?);", (nome_turma.strip(), id_escola))
    conn.commit()
    conn.close()

def listar_turmas():
    conn = banco.conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM turmas;")
    turmas = cursor.fetchall()
    conn.close()
    return turmas

def alterar_turma(id_turma, novo_nome, novo_id_escola):
    assert id_turma > 0, "ID da turma inválido."
    assert novo_nome.strip() != "", "O novo nome da turma não pode ser vazio."
    assert novo_id_escola > 0, "O ID da escola deve ser maior que zero."
    
    conn = banco.conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE turmas SET nome_turma = ?, id_escola = ? WHERE id = ?;", (novo_nome.strip(), novo_id_escola, id_turma))
    linhas_afetadas = cursor.rowcount
    conn.commit()
    conn.close()
    return linhas_afetadas > 0

def excluir_turma(id_turma):
    assert id_turma > 0, "ID da turma inválido."
    
    conn = banco.conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM turmas WHERE id = ?;", (id_turma,))
    linhas_afetadas = cursor.rowcount
    conn.commit()
    conn.close()
    return linhas_afetadas > 0
