vida_atual = 100
dano = int(input("Digite o dano inicial: "))
def sofrer_dano(vida, dano):
    while vida > 0:
        if dano > vida:
            vida -= dano
            print("Vida atual ", vida)
        dano = input("Digite o novo dano: ")

sofrer_dano(vida_atual,dano  )        


