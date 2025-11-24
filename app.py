import streamlit as st
import numpy as np

st.set_page_config(page_title="Matrice Competenze", layout="centered")

st.image("http://www.covi-electric.com/images/yootheme/Logo-COVI.png", width=200)

st.title("Matrice Competenze – Performance vs Comportamento")
st.write("Seleziona i valori da 1 a 5 per posizionare la persona nella matrice.")

perf = st.slider("Performance (1 = Basso, 5 = Alto)", 1, 5, 1)
comp = st.slider("Comportamento (1 = Basso, 5 = Alto)", 1, 5, 1)

matrix_numbers = np.arange(1, 26).reshape(5, 5)

quadrante = matrix_numbers[comp - 1, perf - 1]

st.subheader(f"Risultato: Quadrante {quadrante}")

colors = [
    ["#7a0000", "#cc0000", "#e57373", "#ffb300", "#fff176"],
    ["#c62828", "#ef5350", "#ff7043", "#ffd54f", "#fff59d"],
    ["#ef6c00", "#ff9800", "#fdd835", "#fff59d", "#c5e1a5"],
    ["#fff176", "#fff9c4", "#dcedc8", "#aed581", "#81c784"],
    ["#fff9c4", "#fffde7", "#c8e6c9", "#66bb6a", "#2e7d32"]
]

st.write("Matrice")

for i in range(5):
    cols = st.columns(5)
    for j in range(5):
        style = f"""
        background-color:{colors[i][j]};
        color:black;
        border-radius:6px;
        width:70px;
        height:70px;
        display:flex;
        justify-content:center;
        align-items:center;
        font-size:18px;
        """
        if matrix_numbers[i][j] == quadrante:
            style += "border: 3px solid black;"
        cols[j].markdown(f"<div style='{style}'>{matrix_numbers[i][j]}</div>", unsafe_allow_html=True)
