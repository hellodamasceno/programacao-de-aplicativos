cargo_funcionario = input("digite seu cargo: ")
codigo_acesso = int(input("digite seu codigo de acesso: "))
botão_emergencia = input("Botão de emergência pressionado? ")
epi = input("EPI completo? ")


if (cargo_funcionario == "engenheiro" or cargo_funcionario == "tecnico") and (codigo_acesso == 1234 or botão_emergencia == "sim") and epi == "sim":
    print("Sistema liberado! ")

else:
    print("ACESSO NEGADO: RISCO DE SEGURANÇA")

