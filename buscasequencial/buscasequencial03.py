def maior_numero(lista):
    maior = lista[0]
    posicao = 0
    for i in range(1, len(lista)):
        if lista[i] > maior:
            posicao = i
    return maior, posicao

lista = [25,10,56,97,3,21]
maior, posicao = maior_numero(lista)

print("Maior numero: ", maior)
print("Posição: ", posicao)