import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS escolas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_serie TEXT NOT NULL,
    id_escola INTEGER NOT NULL,
    FOREIGN KEY (id_escola) REFERENCES escolas(id)''')

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

#O codigo não funcionaria pq o foreign key e para fazer relacao entre uma tabela e outra em um banco de dados que não existe nada, porém e acessei o banco de dados que ja existe dados
# entao so funcionaria se existisse conteudo nas duas tabelas criada dentro do banco de dados.       