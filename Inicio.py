import streamlit as st
import pandas as pd
import re
#---------------------------------------------------------------------------

# 1. El público de la encuesta
# 2. El Bienestar General
# 3. Relaciones Afectivas
# 4. Las Relaciones Extramatrimoniales
# 5. Predicción de la "Infidelidad"

#---------------------------------------------------------------------------
st.set_page_config(page_title='Equilibrio', layout='wide',initial_sidebar_state="expanded")

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
    'text-align:center;"><strong>España 2008</strong>- El Bienestar General y las Relaciones Afectivas</p>'
    '</div>',
    unsafe_allow_html=True
)
#---------------------------------------------------------------------------
col1, col2, col3 = st.columns(3)
col2.image("./img/0.jpg",width=400)
#---------------------------------------------------------------------------
# Autor / Fecha
c1, c2= st.columns(2)
with c1:
    st.info('AUTOR : AITOR GUERRA BERNAL', icon="💡")
with c2:
    st.info('FECHA : 15/06/2023', icon="📅")

# Columnas
st.write("El Bienestar General y las Relaciones Afectivas - España 2008")
st.write("\n")
st.write("\n")

st.sidebar.image ("./img/3.jpg",use_column_width=True)
st.sidebar.markdown(
    """
    <style>
    .sidebar-text {
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="sidebar-text">El objetivo principal es obtener una comprensión más profunda del estado emocional y las dinámicas de pareja en España en ese período específico. A través del análisis de los datos recopilados y la aplicación de técnicas predictivas, se busca identificar posibles factores que influyan en la infidelidad en las relaciones de pareja.</div>',
    unsafe_allow_html=True
)
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
    '<div class="justified-text">El proyecto se enfoca en analizar diferentes aspectos relacionados con el bienestar general y las relaciones afectivas en España en el año 2008. A partir de estos datos, se examina el nivel de bienestar general de los participantes, se exploran las características de sus relaciones afectivas y se investiga la presencia  de las relaciones extramatrimoniales.</div>',
    unsafe_allow_html=True
)
st.markdown(
    """
En el proyecto se analizarán los siguientes parámetros:
- El bienestar General.
- Relaciones Afectivas.
- Relaciones Extra - Matrimoniales.
- Predicción de la infidelidad.
    """)
#---------------------------------------------------------------------------

# Lectura.........................................

df_original = pd.read_csv('./pages/pre_st/df_original.csv')
df = pd.read_csv('./pages/pre_st/df.csv')
df3 = pd.read_csv('./pages/pre_st/df3.csv')
df4 = pd.read_csv('./pages/pre_st/df4.csv')
df5 = pd.read_csv('./pages/pre_st/df5.csv', index_col=0)

st.session_state.df1 = df_original
st.session_state.df2 = df
st.session_state.df3 = df3
st.session_state.df4 = df4
st.session_state.df5 = df5
#--------------------------------------------------------------------------------------------------------------------------

