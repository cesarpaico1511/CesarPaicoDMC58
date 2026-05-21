import streamlit as st
import numpy as np

st.title("Mi primera aplicación en Pythom")  #Titulo
st.sidebar.title("Parámetros")  #Barra lateral izquierda
st.write("Elaborado por: Julio Cesar Paico Jaime") #write es el equivalente a print

st.sidebar.image("innovacion.png")

#st hace referencia a la libreria de streamlit, sidebar coloca a la izquierza, y selectbos, genera un combo con una lista de 4 opciones
sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1", "Sesión 2", "Sesión 3", "Sesión 4"])

#estructuras de control

#Describe el código de la sesión 1
if sesion == "Sesión 1":
  st.write("Bienvenido a la sesión 1")
  st.image("Python.png")

#Describe el código de la sesión 2  
elif sesion == "Sesión 2":
  st.write("Bienvenido a la sesión 2")

  precio = st.number_input("Ingrese el precio del producto", min_value = 0, max_value = 5000, value = 1200)
  descuento = st.number_input("Ingrese el descuento del producto del 0 al 100%", min_value = 0, max_value = 100)

  precio_final_producto = precio - (precio*descuento/100)

  st.write("EL precio final de producto es: ", precio_final_producto)

#Describe el código de la sesión 3
elif sesion == "Sesión 3":
  st.write("Bienvenido a la sesión 3")

  #crea variable fin_rango
  fin_rango = st.slider("Seleccion un valor:", min_value = 0, max_value = 20, value = 7)

  arreglo = np.arange(0, fin_rango)

  st.write(arreglo)

#Describe el código de la sesión 4
else: 
  st.write("Bienvenido a la sesión 4")














  
