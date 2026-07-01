import sqlite3
def deletar_escola_antiga():
    id_escola = int(input("Digite o id da escola para remover: "))
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM escolas WHERE id=?" , (id_escola,))

    conexao.commit() 
    conexao.close()
#Faltava colocar o id=? assim define o que é para apagar