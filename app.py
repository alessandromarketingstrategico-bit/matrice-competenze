import streamlit as st
import numpy as np

st.set_page_config(page_title="Matrice Competenze", layout="centered")

st.title("Matrice Competenze – Performance vs Comportamento")
st.write("Seleziona i valori da 1 a 5 per posizionare la persona nella matrice.")

perf = st.slider("Performance (1 = Basso, 5 = Alto)", 1, 5, 3)
comp = st.slider("Comportamento (1 = Basso, 5 = Alto)", 1, 5, 3)

matrix_numbers = np.flipud(np.arange(1, 26).reshape(5, 5))
quadrante = matrix_numbers[comp - 1, perf - 1]

st.subheader(f"Risultato: Quadrante {quadrante}")

colors = [
    ["#b71c1c","#c62828","#d84315","#f9a825","#fdd835"],
    ["#c62828","#ef5350","#ff7043","#ffca28","#fff59d"],
    ["#ef6c00","#ffa726","#ffd54f","#fff59d","#c5e1a5"],
    ["#fff176","#fff9c4","#dcedc8","#aed581","#81c784"],
    ["#fff59d","#fffde7","#c8e6c9","#66bb6a","#2e7d32"]
]

st.write("")
st.write("Matrice (replicata come il modello)")

for i in range(5):
    row = st.columns([0.6,1,1,1,1,1])
    if i == 0:
        row[0].write("Alto")
    elif i == 2:
        row[0].write("Medio")
    elif i == 4:
        row[0].write("Basso")
    else:
        row[0].write("")

    for j in range(5):
        style = f"""
        background-color:{colors[i][j]};
        border-radius:8px;
        padding:20px;
        text-align:center;
        font-size:20px;
        color:black;
        """
        if matrix_numbers[i][j] == quadrante:
            style += "border: 4px solid black;"
        row[j+1].markdown(f"<div style='{style}'>{matrix_numbers[i][j]}</div>", unsafe_allow_html=True)

st.write("")
cols = st.columns([1,1,1,1,1,1])
cols[1].write("Basso")
cols[3].write("Medio")
cols[5].write("Alto")

st.write("")
st.write("Performance →")
