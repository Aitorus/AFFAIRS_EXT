import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
#---------------------------------------------------------------------------
st.set_page_config(page_title="Bienestar")
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
    'text-align:center;"><strong>El Bienestar General</p>'
    '</div>',
    unsafe_allow_html=True
)
st.write(" ")
st.write(" ")
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

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write("-------------------------------------------------------------------------------------------------------------------")
#---------------------------------------------------------------------------
st.sidebar.image ("./img/4.jpg",use_column_width=True)
# Lectura
df_2 = st.session_state.df2
#---------------------------------------------------------------------------

df_mean = df_2.groupby("COMUNIDAD")["BIENESTAR"].mean().reset_index()

# Create the figure and axes
fig1 = plt.figure(figsize=(8, 8))
ax1 = fig1.add_subplot(111, polar=True)
n = len(df_mean)
theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
radii = [0]
color_palette = plt.cm.get_cmap("tab10")
for i, (comunidad, bienestar) in enumerate(zip(df_mean["COMUNIDAD"], df_mean["BIENESTAR"])):
    color = color_palette(i % 10)
    ax1.bar(theta[i], bienestar, width=0.5, alpha=0.8, color=color)
    ax1.text(theta[i], bienestar, f"{bienestar:.2f}", ha="center", va="bottom", fontsize=10)
ax1.set_yticks(radii)
ax1.set_yticklabels(radii, fontsize=10)
ax1.set_ylim(0, 5)
ax1.set_xticks(theta)
ax1.set_xticklabels(df_mean["COMUNIDAD"], fontsize=10)
ax1.set_facecolor("lightgray")
ax1.set_title("Media de Bienestar por Comunidad", fontsize=14)

st.pyplot(fig1)
#---------------------------------------------------------------------------
st.write("---------------------------------------------------------")
st.write("")
st.write("")
st.write("")

comunidades = df_2["COMUNIDAD"].unique()
comunidades_seleccionadas = st.multiselect("Selecciona las comunidades", comunidades)
datos = df_2[df_2["COMUNIDAD"].isin(comunidades_seleccionadas)]
df_media = datos.groupby("COMUNIDAD").agg({
    "P_FELICIDAD": "mean",
    "P_SALUD": "mean",
    "S_NIVEL_VIDA": "mean",
    "S_LABORAL": "mean"
}).reset_index()
fig = px.line(df_media, x="COMUNIDAD", y=["P_FELICIDAD", "P_SALUD", "S_NIVEL_VIDA", "S_LABORAL"],
              title="Media de Bienestar por Comunidad")
fig.update_layout(xaxis_title="Comunidad", yaxis_title="Media")
st.plotly_chart(fig)

