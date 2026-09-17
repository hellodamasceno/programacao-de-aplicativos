def busca_sequencial(vetor,valor):
    for i in range(len(vetor)):
        if vetor [i] == valor:
            return i
    return -1 

vetor = [10,20,56,49,85,3,1,87]
resultado = busca_sequencial(vetor,49)
print(resultado)