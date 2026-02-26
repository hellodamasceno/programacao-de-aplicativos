media = float(input ("informe sua media: "))
presença = int(input("infome sua presença: "))

if media >= 70 and presença >= 75 :
    print("Parabéns! Você foi aprovado ")
elif media < 70 and presença < 75 :
    print ("Reprovado. Verifique sua nota ou frequência")
    