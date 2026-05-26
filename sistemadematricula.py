import json
import os

sistema_JSON = "alunos.json"

def cadastrar_aluno():
    if os.path.exists(sistema_JSON):
        with open(sistema_JSON, 'r', encoding='utf-8') as arquivo: 
            alunos = json.load(arquivo) 
    else: 
        alunos = []
    
    id_aluno = int(input("Digite o ID: "))
    aluno= { 
        "ID" : id_aluno,
        "nome":input("Digite o nome do Aluno: "),
        "Telefone" :int(input("Digite o telefone: ")),
        "Turma" :input("Digite a turma: "),
        "Idade": int(input("Digite a idade do aluno: ")),
        "CPF": input("Digite o CPF do aluno: ")
    }

    if len(alunos) !=0:
        for dado in alunos:
            if dado["ID"] == id_aluno:
                print("ID já possui cadastro! ")
                return

    alunos.append(aluno)

    with open(sistema_JSON, 'w', encoding='utf-8') as arquivo:
        json.dump(alunos, arquivo, indent=4)
        
    print("Aluno cadastrado! ")    


def listar():
    print("-----Lista de alunos------")
    if os.path.exists(sistema_JSON):
        with open(sistema_JSON, 'r', encoding='utf-8') as arquivo:
            alunos= json.load(arquivo)
    else:
        alunos = []        
    if not alunos:
        print("Aluno não cadastrado")
        return
    for aluno in alunos:  
        print(f"Nome: {aluno['nome']} | CPF: {aluno['CPF']} | Turma: {aluno['Turma']} | Tel: {aluno['Telefone']}")


def atualizar():
    if not os.path.exists(sistema_JSON):
        print("ARQUIVO VAZIO! ")
        return 
    with open(sistema_JSON, 'r', encoding='utf-8') as arquivo: 
            alunos = json.load(arquivo) 
    nome_alterar= int(input("Digite o nome do aluno que deseja editar: ")) 
    for aluno in alunos: 
        if aluno['nome'] == nome_alterar: 
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] 
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
              
        with open(sistema_JSON, 'w', encoding='utf-8') as arquivo: 
            json.dump(alunos, arquivo, indent=4, ensure_ascii=False) 
        print("Dados atualizados com sucesso!") 

def excluir(): 
    print("\n--- Excluir Aluno ---")  
    if not os.path.exists(sistema_JSON): 
        print("Nenhum aluno cadastrado no sistema.") 
        return        
    with open(sistema_JSON, 'r', encoding='utf-8') as  arquivo:
        alunos = json.load(arquivo) 
        
    nome_busca = int(input("Digite o nome do aluno que deseja remover: ")) 
    
    nova_lista = [a for a in alunos if a['id'] != nome_busca] 
    if len(nova_lista) < len(alunos): 
        with open(sistema_JSON, 'w', encoding='utf-8') as arquivo: 
            json.dump(nova_lista, arquivo, indent=4, ensure_ascii=False) 
        print("Aluno removido com sucesso!") 
    else: 
        print("Aluno não encontrado.") 
def menu(): 
    if not os.path.exists(sistema_JSON): 
        with open(sistema_JSON, 'w', encoding='utf-8') as arquivo:
            json.dump([], arquivo)


    while True:
        print("\n=== SISTEMA DE MATRICULA ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        opcao = input("Escolha uma opção: ") 
        
        if opcao == '1': cadastrar_aluno()  
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()    
    
        