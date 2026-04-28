minha_lista_fruta = ["maçã", "banana", "uva", "pera", "laranja"]
minha_lista_ferramenta = ["martelo", "Parafuso", "Prego"]



def esta_na_lista(nome, lista):
    if nome in lista:
        print("Encontrado")
    else:
        print("Não disponivél")    
nome = input ("Digite o nome: ")
lista = input ("Digite a lista: ")
if lista == "frutas":
    lista = minha_lista_fruta
elif lista == "Ferramentas":
    lista = minha_lista_ferramenta
esta_na_lista(nome,lista)
