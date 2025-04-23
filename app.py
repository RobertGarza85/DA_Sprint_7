import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado principal
st.header('Análisis de datos de vehículos en venta')

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para crear un histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Selector de columnas para el gráfico de dispersión
st.write('Gráfico de dispersión')
x_column = st.selectbox('Selecciona la columna para el eje X', car_data.columns)  # Selector para X
y_column = st.selectbox('Selecciona la columna para el eje Y', car_data.columns)  # Selector para Y

scatter_button = st.button('Construir gráfico de dispersión')  # Botón para el gráfico

if scatter_button:  # Al hacer clic en el botón
    st.write(f'Creación de un gráfico de dispersión: {x_column} vs. {y_column}')
    scatter_fig = px.scatter(car_data, x=x_column, y=y_column, color="condition", title=f'{x_column} vs. {y_column}')
    st.plotly_chart(scatter_fig, use_container_width=True)
 #Comentarios: Selector interactivo: Los usuarios pueden elegir qué columnas quieren usar para los ejes X y Y del gráfico de dispersión.
 # Gráfico dinámico: Al hacer clic en el botón "Construir gráfico de dispersión", se genera un gráfico interactivo con Plotly, coloreado por la columna condition.

 #Flexibilidad: Puedes analizar relaciones entre cualquier par de columnas de tu dataset.