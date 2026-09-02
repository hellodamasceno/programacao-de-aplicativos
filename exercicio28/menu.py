import banco
import escola
import exercicio28.turma as turma
import aluno
import sqlite3


banco.inicializar_banco()

def exibir_menu():
    print("\n========= SISTEMA DE GESTÃO ESCOLAR =========")
    print("1. Cadastrar Escola      2. Listar Escolas      3. Alterar Escola      4. Excluir Escola")
    print("5. Cadastrar Turma       6. Listar Turmas       7. Alterar Turma       8. Excluir Turma")
    print("9. Cadastrar Aluno      10. Listar Alunos      11. Alterar Aluno      12. Excluir Aluno")
    print("0. Sair do Sistema")
    print("=============================================")

while True:
    exibir_menu()
    opcao = input("Selecione uma opção: ")
    
    if opcao == "0":
        print("\nEncerrando o sistema. Até mais!")
        break
        
    try:
    
        if opcao == "1":
            nome = input("Nome da Escola: ")
            cidade = input("Cidade: ")
            escola.cadastrar_escola(nome, cidade)
            print("✔️ Escola cadastrada com sucesso!")
            
        elif opcao == "2":
            escolas = escola.listar_escolas()
            print("\n--- LISTA DE ESCOLAS ---")
            for esc in escolas:
                print(f"ID: {esc[0]} | Nome: {esc[1]} | Cidade: {esc[2]}")
                
        elif opcao == "3":
            id_esc = int(input("ID da Escola que deseja alterar: "))
            nome = input("Novo Nome da Escola: ")
            cidade = input("Nova Cidade: ")
            if escola.alterar_escola(id_esc, nome, cidade):
                print(" Escola alterada com sucesso!")
            else:
                print(" Escola não encontrada.")
                
        elif opcao == "4":
            id_esc = int(input("ID da Escola que deseja excluir: "))
            if escola.excluir_escola(id_esc):
                print(" Escola removida com sucesso!")
            else:
                print(" Escola não encontrada.")

        
        elif opcao == "5":
            nome_t = input("Nome da Turma: ")
            id_esc = int(input("ID da Escola Vinculada: "))
            turma.cadastrar_turma(nome_t, id_esc)
            print(" Turma vinculada e cadastrada com sucesso!")
            
        elif opcao == "6":
            turmas = turma.listar_turmas()
            print("\n--- LISTA DE TURMAS ---")
            for tur in turmas:
                print(f"ID: {tur[0]} | Turma: {tur[1]} | ID Escola Pai: {tur[2]}")
                
        elif opcao == "7":
            id_tur = int(input("ID da Turma que deseja alterar: "))
            nome_t = input("Novo Nome da Turma: ")
            id_esc = int(input("Novo ID da Escola Vinculada: "))
            if turma.alterar_turma(id_tur, nome_t, id_esc):
                print(" Turma alterada com sucesso!")
            else:
                print(" Turma não encontrada.")
                
        elif opcao == "8":
            id_tur = int(input("ID da Turma que deseja excluir: "))
            if turma.excluir_turma(id_tur):
                print(" Turma removida com sucesso!")
            else:
                print(" Turma não encontrada.")

        
        elif opcao == "9":
            nome_a = input("Nome do Aluno: ")
            idade = int(input("Idade do Aluno: "))
            id_tur = int(input("ID da Turma Vinculada: "))
            aluno.cadastrar_aluno(nome_a, idade, id_tur)
            print(" Aluno matriculado e cadastrada com sucesso!")
            
        elif opcao == "10":
            alunos = aluno.listar_alunos()
            print("\n--- LISTA DE ALUNOS ---")
            for alu in alunos:
                print(f"ID: {alu[0]} | Nome: {alu[1]} | Idade: {alu[2]} anos | ID Turma: {alu[3]}")
                
        elif opcao == "11":
            id_alu = int(input("ID do Aluno que deseja alterar: "))
            nome_a = input("Novo Nome do Aluno: ")
            idade = int(input("Nova Idade: "))
            id_tur = int(input("Novo ID da Turma Vinculada: "))
            if aluno.alterar_aluno(id_alu, nome_a, idade, id_tur):
                print(" Ficha do aluno alterada com sucesso!")
            else:
                print(" Aluno não encontrado.")
                
        elif opcao == "12":
            id_alu = int(input("ID do Aluno que deseja excluir: "))
            if aluno.excluir_aluno(id_alu):
                print(" Aluno removido do sistema.")
            else:
                print(" Aluno não encontrado.")
                
        else:
            print("⚠️ Opção Inválida! Digite um número correspondente do menu.")

    except ValueError:
        print("\n ERRO DE DIGITAÇÃO: Você inseriu letras em um campo que exigia apenas números (como ID ou Idade). Tente novamente.")
        
    except AssertionError as erro_validacao:
        print(f"\n VALIDAÇÃO NEGADA: {erro_validacao}")
        
    except sqlite3.IntegrityError:
        print("\n ERRO DE INTEGRIDADE RELACIONAL: O ID da tabela pai informado não existe no banco de dados. Cadastre a entidade pai primeiro.")
        
    except sqlite3.Error as erro_banco:
        print(f"\n ERRO CRÍTICO NO BANCO DE DADOS: {erro_banco}")
