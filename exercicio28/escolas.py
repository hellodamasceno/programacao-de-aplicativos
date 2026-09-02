import banco
import sqlite3

def cadastrar_escola(nome, cidade):
    
    assert nome.strip() != "", "O nome da escola não pode ser vazio."
    assert cidade.strip() != "", "A cidade da escola não pode ser vazia."
    
    conn = banco.conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO escolas (nome, cidade) VALUES (?, ?);", (nome.strip(), cidade.strip()))
    conn.commit()
    conn.close()

def listar_escolas():
    conn = banco.conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM escolas;")
    escolas = cursor.fetchall()
    conn.close()
    return escolas

def alterar_escola(id_escola, novo_nome, nova_cidade):
    assert id_escola > 0, "ID da escola inválido."
    assert novo_nome.strip() != "", "O novo nome não pode ser vazio."
    assert nova_cidade.strip() != "", "A nova cidade não pode ser vazia."
    
    conn = banco.conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE escolas SET nome = ?, cidade = ? WHERE id = ?;", (novo_nome.strip(), nova_cidade.strip(), id_escola))
    linhas_afetadas = cursor.rowcount
    conn.commit()
    conn.close()
    return linhas_afetadas > 0

def excluir_escola(id_escola):
    assert id_escola > 0, "ID da escola inválido."
    
    conn = banco.conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM escolas WHERE id = ?;", (id_escola,))
    linhas_afetadas = cursor.rowcount
    conn.commit()
    conn.close()
    return linhas_afetadas > 0
