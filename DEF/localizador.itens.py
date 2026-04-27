def esta_na_lista(lista, nome_buscar):
    for item in lista:
        if item == nome_buscar:
            print("Encontrado")
        else:
            print("Não disponivél")    


minha_lista = ["maçã", "banana", "uva", "pera", "laranja"]

busca1 = "uva"
resultado1 = esta_na_lista(minha_lista, busca1)
print(f"Busca por '{busca1}': {resultado1}")


busca2 = "melancia"
resultado2 = esta_na_lista(minha_lista, busca2)
print(f"Busca por '{busca2}': {resultado2}")



esta_na_lista("lista", "nome_buscar" )
