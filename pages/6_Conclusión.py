import streamlit as st
import pandas as pd
import ipywidgets as widgets
from IPython.display import display
#---------------------------------------------------------------------------
st.set_page_config(page_title="Conclusión")

st.markdown(
    '<div style="color:white;'
    'display:fill;'
    'border-radius:5px;'
    'background-color:#878471;'
    'font-size:200%;'
    'font-family:Courier;'
    'letter-spacing:0.5px">'
    '<p style="padding: 10px;'
    'color:black;'
    'font-size:120%;'
    'text-align:center;"><strong>Conclusión</p>'
    '</div>',
    unsafe_allow_html=True
)
st.write(" ")
st.write(" ")
st.write(" ")

#---------------------------------------------------------------------------

st.image("./img/conc.jpg",use_column_width=True)

st.write("-------------------------------------------------------------------------")
st.write("El estudio reveló diferencias significativas en el nivel de bienestar entre las comunidades estudiadas, relacionadas con la felicidad, satisfacción laboral, nivel de vida y percepción del estado de salud.")
st.write("")
st.write("Las comunidades presentaron variaciones en la satisfacción en el amor, lo que indica la influencia de los entornos sociales y culturales en las percepciones y experiencias amorosas.")
st.write("")
st.write("La infidelidad fue identificada en casi todas las comunidades, aunque hubo diferencias en su prevalencia.")
st.write("")
st.write("El modelo de predicción basado en Naive Bayes mostró un rendimiento subóptimo en la clasificación de casos de infidelidad, lo que indica dificultades para identificar correctamente los casos positivos.")
st.write("")
st.write("Los datos utilizados en el estudio están sesgados debido a una mayor proporción de personas fieles en comparación con las infieles.")
st.write("")
st.write("")
st.write("")
st.markdown(
    """
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="justified-text">En resumen, el proyecto proporcionó información valiosa sobre las actitudes y prácticas sexuales. Aunque el modelo de predicción presentó dificultades, estos resultados pueden servir como base para futuras encuestas,investigaciones y mejoras en la precisión de los modelos en relación con las relaciones afectivas y la infidelidad. Se recomienda considerar datos más equilibrados y explorar diferentes enfoques y algoritmos para obtener una comprensión más precisa de estos temas.</div>',
    unsafe_allow_html=True
)
st.write("")