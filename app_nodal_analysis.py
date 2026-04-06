import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Circuitos - Guia de Engenharia", layout="wide")

st.title("⚡ Análise de Supernó: Problema 3.3 (Sadiku)")
st.markdown("""
Esta ferramenta resolve o circuito usando **Análise Nodal**. 
O Supernó é formado pela fonte de tensão entre dois nós de não-referência.
""")

# --- BARRA LATERAL (INPUTS) ---
st.sidebar.header("🔧 Parâmetros do Circuito")

# Fontes de Tensão
v_fonte_1 = st.sidebar.number_input(
    "Fonte de Tensão Esquerda (V)", value=14.0, step=1.0)
v_superno = st.sidebar.number_input(
    "Fonte do Supernó (V)", value=6.0, step=1.0)

st.sidebar.divider()

# Resistores
r1 = st.sidebar.slider("Resistor R1 (4Ω)", 1, 50, 4)
r2 = st.sidebar.slider("Resistor R2 (3Ω)", 1, 50, 3)
r3 = st.sidebar.slider("Resistor R3 (2Ω)", 1, 50, 2)
r4 = st.sidebar.slider("Resistor R4 (6Ω)", 1, 50, 6)

# --- CÁLCULO (LÓGICA DE ENGENHARIA) ---
# g = 1/R (Condutância)
g1, g2, g3, g4 = 1/r1, 1/r2, 1/r3, 1/r4

# Equação do Supernó: v2 = v1 + v_superno
# Somatório de correntes saindo do Supernó:
# (v - v_fonte_1)*g1 + v*g2 + (v + v_superno)*g3 + (v + v_superno)*g4 = 0
# v * (g1 + g2 + g3 + g4) = v_fonte_1*g1 - v_superno*(g3 + g4)

v_resultado = (v_fonte_1 * g1 - v_superno * (g3 + g4)) / (g1 + g2 + g3 + g4)
v2 = v_resultado + v_superno
i_resultado = v2 / r3

# --- INTERFACE PRINCIPAL ---
# Ajustei a proporção para a imagem ter mais espaço
col1, col2 = st.columns([0.6, 0.8])

with col1:
    st.subheader("Esquema do Circuito")
    try:
        # Tenta carregar a imagem da pasta local
        st.image("images/nodal.png",
                 caption="Diagrama do Problema 3.3 (Sadiku)", use_container_width=True)
    except:
        # Caso você ainda não tenha salvo a imagem na pasta
        st.warning(
            "⚠️ Arquivo 'circuito.png' não encontrado na pasta do projeto.")
        st.info(
            "Dica: Salve a imagem do enunciado como 'circuito.png' para visualizá-la aqui.")

with col2:
    st.subheader("📊 Resultados")

    # Exibição das métricas
    st.metric(label="Tensão v", value=f"{v_resultado:.2f} V")
    st.metric(label="Corrente i", value=f"{i_resultado:.2f} A")

    with st.expander("Ver detalhes dos nós"):
        st.write(f"Nó v: **{v_resultado:.2f}V**")
        st.write(f"Nó v2: **{v2:.2f}V**")
