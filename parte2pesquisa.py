def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_situacao(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"


# Testes da função calcular_media
assert calcular_media(8, 6) == 7
assert calcular_media(10, 10) == 10
assert calcular_media(0, 0) == 0

# Testes da função verificar_situacao
assert verificar_situacao(7) == "Aprovado"
assert verificar_situacao(6) == "Aprovado"
assert verificar_situacao(5.9) == "Reprovado"

print("Todos os testes passaram!")


# O que acontece quando todos os testes passam? O programa continua a execução normalmente e imprime:
# "Todos os testes passaram!"
#Qual teste verifica o valor mínimo para aprovação? "assert verificar_situacao(6) == "Aprovado""
#Por que testar a nota 5.9 é importante? Porque 5.9 está logo abaixo do limite de 6. O teste confirma que médias menores que 6 são corretamente classificadas como "Reprovado".


def eh_par(numero):
    if numero % 2 == 0:
        return "par"
    return "impar"    


def calcular_desconto(preco, desconto):
    valor_desconto = preco * (desconto / 100)
    preco_final = preco - valor_desconto
    return preco_final



def pode_votar(idade):
    if idade >= 16:
        return "Pode votar"
    return "Não pode votar"


assert eh_par (2) == "par"
assert eh_par(7) == "impar"
assert eh_par(10) == "par"

assert calcular_desconto(100, 20) == 80
assert calcular_desconto(200, 10) == 180
assert calcular_desconto(50, 50) == 25

assert pode_votar(16) == "Pode votar"
assert pode_votar(15) == "Não pode votar"
assert pode_votar(25) == "Pode votar"