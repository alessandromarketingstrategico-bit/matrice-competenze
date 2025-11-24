import streamlit as st
import numpy as np

st.set_page_config(page_title="Matrice Competenze", layout="centered")

st.title("Matrice Competenze – Performance vs Comportamento")
st.write("Seleziona i valori da 1 a 5 per posizionare la persona nella matrice.")

# Input utente
perf = st.slider("Performance (1 = Basso, 5 = Alto)", 1, 5, 3)
comp = st.slider("Comportamento (1 = Basso, 5 = Alto)", 1, 5, 3)

# Genera matrice 1–25
matrix_numbers = np.arange(1, 26).reshape(5, 5)
matrix_numbers = np.flipud(matrix_numbers)

quadrante = matrix_numbers[comp - 1, perf - 1]

st.subheader(f"Risultato: Quadrante {quadrante}")

# Tavolozza colori simile alla tua
colors = [
    ["#7a0000", "#cc0000", "#e57373", "#ffb300", "#fff176"],
    ["#c62828", "#ef5350", "#ff7043", "#ffd54f", "#fff59d"],
    ["#ef6c00", "#ff9800", "#fdd835", "#fff59d", "#c5e1a5"],
    ["#fff176", "#fff9c4", "#dcedc8", "#aed581", "#81c784"],
    ["#fff9c4", "#fffde7", "#c8e6c9", "#66bb6a", "#2e7d32"]
]

# Mostra matrice
st.write("Matrice")

for i in range(5):
    cols = st.columns(5)
    for j in range(5):
        style = f"""
        background-color:{colors[i][j]};
        color:black;
        border-radius:6px;
        padding:15px;
        text-align:center;
        font-size:18px;
        """
        if matrix_numbers[i][j] == quadrante:
            style += "border: 3px solid black;"
        cols[j].markdown(f"<div style='{style}'>{matrix_numbers[i][j]}</div>", unsafe_allow_html=True)
