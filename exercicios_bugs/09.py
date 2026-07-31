import sqlite3

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    cursor.execute("UPDATE alunos SET nome = ? WHERE  id = ?", (novo_nome, id_aluno)) 
    conexao.commit()    
    conexao.close()

id_aluno = int(input("Digite o id: "))
novo_nome = input("Digite o novo nome: ") 
print("Nome atualizado! ")   


#Faltava colocar o where e adiciona os input para coloca o novo nome