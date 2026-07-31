import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()
conexao.execute("PRAGMA foreign_keys = ON")
cursor.execute("""
CREATE TABLE IF NOT EXISTS series (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_serie TEXT NOT NULL,
    id_escola INTEGER NOT NULL,
    FOREIGN KEY (id_escola) REFERENCES escolas(id)
)
""")
conexao.commit()
conexao.close()
#CRIAR A TABELA SERIES PARA SALVAR 

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()
conexao.execute("PRAGMA foreign_keys = ON")
cursor.execute("""
CREATE TABLE IF NOT EXISTS escolas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_serie TEXT NOT NULL,
    id_escola INTEGER NOT NULL,
    FOREIGN KEY (id_escola) REFERENCES escolas(id)
)
""")
conexao.commit()
conexao.close()
#CRIAR A TABELA ESCOLAS PARA SALVAR

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('escola_demonstracao.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?,? )",
                       (nome_serie, id_escola))
        conexao.commit()    
    except sqlite3.IntegrityError:
      print("ERRO: escola inexistente")
    finally:
       conexao.close()  
cadastrar_serie("6º Ano", 999)

#primeiro erro é pq eu não tenho uma tabela criada para "series" e nem para "escola"
# faltava o conexao.execute com o PRAGMA