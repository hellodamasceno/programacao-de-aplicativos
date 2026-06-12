#ALTERAR CPF E NOME
import sqlite3 

# conexao = sqlite3.connect('escola_demonstracao.db')
# cursor = conexao.cursor()

# cpf_atual = input("Digite o CPF atual: ")

# comando_buscar = f'''
#                 SELECT * FROM escola_demonstracao
#                 where cpf = '{cpf_atual}' '''
# cursor.execute (comando_buscar)
# aluno = cursor.fetchone()

# if aluno:
#     print("Aluno encontrado")
#     print(aluno)
#     novo_nome = input("Digite o novo nome: ")    
#     novo_cpf = input("Digite o novo CPF: ")
#     comando_atualizar = (f''' UPDATE escola_demonstracao
#                         SET nome = '{novo_nome}',
#                         cpf = '{novo_cpf}' WHERE cpf= '{cpf_atual}' ''')


#     cursor.execute(comando_atualizar)
#     conexao.commit()
#     print ("Aluno atualizado")

# else:
#     print("aluno não encontrado") 

# cursor.execute("SELECT * FROM escola_demonstracao")

# for aluno in cursor.fetchall():
#     print(aluno)

# conexao.close()       


#EXCLUIR 

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()
cursor.execute("SELECT * FROM escola_demonstracao")
print("Alunos cadastrados")

for aluno in cursor.fetchall():
    print(aluno)
id_aluno = int(input("Digite o ID do aluno: "))
comando_excluir = (f''' DELETE FROM escola_demonstracao
                   WHERE id = {id_aluno}''') 
cursor.execute(comando_excluir)
conexao.commit 
print("Lista atualizada" )  
cursor.execute ("SELECT * FROM escola_demonstracao")
for aluno in cursor.fetchall():
    print(aluno)
conexao.close       