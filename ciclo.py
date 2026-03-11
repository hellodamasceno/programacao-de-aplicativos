numero_total = int(input("Qual o numero de garrafas que passaram pela esteira hoje? "))

if numero == 500:
    print ("HORA DA LIMPEZA: Parar máquina imediatamente!")
    print("QUALIDADE: Retirar amostra para teste.")

elif numero_total % 500 == 0:
    print ("HORA DA LIMPEZA: Parar máquina imediatamente!")
elif numero_total % 100 == 0:
    print ("QUALIDADE: Retirar amostra para teste.")

else:
    print (f": Produção em dia. Garrafa número{ numero_total} processada.")
