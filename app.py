import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv')
st.header("Análisis de anuncios de coches usados")
st.subheader("Visualización con botones")


hist_button = st.button("Mostrar histograma")
if hist_button:
    st.write("Creación de un histograma para la columna odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button("Mostrar dispersión")
if scatter_button:
    st.write("Creación de un gráfico de dispersión (precio vs odómetro)")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


st.subheader("Visualización con checkboxes")


if st.checkbox("Mostrar histograma del odómetro"):
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


if st.checkbox("Mostrar gráfico de dispersión (precio vs odómetro)"):
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

    