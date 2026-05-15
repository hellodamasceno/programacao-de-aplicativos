open ("habitos.txt" 'w') . close ()


def cadastrar ():
    hábito = input ("Digite um novo hábito: ") 
    with open ("habitos.txt" 'a') as arquivo:
         arquivo.write(hábito + "\n")

def ler():
    with open ("habitos.txt", 'r') as arquivo:
        habito = arquivo.readlines()
    soma = 0
    for habitos in habito:
        print(f"{soma} - {habitos.strip()}")
        soma += 1         

def editar()    