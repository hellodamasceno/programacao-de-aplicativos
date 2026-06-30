import sqlite3
def buscar_professor(id_prof):
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM serie WHERE id=?", (id_prof,)) 
    resultado = cursor.fetchone() 
    print(resultado)
    conexao.close()
buscar_professor()   

#faltava a virgula na linha 5 depois de id_prof pq sem a virgula ele não entende como parametro