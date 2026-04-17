import streamlit as st
import os
import sys
import subprocess
import webbrowser
import socket

# --- BLOCO DE AUTO-EXECUÇÃO INTELIGENTE ---
def is_port_open(port):
    """Verifica se o servidor Streamlit já está rodando na porta padrão."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if __name__ == "__main__":
    if not st.runtime.exists():
        porta = 8501
        if is_port_open(porta):
            # Se já está rodando, apenas abre o navegador de novo
            webbrowser.open(f"http://localhost:{porta}")
        else:
            # Se não está rodando, inicia o processo
            # --server.headless=true impede que o Streamlit tente abrir o navegador sozinho (nós faremos isso)
            subprocess.Popen(["streamlit", "run", sys.argv[0], "--server.port", str(porta), "--server.headless", "true"])
            time_wait = 0
            while not is_port_open(porta) and time_wait < 5:
                import time
                time.sleep(0.5)
                time_wait += 0.5
            webbrowser.open(f"http://localhost:{porta}")
        sys.exit()
# ------------------------------------------

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Calculadora de Circuitos", layout="wide", page_icon="⚡")

# 2. INTERFACE
st.title("⚡ Análise de Supernó: Problema 3.3 (Sadiku)")

# --- BARRA LATERAL ---
st.sidebar.header("🔧 Parâmetros")
v_fonte_1 = st.sidebar.number_input("Fonte Esquerda (V)", value=14.0)
v_superno = st.sidebar.number_input("Fonte Supernó (V)", value=6.0)

with st.sidebar.expander("Resistores (Ω)", expanded=True):
    r1 = st.slider("R1", 1, 50, 4)
    r2 = st.slider("R2", 1, 50, 3)
    r3 = st.slider("R3", 1, 50, 2)
    r4 = st.slider("R4", 1, 50, 6)

# 3. CÁLCULOS
g1, g2, g3, g4 = 1/r1, 1/r2, 1/r3, 1/r4
v_resultado = (v_fonte_1 * g1 - v_superno * (g3 + g4)) / (g1 + g2 + g3 + g4)
v2 = v_resultado + v_superno
i_resultado = v2 / r3

# 4. LAYOUT PRINCIPAL
col1, col2 = st.columns([0.6, 0.4])

with col1:
    st.subheader("🖼️ Esquema")
    caminho_imagem = r"C:\PythonCodes\Codes 2026\images\nodal.png"
    if os.path.exists(caminho_imagem):
        st.image(caminho_imagem, width="stretch")
    else:
        st.error(f"Imagem não encontrada em: {caminho_imagem}")

with col2:
    st.subheader("📊 Resultados")
    st.metric("Tensão v1", f"{v_resultado:.2f} V")
    st.metric("Corrente i", f"{i_resultado:.2f} A")
    
    with st.expander("Detalhes Técnicos"):
        st.write(f"V1: {v_resultado:.3f}V | V2: {v2:.3f}V")