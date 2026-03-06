codigo = int(input("Digite o codigo do drone "))
autorização = input("Possui autorização? ")

if codigo == 999 or autorização == "sim":

    nivel = int(input("Qual o nivél de bateria? "))
    clima = input("O clima está ensolarado ou chuvoso? ")
    vento = int(input("Velocidade do vento: "))
    if nivel < 10:
        print("Pouso autorizado")
    elif (nivel >=10 and clima == "ensolarado" and vento <30) or (clima == "chuvoso" and vento <10):
        print("POUSO AUTORIZADO: Iniciando descida") 
    else:
       print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita.") 

else:
    print(" ERRO 01:Drone não identificado. Retornando à base")       
