def pode_votar(idade):
    return idade >= 16
def executar_painel_de_testes():
    print("=== PAINEL DE DISCUSSÃO: TESTES FORTES VS. REPETIDOS ===")
    print("\n[EXEMPLO BASE DO PROFESSOR]")
    print(f"pode_votar(15) -> Esperado: False | Obtido: {pode_votar(15)} (Fronteira inferior)")
    print(f"pode_votar(16) -> Esperado: True  | Obtido: {pode_votar(16)} (Fronteira exata)")
executar_painel_de_testes()