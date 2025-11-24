import streamlit as st
import pandas as pd
from matrix_logic import get_matrix, get_value

st.set_page_config(page_title="Matrice Performance/Comportamento", layout="centered")

st.image("http://www.covi-electric.com/images/yootheme/Logo-COVI.png", width=220)

st.title("Matrice Performance / Comportamento")

st.write("Inserisci i valori da 1 a 5 per Performance (X) e Comportamento (Y).")

col1, col2 = st.columns(2)

with col1:
    x = st.number_input("Performance (X)", min_value=1, max_value=5, step=1, value=3)

with col2:
    y = st.number_input("Comportamento (Y)", min_value=1, max_value=5, step=1, value=3)

matrix = get_matrix()
result_value = get_value(x, y)

st.subheader(f"Risultato = {result_value}")

df = pd.DataFrame(matrix)

color_map = {
    1:  "#7A0000",
    2:  "#C00000",
    3:  "#E36C6C",
    4:  "#FFC000",
    5:  "#FFF2CC",
    6:  "#C00000",
    7:  "#C0504D",
    8:  "#FFC000",
    9:  "#FFE699",
    10: "#FFF2CC",
    11: "#C0504D",
    12: "#F4B084",
    13: "#FFE699",
    14: "#FFF2CC",
    15: "#C6E0B4",
    16: "#FFC000",
    17: "#FFE699",
    18: "#FFF2CC",
    19: "#C6E0B4",
    20: "#70AD47",
    21: "#FFF2CC",
    22: "#FFE699",
    23: "#C6E0B4",
    24: "#70AD47",
    25: "#385723"
}

def highlight_cell(val):
    color = color_map[val]
    border = "3px solid black" if val == result_value else "1px solid #666"
    return f"""
        background-color: {color};
        border: {border};
        width: 80px;
        height: 80px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    """

st.markdown("### Matrice")

st.write("Comportamento (asse Y): Alto in alto, Basso in basso")
st.write("Performance (asse X): Basso a sinistra, Alto a destra")

styled_df = df.style.applymap(highlight_cell)

st.dataframe(styled_df, height=500)

st.markdown("""
<div style="text-align: center; margin-top: 20px; font-size: 20px;">
  PERFORMANCE → da Basso a sinistra, ad Alto a destra
</div>
""", unsafe_allow_html=True)
