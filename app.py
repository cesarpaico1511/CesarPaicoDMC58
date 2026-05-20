import streamlit as st

st.title("Mi primera aplicación en Pythom")  #Titulo
st.sidebar.title("Parámetros")  #Barra lateral izquierda
st.write("Elaborado por: Julio Cesar Paico Jaime") #write es el equivalente a print

st.sidebar.image("innovacion.png")

#st hace referencia a la libreria de streamlit, sidebar coloca a la izquierza, y selectbos, genera un combo con una lista de 4 opciones
sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1", "Sesión 2", "Sesión 3", "Sesión 4"])

#estructuras de control

if sesion == "Sesión 1":
  st.write("Bienvenido a la sesión 1")
  st.image("Python.png")


  
elif sesion == "Sesión 2":
  st.write("Bienvenido a la sesión 2")

  precio = st.number_input("Ingrese el precio del producto")
  descuento = st.number_input("Ingrese el descuento del producto")

  precio_final_producto = precio - (precio*descuento)

  st.write("EL precio final de producto es: ",precio_final_prodcuto)

elif sesion == "Sesión 3":
  st.write("Bienvenido a la sesión 3")

else: 
  st.write("Bienvenido a la sesión 4")














  
