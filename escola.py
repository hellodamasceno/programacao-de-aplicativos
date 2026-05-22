import json # para carregar a biblioteca 
import os # para combater os erros 

BANCO_DADOS = 'alunos.json' # para armazenar o conteudo

def cadastrar():# para cadastar 
    print("\n--- Novo Cadastro ---") # para ficar esteticamente organizado no terminal
    
    if os.path.exists(BANCO_DADOS): # para verificar se o arquivo existe
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo e le o conteudo
            alunos = json.load(f) # le o arquivo no formato JSON
    else: # se não existe 
        alunos = [] # fica vazia a lista

    novo_aluno = { # cria as opções 
        "nome": input("Nome: "),# pede para o usuario digitar o nome
        "telefone": input("Telefone: "),# pede para o usuario digitar o telefone
        "turma": input("Turma: "),# pde para digitar a turma
        "idade": int(input("Idade: ")),# pede para o usuario digitar a idade
        "cpf": input("CPF: ")# pede para o usuario digitar o cpf
    }
    
    alunos.append(novo_aluno) #adiciona os dados na lista 

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # salva as informações
        json.dump(alunos, f, indent=4, ensure_ascii=False) #para salvar a informação na formatação JSON
        
    print("Aluno cadastrado com sucesso!") # mensagem que aparece no terminal após o cadastro

def listar(): # para listar os dados cadastrados
    print("\n--- Lista de Alunos ---") # para ficar esteticamente organizado no terminal
    
    if os.path.exists(BANCO_DADOS): # carrega o arquivo apenas se existir
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo no modo leitura
            alunos = json.load(f) # le todo o arquivo JSON
    else: # se não existe 
        alunos = [] #  a lista fica vazia 

    if not alunos: # se não existe nada 
        print("Nenhum aluno cadastrado.")# aparece essa mensagem no terminal
        return# para encerrar a função

    for aluno in alunos: # percorre a lista 
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")
# aparece organizado e esteticamente bonito no terminal
def atualizar():# para atualizar o cadastro
    print("\n--- Atualizar Aluno ---")# para ficar esteticamente organizado no terminal
    if not os.path.exists(BANCO_DADOS):# verifica se existe algo dentro do arquivo
        print("Nenhum aluno cadastrado no sistema.")# para dizer que não existe nada, aparece no terminal
        return # encerra a função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo no modo leitura
        alunos = json.load(f) # le o arquivo no formato JSON
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) # pede um valor variavél 
    
    for aluno in alunos: # percorre a lista
        if aluno['cpf'] == cpf_busca: # verifica se ja existe para pode editar
            print(f"Editando dados de: {aluno['nome']}")# informa que esta editando os dados
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # permite atualizar o nome mais se apertar enter continua a mesma coisa 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] #permite atualizar o nome mais se apertar enter continua a mesma coisa
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] #permite atualizar o nome mais se apertar enter continua a mesma coisa
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])#permite atualizar o nome mais se apertar enter continua a mesma coisa
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']#permite atualizar o nome mais se apertar enter continua a mesma coisa
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # abre o arquivo no modo leitura
                json.dump(alunos, f, indent=4, ensure_ascii=False) # salva as informação
            print("Dados atualizados com sucesso!") # aparece no terminal de forma organizada 
            return # encerra a função
            
    print("Aluno não encontrado.") # para aparecer no terminar de forma organizada e bonita

def excluir(): # para fazer exclusão de algo do arquivo
    print("\n--- Excluir Aluno ---") # para aparecer organizado no terminar e o \n serve para quebrar a linha
    if not os.path.exists(BANCO_DADOS): # verifica se existe algo no arquivo
        print("Nenhum aluno cadastrado no sistema.") # para ficar bonito no terminal
        return # encerra a função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo no modo leitura 
        alunos = json.load(f) # le o formato no modo JSON
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: ")) #da a opçao para digitar o id que você quer excluir do arquivo
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] # ercorre a lista e verifica se o id é diferente do id buscado
    
    if len(nova_lista) < len(alunos): # para ver o tamanho da lista
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # abre o arquivo no modo leitura
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # salva as informações no formato JSON
        print("Aluno removido com sucesso!") # para ficar esteticamente bonito e organizado
    else: # se não existe
        print("Aluno não encontrado.") # aparece a mensagem no terminal
def menu(): # definir uma função
    if not os.path.exists(BANCO_DADOS): #verifica se existe algo dentro do arquivo
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:# abre o arquivo no mode de escrever/transcrever
            json.dump([], f) # adiciona o valor a lista

    while True: # rodar enquanto for verdadeiro
        print("\n=== SISTEMA ESCOLAR ===")# aparece as opçoes no terminal
        print("1. Cadastrar Aluno")# aparece as opçoes no terminal
        print("2. Listar Alunos")# aparece as opçoes no terminal
        print("3. Atualizar Aluno")# aparece as opçoes no terminal
        print("4. Excluir Aluno")# aparece as opçoes no terminal
        print("5. Sair")# aparece as opçoes no terminal
        
        opcao = input("Escolha uma opção: ")# para o usuario escolher as opções 
        
        if opcao == '1': cadastrar() # verifica oq o usuario escolheu e chama a função 
        elif opcao == '2': listar()# verifica oq o usuario escolheu e chama a função 
        elif opcao == '3': atualizar()# verifica oq o usuario escolheu e chama a função 
        elif opcao == '4': excluir()# verifica oq o usuario escolheu e chama a função 
        elif opcao == '5': break# verifica oq o usuario escolheu e para de rodar o codigo
        else: print("Opção inválida!")# aparece no terminal para encerrar o programa

menu() # chama a função