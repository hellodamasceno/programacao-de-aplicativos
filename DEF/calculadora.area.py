tentativas_usuario = 0
largura_area = int(input("Digite a largura da area: "))
comprimento_area  = int(input("Digite o comprimento da area: "))

def calcular_area(largura, comprimento, tentativas ):
    while tentativas != 3:
        multiplicação = largura * comprimento
        print(f"Area calculada:  {multiplicação}") 
        largura = int(input("Digite a largura da area: "))
        comprimento = int(input("Digite o comprimento da area: "))
        tentativas +=1

calcular_area(largura_area, comprimento_area, tentativas_usuario)