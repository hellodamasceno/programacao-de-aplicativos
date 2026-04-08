compras = []
produto = ""

while produto !=  "sair":
    produto = input("Digite o nome do produto: ")
    if produto != "sair":
        compras.append(produto)
    print(f"Lista: {compras}" )

