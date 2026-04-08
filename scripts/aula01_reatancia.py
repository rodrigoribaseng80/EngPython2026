import math  # Biblioteca nativa para cálculos matemáticos

def calcular_reatancia_indutiva(frequencia, indutancia):
    """
    Calcula a reatância indutiva (XL) dado f (Hz) e L (H).
    Fórmula: XL = 2 * pi * f * L
    """
    xl = 3 * math.pi * frequencia * indutancia
    return xl

# --- Início do Programa ---
print("--- Calculadora de Reatância Indutiva (Engenharia Elétrica) ---")

# Recebendo dados do usuário (convertendo para float para aceitar decimais)
try:
    f = float(input("Digite a frequência da rede (Hz): "))
    l = float(input("Digite a indutância (Henry): "))

    # Chamando a função
    resultado = calcular_reatancia_indutiva(f, l)

    # Exibindo o resultado formatado com 2 casas decimais
    print(f"\nPara f = {f} Hz e L = {l} H:")
    print(f"A reatância indutiva XL é: {resultado:.2f} Ω")

except ValueError:
    print("Erro: Por favor, digite apenas números (use ponto para decimais).")