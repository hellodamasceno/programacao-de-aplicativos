def busca_repetida(lista, valor):
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador +=1
    return contador
        
lista = [2,10,8,2,96,2,3,2]
print(busca_repetida(lista, 2))        