nome_do_heroi = input("digite o nome do seu heroí: ")
poder_de_ataque = float (input("digite o seu poder de ataque: "))
pontos_de_defesa = float (input("digite seu pontos de defesa: "))

subtraçao = poder_de_ataque - pontos_de_defesa 

if subtraçao <= 0 :
    print("O vilão bloqueou o ataque! Dano: 0")
elif subtraçao > 0:
    print("Ataque crítico! Você causou dano ao vilão de " , subtraçao)

