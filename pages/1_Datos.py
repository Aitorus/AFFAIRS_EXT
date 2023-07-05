import streamlit as st
import pandas as pd
import plotly.express as px
#---------------------------------------------------------------------------
st.set_page_config(page_title="Datos")
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
    'text-align:center;"><strong>Nuestros Datos...  </p>'
    '</div>',
    unsafe_allow_html=True
)
st.write(" ")
st.write(" ")
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

st.markdown(
    '<div class="justified-text">La única fuente y principal de nuestros datos proviene del CIS- Centro de Investigaciones Sociológicas Español, de aquí obtenemos nuestro conjunto de datos del estudio 2738. Este estudio hace referencia a Actitudes y Prácticas Sexuales. El estudio data del 14 de enero de 2008.</div>',
    unsafe_allow_html=True
)


st.write("")
st.write("")
st.write("")
if st.button('Enlace Conjunto Datos'):
    st.write(' https://www.cis.es/cis/opencm/ES/1_encuestas/estudios/ver.jsp?estudio=9882&amp;cuestionario=11496&amp;muestra=17165 ')


if st.button("Enlace Estudio"):
    st.write("https://datos.gob.es/es/catalogo/ea0022266-1883barometro-de-septiembre-1990")

if st.button("Enlace Preguntas"):
    st.write("https://www.cis.es/cis/export/sites/default/-Archivos/Marginales/2720_2739/2738/e273800.html")
#---------------------------------------------------------------------------
# Lectura
df_original1 = st.session_state.df1
df_final1 = st.session_state.df2



#---------------------------------------------------------------------------
st.write("")
st.write("")
st.write("")
st.write("--------------------------------------------------------------------------")
tabs0 = st.tabs(["Dataframe Original","Inicio","Procesamiento","Dataframe Final","El Público"])

tab_plots= tabs0[0]
with tab_plots:
    # Dataframe
    st.write("El Dataframe original convertido de .sav a .csv")
    st.write(df_original1)
tab_plots= tabs0[1]
with tab_plots:
    # Inicio
    st.write("Dataframe Info")
    st.image("./img/1t.jpg")
    nulos = df_original1.isnull().sum().sum()
    st.write("Total de valores nulos: ")
    st.write(nulos)
    
    with st.expander('Exploración de las variables Núm:',expanded=False):
        st.write(df_original1.describe().T)
    with st.expander('Exploración de las variables CAT:',expanded=False):
        st.image("./img/EDA.png")
tab_plots= tabs0[2]
with tab_plots:
    # Procesamiento
    st.write("Operaciones principales")
    c1, c2= st.columns(2)
    with c1:
        st.write("Drop COL")
        st.image("./img/p1.jpg")
    with c2:
        st.write("Rename COL")
        st.image("./img/p2.jpg")
    c1, c2= st.columns(2)
    with c1:
        st.write("Astype COL")
        st.image("./img/p3.jpg")
        st.write("KNN Imputer")
        st.image("./img/p5.jpg")
    with c2:
        st.write("MAP COL")
        st.image("./img/p4.jpg")
    
tab_plots= tabs0[3]
with tab_plots:
    # Final Procesamiento
    st.write("")
    st.write(df_final1)
    
tab_plots= tabs0[4]
with tab_plots:
    st.write("¿Quien es nuestro público?¿ De quien han obtenido los datos y que características tienen?")
    total = len(df_final1["ID"])
    st.write("Total de encuestados:",total)
    st.write("¿De dónde son?")

    # ------------------------------------------------------------
    region_counts = df_final1["COMUNIDAD"].value_counts()
    fig1 = px.pie(region_counts, values=region_counts, names=region_counts.index, 
                title="Encuestados por Comunidad", hole=0.4)
    fig1.update_traces(textposition="inside", textinfo="percent+label", 
                    marker=dict(line=dict(color="#000000", width=2)))
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1)

    # ------------------------------------------------------------
    st.write("¿Que sexo tienen?")
    sexo_counts = df_final1["SEXO"].value_counts()
    fig2 = px.bar(x=["Mujer", "Hombre"], y=sexo_counts.values,
                color=["blue", "pink"],
                labels={"x": "Sexo", "y": "Cantidad"},
                title="Sexo Encuestados")
    fig2.update_traces(textposition="inside",
                    marker=dict(line=dict(color="#000000", width=2,)))
    fig2.update_layout(showlegend=False)
    st.plotly_chart(fig2)
    # ------------------------------------------------------------
    st.write("¿Que edad tienen?")
    age_ranges = pd.cut(df_final1["EDAD"], bins=range(18, 101, 6), right=False)
    age_counts = age_ranges.value_counts().sort_index()
    fig3 = px.bar(x=age_counts.index.astype(str), y=age_counts.values, color=age_counts.index.astype(str),
                labels={"x": "Rango de Edad", "y": "Cantidad", "color": "Rango de Edad"},
                title="Encuestados por Edad")
    fig3.update_layout(showlegend=False)
    st.plotly_chart(fig3)