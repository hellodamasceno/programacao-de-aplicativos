import json
import os

sistema_JSON = "alunos.json"

def carregar_dados():
    if not os.path.exists(sistema_JSON):
        return []

def cadastrar_aluno():
    if os.path.exists(sistema_JSON):
        id_aluno = int(input("Digite o ID: "))
        aluno= { 
            "ID" : id_aluno,
            "nome":input("Digite o nome do Aluno: "),
            "Telefone" :int(input("Digite o telefone: ")),
            "Turma" :input("Digite a turma: "),
            "Idade": int(input("Digite a idade do aluno: ")),
            "CPF": input("Digite o CPF do aluno: "),
        }
        with open(sistema_JSON, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        for dado in dados:
            if dado["id"] == id_aluno:
                print("ID já possui cadastro! ")
            else:
                dados.append(aluno)
                with open(sistema_JSON, 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, indent=4)
                print("Aluno cadastrado! ")    