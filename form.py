import streamlit as st
st.title("formulario de registro Estudiantil IP-2026")

nombre = st.text_input("Nombre Completo")
edad=st.number_input("Edad", min_value=0, max_value=80)
carrera=st.selectbox("carrera", ["Ingenieria en computacion", "Diseño wed", "tecnico en Informatica"])
comantario=st.text_area("Comantario adicional(opcional)")

if st.button("Enviar"):
    st.write("##Datos Registrados:")
    st.write(f"**nombre Completo** : {nombre}")
    st.write(f"**edad**: {edad}")
    st.write(f"**Carrera** : {carrera}")
    st.write(F"**Comentario** :{comentario}")
    st.success(f"**Formulario Enviado con Exito")