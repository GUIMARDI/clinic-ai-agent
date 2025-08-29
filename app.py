import streamlit as st
from utils.llm import resume_historial
from utils.calendar import agendar_cita

st.set_page_config(page_title="ClinicAI Assistant", page_icon="🏥")

st.title("🏥 ClinicAI - Resumen + Citas")

# Subir PDF
uploaded_file = st.file_uploader("Sube el historial médico (PDF)", type="pdf")
if uploaded_file:
    with st.spinner("Analizando..."):
        resumen = resume_historial(uploaded_file)
    st.success("✅ Resumen generado:")
    st.write(resumen)

    # Agendar cita
    fecha = st.date_input("Selecciona fecha")
    hora = st.time_input("Selecciona hora")
    if st.button("Agendar cita"):
        agendar_cita(fecha, hora)
        st.balloons()
        st.success("Cita agendada con Google Calendar")
