import sqlite3 
 
def cadastrar_escola_manual(): 
    try:
        id_escola = int(input("Digite o ID para a nova escola: ")) 
        nome = input("Nome da escola: ") 
            
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
                
        cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola, nome)) 
                
        conexao.commit() 
    except sqlite3.IntegrityError:
        print("AVISO: Esse ID já existe ")
    conexao.close() 
#com essa estrutura o proframa aprende a lidar com os erros do usuario