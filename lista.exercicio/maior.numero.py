numeros = [20, 10, 50, 70, 100]
valor_maximo = 0
print(f"Valores originais {numeros}")

for numero in numeros:
    if numero > valor_maximo:
        valor_maximo = numero 
        print(f"Valores trocados: {numero}")

