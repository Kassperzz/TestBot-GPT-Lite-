import streamlit as st
import os
from utils.test_generator import generate_tests
from utils.report_formatter import format_report
from utils.file_handler import extract_zip, collect_source_files, read_files
import time

# ======================
# CONFIGURACIÓN GENERAL
# ======================
st.set_page_config(page_title="TestBot-GPT", page_icon="🤖", layout="wide")

st.title("🤖 TestBot-GPT")
st.subheader("Tu asistente local para generar pruebas de software con IA (Ollama)")

st.markdown("""
Esta es la versión **Lite** de *TestBot-GPT*, pensada para estudiantes y testers junior.  
Funciona **completamente offline** usando Ollama local.  
Puedes ingresar tu código manualmente o subir un **.zip** con tu proyecto.
""")

# ======================
# OPCIONES DE ENTRADA
# ======================
tab1, tab2 = st.tabs(["🧾 Texto manual", "📦 Proyecto .zip"])

# --- Entrada de texto ---
with tab1:
    user_input = st.text_area("✏️ Ingresa tu código o descripción:", height=200)

    if st.button("🚀 Generar pruebas (texto manual)"):
        if not user_input.strip():
            st.warning("Por favor ingresa una descripción o fragmento de código.")
        else:
            with st.spinner("Generando casos de prueba..."):
                try:
                    raw_output = generate_tests(user_input)
                    report = format_report(raw_output)
                    st.success("✅ Pruebas generadas exitosamente.")
                    st.code(report, language="python")
                except Exception as e:
                    st.error(f"Ocurrió un error: {e}")

# --- Subida de ZIP ---
with tab2:
    uploaded_zip = st.file_uploader("📦 Sube tu archivo .zip", type=["zip"])
    if uploaded_zip:
        with st.spinner("📂 Procesando el proyecto..."):
            try:
                # Extraer y leer archivos
                folder_path = extract_zip(uploaded_zip, extract_to="temp_project")
                source_files = collect_source_files(folder_path)
                project_text = read_files(source_files)

                st.info(f"Se analizarán {len(source_files)} archivos del proyecto.")

                if st.button("🚀 Generar pruebas (proyecto completo)"):
                    progress = st.progress(0, text="⚙️ Analizando y generando pruebas...")
                    status_text = st.empty()

                    try:
                        # Simulación visual de progreso mientras se genera
                        for i in range(0, 80, 5):
                            progress.progress(i, text=f"🧠 Procesando archivos... {i}%")
                            time.sleep(0.2)  # ajusta según tu CPU

                        # Llamada real a Ollama
                        raw_output = generate_tests(project_text, file_paths=source_files)

                        # Avance final durante formateo
                        for i in range(80, 101, 5):
                            progress.progress(i, text=f"✅ Generando resultado... {i}%")
                            time.sleep(0.1)

                        report = format_report(raw_output)
                        progress.empty()
                        status_text.success("✅ Pruebas generadas exitosamente.")
                        st.code(report, language="python")

                    except Exception as e:
                        progress.empty()
                        st.error(f"Ocurrió un error: {e}")

            except Exception as e:
                st.error(f"Ocurrió un error al procesar el ZIP: {e}")

st.markdown("---")
st.markdown("<small>Hecho por Kasperzzz</small>", unsafe_allow_html=True)
