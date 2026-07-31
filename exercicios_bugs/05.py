import sqlite3
def vincular_aluno_turma():
    nome = input("nome do aluno: ")
    conexao = None
    try:
        id_turma = int(input("Digite o ID numerico da turma: "))
        
        conexao = sqlite3.connect('escola_demonstracao.db') 
        cursor = conexao.cursor () 
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", 
                   (nome, id_turma))
        conexao.commit()
    except ValueError:
        print("Erro! digite apenas numeros ")
    except sqlite3.Error:
        print("Erro no banco de dados! ")
    finally:
         if conexao is not None:
            conexao.close()
vincular_aluno_turma()
#não fiz o conexao.cursor e se não fizer não cria o cursor     
# precisava fazer o valueerror para não quebrar 
#O None nA CONEXAO E PARA EVITAR Q ELA QUEBRE SE NÃO EXISTIR
  