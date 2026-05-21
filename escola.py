import json


def criar_arquivo ():
     open ("escola.json", 'w').close()
1
def salvar_dados(dados):
     with open ("escola.json", 'w')as arquivo:
          json.dump(dados, arquivo, indent=4)


def cadastar_aluno (dados, cpf ):
    dados = listar_aluno()
    nome = input("Nome Completo: ")
    telefone = int(input("Telefone: "))
    turma = input("Turma: ")
    idade = input("Idade: ")
    cpf = int(input("Digite o CPF: "))
    dados = {
            "nome": nome,
            "telefone": telefone,
            "turma": turma,
            "idade": idade,
            "cpf": cpf,
        }
def listar_aluno():
     with open("escola.json", 'r') as arquivo:
        dados = json.load (arquivo)
print()


def atualizar_dados():
    with open("escola.json", 'r') as arquivo:
        dados = json.load(arquivo)
        dados['telefone'] =telefone = int(input("Digite o novo Telefone: "))
        dados['turma'] =turma = input("Digite a nova Turma: ")

def remover_aluno():
    with open("escola.json", 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    if 'cpf' in dados:
        del dados ['cpf']
        print("Campo 'cpf ' removido com sucesso!")
    with open("escola.json", 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


          

while True:
    print("------SEJA BEM VINDO AO SISTEMA-------") 
    print(" 1-Cadastrar | 2-Ler | 3-Atualizar |4-Deletar | 5-Encerrar sessão") 
    opcao = input("Digite a opção desejada: ")
    if opcao == '1': cadastar_aluno()
    elif  opcao == '2': listar_aluno()
    elif opcao == '3': atualizar_dados()
    elif opcao == '4': remover_aluno()
    else: break
         