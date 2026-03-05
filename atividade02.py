seja_bem_vindo = input("Seja bem vindo, digite o seu nome: ")
curso = input(f"Olá {seja_bem_vindo}, você concluiu o curso de segurança? ")


if curso == "sim":
    instrutor = input ("O instrutor está presente na sala? ")
    if instrutor == "sim":
        print ("Acesso Liberado: Operação iniciada")
    else:
        print ("Aguarde o instrutor para ligar a máquina")

else:
    print ("Acesso Negado: Faça o treinamento primeiro")

