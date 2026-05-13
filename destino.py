open ("viagens.txt", 'w') . close ()

def adicionar ():
    lugar = input("Sugere um lugar: ")
    with open("viagens.txt", 'a') as arquivo:
        arquivo.write(lugar + '\n')
        print("Lugar adicionado! ")


def ler():
    with open ("viagens.txt", 'r') as arquivo:
        viagens = arquivo.readlines()

    soma = 0
    for viagem in viagens:
        print(f"{soma} - {viagem.strip()}")
        soma += 1

def editar():
    ler()
    editar_destino = input("Digite o destino que deseja alterar: ")
    novo_destino = input("Digite o novo destino: ")

    with open("viagens.txt", 'r') as arquivo:
        linhas = arquivo.readlines()

    editar_destino = novo_destino + '\n'
    with open("viagens.txt", 'w') as arquivo:
        arquivo.writelines(linhas)
        print("lugar atualizado atualizado! ")

def deletar():
    ler()
    destino = input("Digite o nome do destino que deseja excluir: ")
    with open("viagens.txt", 'r') as arquivo:
        linhas = arquivo.readlines()
    del linhas[destino]
    with open("viagens.txt", 'w') as arquivo:
        arquivo.writelines(linhas)
        print("Aluno removido! ")

while True:
    print("------PLANEJADOR DE VIAGENS--------")
    print(" 1-Cadastrar | 2-Ler | 3-Editar |4-Deletar | 5-Encerrar sessão") 
    opcao = input("Digite a opção desejada: ")
    if opcao == '1': adicionar()
    elif  opcao == '2': ler()
    elif opcao == '3': editar()
    elif opcao == '4': deletar()
    else:
        print("Saindo do programa! ")