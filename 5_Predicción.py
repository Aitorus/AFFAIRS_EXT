import streamlit as st
import pandas as pd
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
#---------------------------------------------------------------------------
st.set_page_config(page_title="Predicción")

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
    'text-align:center;"><strong>Machine Learning</p>'
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
st.write("-------------------------------------------------------------------------------------------------------------------")
#---------------------------------------------------------------------------
# Lectura

df_5 = st.session_state.df5


#---------------------------------------------------------------------------

# Definir los rangos para cada columna
rango_comunidad = st.sidebar.slider("COMUNIDAD", 1, 17)
st.sidebar.write("1.Andalucía 2.Aragón 3.Asturias 4.Baleares 5.Canarias 6.Cantabria 7.Castilla-La Manchad 8.Castilla-León 9.Cataluña 10.Extremadura 11.Galicia 12.Madrid 13.Murcia 14.Navarra 15.País Vasco 16.Rioja 17.Valencia")
st.sidebar.write("--------------------------------------------------------")
rango_s_amor = st.sidebar.slider("Satisfacción Amor", 0, 6)
st.sidebar.write("0.No tengo 1.Nada 2.Poco 3.Regular 4.Bastante 5.Mucho")
st.sidebar.write("--------------------------------------------------------")
rango_anos_pareja = st.sidebar.slider("Años en Pareja", 0, 100)
st.sidebar.write("--------------------------------------------------------")
rango_s_pareja = st.sidebar.slider("Satisfacción Pareja", 0, 5)
st.sidebar.write("0.No sé 1.Nada 2.Poco 3.Regular 4.Bastante 5.Mucho")
st.sidebar.write("--------------------------------------------------------")
rango_convive_pareja = st.sidebar.slider("Convive en Pareja", 0, 1)
st.sidebar.write("Sí:1 No:0")
st.sidebar.write("--------------------------------------------------------")
rango_afinidad_gen = st.sidebar.slider("Afinidad General en Pareja", 0, 4)
st.sidebar.write("0.Muy Mal 1.Mal 2.Regular 3.Bien 4.Muy Bien ")
st.sidebar.write("--------------------------------------------------------")
rango_afinidad_gustos = st.sidebar.slider("Afinidad Gustos en Pareja", 0, 5)
st.sidebar.write("0. No sé 1.Muy Mal 2.Mal 3.Regular 4.Bien 5.Muy Bien ")
st.sidebar.write("--------------------------------------------------------")
rango_afinidad_social = st.sidebar.slider("Afinidad Social en Pareja", 0, 5)
st.sidebar.write("0. No sé 1.Muy Mal 2.Mal 3.Regular 4.Bien 5.Muy Bien ")
st.sidebar.write("--------------------------------------------------------")
rango_afinidad_economi = st.sidebar.slider("Afinidad Económica en Pareja", 0, 5)
st.sidebar.write("0. No sé 1.Muy Mal 2.Mal 3.Regular 4.Bien 5.Muy Bien ")
st.sidebar.write("--------------------------------------------------------")
rango_afinidad_sex = st.sidebar.slider("Afinidad Sexual en Pareja", 0, 5)
st.sidebar.write("0. No sé 1.Muy Mal 2.Mal 3.Regular 4.Bien 5.Muy Bien ")
st.sidebar.write("--------------------------------------------------------")
rango_importancia_sex = st.sidebar.slider("Importancia del Sexo", 0, 10)
st.sidebar.write("0.Nada 5.Regular 10.Mucho")
st.sidebar.write("--------------------------------------------------------")
rango_importancia_sex_pareja = st.sidebar.slider("Importancia del Sexo de la Pareja", 0, 10)
st.sidebar.write("0.Nada 5.Regular 10.Mucho")
st.sidebar.write("--------------------------------------------------------")
rango_educacion_s = st.sidebar.slider("Eduación Sexual", 0, 1)
st.sidebar.write("0.No ha recibido 1.Si ha recibido")
st.sidebar.write("--------------------------------------------------------")
rango_atracion_p = st.sidebar.slider("Atracción Pasajera", 0, 1)
st.sidebar.write("0.No ha tenido 1.Si ha tenido")
st.sidebar.write("Atracción vecinos/as,compañeros/as,etc..")
st.sidebar.write("--------------------------------------------------------")
rango_n_parejas = st.sidebar.slider("Número de Parejas", 1, 6)
st.sidebar.write("1(0-2) 2.(3-4) 3.(5-6) 4.(7-8) 5.(8-9) 6.(>10)")
st.sidebar.write("--------------------------------------------------------")
rango_comunicacion_sex = st.sidebar.slider("Comunicación respecto al Sexo", 0, 3)
st.sidebar.write("0.Sin pareja 1.Es incómodo 2.Según el momento 3.Sí")
st.sidebar.write("--------------------------------------------------------")
rango_atraccion = st.sidebar.slider("Atracción Externa", 0, 2)
st.sidebar.write("0.Sin pareja 1.No 2.Sí")
st.sidebar.write("Atracción ajena a su pareja")
st.sidebar.write("--------------------------------------------------------")
st.sidebar.write("Frecuencia Sexual:")
rango_f_diariamente = st.sidebar.checkbox("F Diariamente", value=False)
rango_f_mensualmente = st.sidebar.checkbox("F Mensualmente",  value=False)
rango_f_ocasionalmente = st.sidebar.checkbox("F Ocasionalmente", value=False)
rango_f_regularmente = st.sidebar.checkbox("F Regularmente",  value=False)
rango_f_sin_actividad = st.sidebar.checkbox("F Sin actividad sexual", value=False)
st.sidebar.write("--------------------------------------------------------")
rango_f_anual = st.sidebar.slider("Frecuencia Anual", 0, 1)
st.sidebar.write("0.Según la época 1.Igual todo el año")
st.sidebar.write("--------------------------------------------------------")
rango_sexo = st.sidebar.slider("Género", 0, 1)
st.sidebar.write("0.Hombre 1.Mujer")
st.sidebar.write("--------------------------------------------------------")
rango_edad = st.sidebar.slider("Edad", 18, 100)
st.sidebar.write("--------------------------------------------------------")
rango_estudios = st.sidebar.slider("ESTUDIOS", 0, 4)
st.sidebar.write("0.Sin estudios 1.Primer grado(EGB) 2.Grado Medio 3.Grado Superior/Bat 4.Universitario")
st.sidebar.write("--------------------------------------------------------")
rango_sit_laboral = st.sidebar.slider("SIT_LABORAL", 0, 2)
st.sidebar.write("0.Desempleado 1.Estudiante 2.Trabaja/Jubilado")
st.sidebar.write("--------------------------------------------------------")
st.sidebar.write("Ocupación:")
rango_ocupacion_autonomo = st.sidebar.checkbox("Autónomo", value=False)
rango_ocupacion_otro = st.sidebar.checkbox("Otro", value=False)
rango_ocupacion_obrero = st.sidebar.checkbox("Obrero", value=False)
rango_ocupacion_mando = st.sidebar.checkbox("Mando", value=False)
rango_ocupacion_director = st.sidebar.checkbox("Director", value=False)
rango_ocupacion_comerciante = st.sidebar.checkbox("Comerciante", value=False)
rango_ocupacion_agricultor = st.sidebar.checkbox("Agricultor", value=False)
st.sidebar.write("--------------------------------------------------------")
rango_status = st.sidebar.slider("STATUS", 0, 2)
st.sidebar.write("0.Baja 1.Media 2.Alta ")
st.sidebar.write("--------------------------------------------------------")
rango_nacionalidad = st.sidebar.slider("NACIONALIDAD", 0, 1)
st.sidebar.write("0.Extranjero 1.Nacionalidad Española")
st.sidebar.write("--------------------------------------------------------")
rango_religion = st.sidebar.slider("RELIGION", 0, 2)
st.sidebar.write("0.No creyente 1.Católico 3.Otra religión")
st.sidebar.write("--------------------------------------------------------")
rango_felicidad = st.sidebar.slider("Felicidad General", 0, 5)
st.sidebar.write("0.No sé 1.Nada 2.Poco 3.Regular 4.Bastante 5.Mucho")
st.sidebar.write("--------------------------------------------------------")
rango_salud = st.sidebar.slider("Estado de Salud", 1, 5)
st.sidebar.write("1.Muy Malo 2.Malo 3.Regular 4.Bueno 5.Muy bueno")
st.sidebar.write("--------------------------------------------------------")
rango_nivel= st.sidebar.slider("Satisfacción Nivel de Vida", 0, 5)
st.sidebar.write("0.No sé 1.Nada 2.Poco 3.Regular 4.Bastante 5.Mucho")
st.sidebar.write("--------------------------------------------------------")
rango_laboral = st.sidebar.slider("Satisfacción Laboral", 0, 5)
st.sidebar.write("")
st.sidebar.write("0.No sé 1.Nada 2.Poco 3.Regular 4.Bastante 5.Mucho")

bienestar = (rango_felicidad + rango_salud + rango_nivel + rango_laboral)/4

st.write("------------------------------------------------------------------------")
if st.button("PyCaret"):
    st.image("./img/pycaret1.jpg")
# -------------------------------------------------------------------------------------

new_data = pd.DataFrame({
        "COMUNIDAD": [rango_comunidad],
        "S_AMOR": [rango_s_amor],
        "AÑOS_PAREJA": [rango_anos_pareja],
        "S_PAREJA": [rango_s_pareja],
        "CONVIVE_PAREJA": [rango_convive_pareja],
        "AFINIDAD_GEN": [rango_afinidad_gen],
        "AFINIDAD_GUSTOS": [rango_afinidad_gustos],
        "AFINIDAD_SOCIAL": [rango_afinidad_social],
        "AFINIDAD_ECONOMI": [rango_afinidad_economi],
        "AFINIDAD_SEX": [rango_afinidad_sex],
        "IMPORTANCIA_SEX": [rango_importancia_sex],
        "IMPORTANCIA_SEX_PAREJA": [rango_importancia_sex_pareja],
        "EDUCACION_S": [rango_educacion_s],
        "ATRACION_P": [rango_atracion_p],
        "N_PAREJAS": [rango_n_parejas],
        "COMUNICACION_SEX": [rango_comunicacion_sex],
        "ATRACCIÓN": [rango_atraccion],
        "F_SEXO_Diariamente": [rango_f_diariamente],
        "F_SEXO_Mensualmente": [rango_f_mensualmente],
        "F_SEXO_Ocasionalmente": [rango_f_ocasionalmente],
        "F_SEXO_Regularmente": [rango_f_regularmente],
        "F_SEXO_Sin actividad sexual": [rango_f_sin_actividad],
        "F_ANUAL": [rango_f_anual],
        "SEXO": [rango_sexo],
        "EDAD": [rango_edad],
        "ESTUDIOS": [rango_estudios],
        "SIT_LABORAL": [rango_sit_laboral],
        "OCUPACION_Autónomo": [int(rango_ocupacion_autonomo)],
        "OCUPACION_Otro": [int(rango_ocupacion_otro)],
        "OCUPACION_Obrero": [int(rango_ocupacion_obrero)],
        "OCUPACION_Mando": [int(rango_ocupacion_mando)],
        "OCUPACION_Director": [int(rango_ocupacion_director)],
        "OCUPACION_Comerciante": [int(rango_ocupacion_comerciante)],
        "OCUPACION_Agricultor": [int(rango_ocupacion_agricultor)],
        "STATUS": [rango_status], 
        "NACIONALIDAD": [rango_nacionalidad],
        "RELIGION": [rango_religion],
        "BIENESTAR": [bienestar]
    })



st.write("DataFrame creado:")
st.write(new_data)

    
    
st.write("-----------------------------------------------------------")
st.markdown(
    '<div class="justified-text">Recall (sensibilidad): Mide la proporción de verdaderos positivos respecto a todos los valores positivos reales. Es útil cuando el objetivo es identificar la mayor cantidad posible de casos positivos, minimizando los falsos negativos.</div>',
    unsafe_allow_html=True
)
st.write("Es importante identificar a todas las personas que son infieles, ya que no quieres perder a ningún infiel potencial. Un alto recall indica que el modelo puede detectar adecuadamente los casos de infidelidad, minimizando los falsos negativos.")
st.write("-----------------------------------------------------------")
st.markdown(
    '<div class="justified-text">Precision (precisión): Mide la proporción de verdaderos positivos respecto a todos los valores positivos predichos. Es útil cuando el objetivo es minimizar los falsos positivos y tener una alta confianza en las predicciones positivas.</div>',
    unsafe_allow_html=True
)
st.write("La precisión es relevante porque queremos asegurarnos de que las personas que el modelo predice como infieles realmente lo sean. Una alta precisión indica que el modelo tiene una baja tasa de falsos positivos.")
st.write("-----------------------------------------------------------")
st.markdown(
    '<div class="justified-text">F1 score: Es una medida que combina el recall y la precisión, ofreciendo un equilibrio entre ambos. Es útil cuando deseas tener en cuenta tanto la capacidad de identificar casos positivos como la precisión de las predicciones.</div>',
    unsafe_allow_html=True
)
st.write("El F1-score proporciona una evaluación general del rendimiento del modelo al considerar tanto los falsos positivos como los falsos negativos.")
st.write("-----------------------------------------------------------")
from pycaret.classification import setup, create_model, predict_model, plot_model

  
def perform_classification(df):
    classification_setup = setup(data=df_5, target='R_EXT_MATRIMONIAL')
    model = create_model('nb')
    # Realizar predicciones en el nuevo conjunto de datos
    predictions = predict_model(model, data=df)
    # Mostrar las predicciones
    st.write("Valor predecido: ", predictions["prediction_label"])
    st.write("Puntuación de la predicción: ", predictions["prediction_score"])
    st.write("------------------------------------------------------------------------")
    plot_model(model, plot='confusion_matrix', display_format= 'streamlit')
    st.write("------------------------------------------------------------------------")
    
if st.button("Crear DataFrame y Pycaret"):
    newdata = new_data.copy()
    perform_classification(newdata)


    
    
    

# ----------------------------------------------------------------------
