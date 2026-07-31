
import sqlite3 
 
def cadastrar_escola_manual():  
    id_escola = int(input("Digite o ID para a nova escola: ")) 
    nome = input("Nome da escola: ") 
            
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor()   
    try:
        cursor.execute(
            "INSERT INTO escolas (id, nome) VALUES (?, ?)", 
            (id_escola, nome)
        )
        conexao.commit()
        print("Escola cadastrada com sucesso!")
        
    except sqlite3.IntegrityError:
        print(f"Erro: O ID {id_escola} já está cadastrado no sistema.")
        
    finally:
        conexao.close()
        #Com o sqlite3.IntegrityError detecta o erro caso o ID já exista evita erro no  programa