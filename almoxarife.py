print("Digite 1 para adicionar ")
print("Digite 2 para listar ")
print("Digite 3 para sair ")

lista = []

opçoes = input("Digite a opção desejada: ")


while opçoes != 3:
    opçoes = input("Digite a opção desejada: ")

if opçoes == "1":
    item = input("Digite o item que deseja adicionar: ")
    lista.append(item)
    print(lista)
    
elif opçoes == "2":
    item = input("Digite um item para listar: ")
    print(lista)

elif opçoes == "3":
    print ("Saindo do sistema...")