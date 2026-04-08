import math

# Parâmetros do Circuito
f = 60           # Frequência em Hz
R = 99           # Resistência em Ohms
L = 0.05         # Indutância em Henry
C = 0.0001       # Capacitância em Farad (100 uF)

# Cálculo das Reatâncias (Escalares)
omega = 2 * math.pi * f
xl = omega * L
xc = 1 / (omega * C)

# --- O Pulo do Gato: Transformando em Números Complexos ---
# Em Python, usamos a função complex(real, imag) ou a sintaxe direta com 'j'
z_r = complex(R, 0)
z_l = 1j * xl    # Reatância indutiva é +jXL
z_c = -1j * xc   # Reatância capacitiva é -jXC

# Impedância Total (Série)
z_total = z_r + z_l + z_c

print(f"--- Análise de Circuito RLC (f={f}Hz) ---")
print(f"Impedância Retangular: {z_total:.2f} Ω")

# Extraindo Módulo (Z) e Fase (Graus)
modulo = abs(z_total)
fase_rad = math.atan2(z_total.imag, z_total.real)
fase_deg = math.degrees(fase_rad)

print(f"Impedância Polar: {modulo:.2f} ∠ {fase_deg:.2f}° Ω")