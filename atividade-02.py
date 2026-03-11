id = int(input(" ID do funcionario: "))
temperatura = float(input("Temperatura da máquina : "))
tempo_uso = float(input("Tempo de uso: "))

if (id  % 3 == 0) and (temperatura > 40 or tempo_uso > 8):
    print(f"Funcionário {id}, você foi escalado para a manutenção preventiva hoje.")

else:
    print(f"Funcionário {id}, sua máquina opera dentro dos padrões normais.")    