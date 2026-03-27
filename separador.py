numeros = [5,10,20,50,60,75,80,15,90,100]
numeros_par = []
numeros_impar = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_par.append (numero)
    elif numero % 2 != 0:
        numeros_impar.append (numero)

print (f"Lista atualizada: {numeros_impar} numeros impar")
print(f"Lista atualizada: {numeros_par} numeros pares")        
