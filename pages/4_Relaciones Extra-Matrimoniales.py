import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import folium_static
import json
import requests

#---------------------------------------------------------------------------
st.set_page_config(page_title="Ups")

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
    'text-align:center;"><strong>Relaciones Extra-Matrimoniales</p>'
    '</div>',
    unsafe_allow_html=True
)
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write("-------------------------------------------------------------------------------------------------------------------")
#---------------------------------------------------------------------------
# Lectura

df_4 = st.session_state.df4

#---------------------------------------------------------------------------

# Descargar el archivo GeoJSON y guardarlo localmente
ccaa_url = "https://github.com/R-CoderDotCom/data/blob/main/shapefile_spain/spain.geojson?raw=true"
response = requests.get(ccaa_url)
with open("spain.geojson", "w") as f:
    f.write(response.text)

# Cargar el GeoJSON localmente
with open("spain.geojson") as f:
    ccaa = json.load(f)

# Calcular el recuento de R_EXT_MATRIMONIAL por comunidad
df_count = df_4.groupby("COMUNIDAD")["R_EXT_MATRIMONIAL"].value_counts().reset_index(name="count")
df_count = df_count[df_count["R_EXT_MATRIMONIAL"] == 1]

# Crear el mapa con Folium
m = folium.Map(location=[40.0, -3.72], zoom_start=4)

# Añadir el geojson como una capa al mapa
folium.GeoJson(ccaa, name="Spain Geojson").add_to(m)

# Añadir el choropleth al mapa
folium.Choropleth(
    geo_data=ccaa,
    name="Recuento R_EXT_MATRIMONIAL",
    data=df_count,
    columns=["COMUNIDAD", "count"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Recuento R_EXT_MATRIMONIAL"
).add_to(m)

# Mostrar el mapa en Streamlit
folium_static(m)
st.write("---------------------------------------------")
columnas = ['AÑOS_PAREJA', 'CONVIVE_PAREJA', 'CASADO', 'EDUCACION_S', 'ATRACION_P', 'N_PAREJAS', 'COMUNICACION_SEX',
            'ATRACCIÓN', 'F_SEXO', 'F_ANUAL', 'SEXO', 'EDAD', 'E_CIVIL', 'ESTUDIOS', 'SIT_LABORAL',
            'OCUPACION', 'STATUS', 'NACIONALIDAD',"BIENESTAR",'RELIGION']

columna_seleccionada = st.selectbox("Selecciona una columna para comparar con R_EXT_MATRIMONIAL", columnas)

df_recuento = df_4.groupby(columna_seleccionada)["R_EXT_MATRIMONIAL"].value_counts().reset_index(name="Recuento")

fig = px.bar(df_recuento, x=columna_seleccionada, y="Recuento", color="R_EXT_MATRIMONIAL",
             title="Recuento de R_EXT_MATRIMONIAL según la columna seleccionada")
fig.update_layout(xaxis_title=columna_seleccionada, yaxis_title="Recuento",showlegend=False)
st.plotly_chart(fig)

# ---------------------------------------------------------------------
st.sidebar.write("--------------------------------------------")
st.sidebar.write("Leyenda: ")
st.sidebar.write("CONVIVE_PAREJA")
st.sidebar.write("Sí:1 No:0")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("CASADO")
st.sidebar.write("Sí:1 No:0")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("EDUCACION_S")
st.sidebar.write("Ha recibido educación sexual")
st.sidebar.write("Sí:1 No:0")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("ATRACION_P")
st.sidebar.write("Atracción vecinas/nos,compañeros/as,etc..")
st.sidebar.write("Sí:1 No:0")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("COMUNICACION_SEX")
st.sidebar.write("Comunicación sobre el sexo con la pareja")
st.sidebar.write("0.Sin pareja 1.Es incómodo 2.Según el momento 3.Sí")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("R_EXT_MATRIMONIAL")
st.sidebar.write("Ha tenido relaciones fuera de la pareja/matrimonio.")
st.sidebar.write("Sí:1 No:0")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("ATRACCIÓN")
st.sidebar.write("0.Sin pareja 1.No 2.Sí")
st.sidebar.write("Atracción ajena a su pareja")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("SEXO")
st.sidebar.write("0.Hombre 1.Mujer")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("E_CIVIL")
st.sidebar.write("0.Soltero/a 1.Relación")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("ESTUDIOS")
st.sidebar.write("0.Sin estudios 1.Primer grado(EGB) 2.Grado Medio 3.Grado Superior/Bat 4.Universitario")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("SIT_LABORAL")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("STATUS")
st.sidebar.write("Estatus Social")
st.sidebar.write("0.Baja 1.Media 2.Alta ")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("RELIGION")
st.sidebar.write("0.No creyente 1.Católico 3.Otra religión")
st.sidebar.write("--------------------------------------------")
st.sidebar.write("NACIONALIDAD")
st.sidebar.write("0.Extranjero 1.Nacionalidad Española")