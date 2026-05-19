open ("Habitos.txt" , 'w'). close()

def adicionar_habito():
    habito = input("Digite o novo hábito: ")

    # Modo 'a' -> adiciona ao final do arquivo
    with open("Habitos.txt", 'a', encoding="utf-8") as arquivo:
        arquivo.write(habito + "\n")

    print("Hábito cadastrado com sucesso!\n")


def ver_habitos():
    with open("Habitos.txt",  'r', encoding="utf-8") as arquivo:
        habitos = arquivo.readlines()

    if len(habitos) == 0:
            print("Nenhum hábito cadastrado.\n")
            return []

    print("\n--- LISTA DE HÁBITOS ---")
    for indice, habito in enumerate(habitos):
            # .strip() remove a quebra de linha
            print(f"{indice} - {habito.strip()}")

    print()
    return habitos

def editar():
    ver_habitos()
    editar_habito = input("Digite o habito que deseja alterar: ")
    novo_habito = input("Digite o novo habito: ")

    with open("Habitos.txt", 'r') as arquivo:
        linhas = arquivo.readlines()

    editar_habito = novo_habito + '\n'
    with open("Habitos.txt", 'w') as arquivo:
        arquivo.writelines(linhas)
        print("habito  atualizado! ")

def descartar():
    habitos = ver_habitos()
    if habitos:
        try:
            idx = int(input("Número para remover: "))
            habitos.pop(idx)
            print("Removido!")
        except (ValueError, IndexError):
            print("Índice inválido.")

while True:
    print("\n1. Cadastrar | 2. Revisar | 3. Ajustar | 4. Descartar | 5. Sair")
    op = input("Escolha: ")
    if op == "1": adicionar_habito()
    elif op == "2": ver_habitos()
    elif op == "3": editar()
    elif op == "4": descartar()
    elif op == "5": break
