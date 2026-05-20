import streamlit as st

st.title("Mi primera aplicación en Pythom")  #Titulo
st.sidebar.title("Parámetros")  #Barra lateral izquierda
st.write("Elaborado por: Julio Cesar Paico Jaime") #write es el equivalente a print

sesion = st.selectbox("Seleccione una sesión", ["Sesión 1"], ["Sesión 2"], ["Sesión 3"], ["Sesión 4"])
