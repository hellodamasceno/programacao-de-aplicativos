temeperatura = float(input("digite a temperatura atual: "))

if temeperatura <= 30:
    print("Alerta de Calor!")
    umidade = float(input(" Digite a umidade: "))
    if umidade <= 40:
        print ("Ação: Ligar Irrigação!")
    else:
           print("Ação: Ligar apenas ventiladores")