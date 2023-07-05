import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import folium_static
import json
import requests

#---------------------------------------------------------------------------
st.set_page_config(page_title="R.Afectivas")
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
    'text-align:center;"><strong>Las Relaciones Afectivas</p>'
    '</div>',
    unsafe_allow_html=True
)
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

#---------------------------------------------------------------------------
# Lectura
df_3 = st.session_state.df3
#---------------------------------------------------------------------------

# Satisfacción en el AMOR
fig3 = px.treemap(df_3, path=["COMUNIDAD"], values="S_AMOR",
                 color="S_AMOR", hover_data=["COMUNIDAD"],
                 title="Satisfacción en el AMOR por Comunidad")
st.plotly_chart(fig3)


#---------------------------------------------------------------------------
# Descargar el archivo GeoJSON y guardarlo localmente
ccaa_url = "https://github.com/R-CoderDotCom/data/blob/main/shapefile_spain/spain.geojson?raw=true"
response = requests.get(ccaa_url)
with open("spain.geojson", "w") as f:
    f.write(response.text)

# Cargar el GeoJSON localmente
with open("spain.geojson") as f:
    ccaa = json.load(f)

# Calcular la media de S_AMOR por comunidad
df_mean = df_3.groupby("COMUNIDAD")["S_AMOR"].mean().reset_index()

# Crear el mapa con Folium
m = folium.Map(location=[40.0, -3.72], zoom_start=4)

# Añadir el geojson como una capa al mapa
folium.GeoJson(ccaa, name="Spain Geojson").add_to(m)

# Añadir el choropleth al mapa
folium.Choropleth(
    geo_data=ccaa,
    name="Media S_AMOR",
    data=df_mean,
    columns=["COMUNIDAD", "S_AMOR"],
    key_on="feature.properties.name",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Media S_AMOR"
).add_to(m)

# Mostrar el mapa en Streamlit
st.write("Satisfacción del Amor: ")
folium_static(m)

st.write("-----------------------------------------------------------------------------")
st.write("Repercusión del Amor respecto otras variables:")
columnas = ['AÑOS_PAREJA', 'CONVIVE_PAREJA', 'CASADO', 'EDUCACION_S', 'ATRACION_P', 'N_PAREJAS', 'COMUNICACION_SEX',
            'R_EXT_MATRIMONIAL', 'ATRACCIÓN', 'F_SEXO', 'F_ANUAL',"BIENESTAR",'SEXO', 'EDAD', 'E_CIVIL', 'ESTUDIOS', 'SIT_LABORAL',
            'OCUPACION', 'STATUS', 'NACIONALIDAD', 'RELIGION']

columna_seleccionada = st.selectbox("Selecciona una columna para comparar con S_AMOR", columnas)

df_media = df_3.groupby(columna_seleccionada)["S_AMOR"].mean().reset_index()

fig = px.bar(df_media, x=columna_seleccionada, y="S_AMOR", title="Relación entre la columna seleccionada y S_AMOR")
fig.update_layout(xaxis_title=columna_seleccionada, yaxis_title="Media de S_AMOR")
st.plotly_chart(fig)


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