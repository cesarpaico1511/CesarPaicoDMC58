import streamlit as st

st.title("Mi primera aplicación en Pythom")  #Titulo
st.sidebar.title("Parámetros")  #Barra lateral izquierda
st.write("Elaborado por: Julio Cesar Paico Jaime") #write es el equivalente a print

#st hace referencia a la libreria de streamlit, sidebar coloca a la izquierza, y selectbos, genera un combo con una lista de 4 opciones
sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1", "Sesión 2", "Sesión 3", "Sesión 4"])

#estructuras de control

if sesion == "Sesión 1":
  st.write("Bienvenido a la sesión 1")
  
elif sesion == "Sesión 2":
  st.write("Bienvenido a la sesión 2")

elif sesion == "Sesión 3":
  st.write("Bienvenido a la sesión 3")

else: 
  st.write("Bienvenido a la sesión4")














  
