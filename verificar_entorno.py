import streamlit as st
import os
import platform
import sys

st.set_page_config(
    page_title="Verificación de Entorno",
    page_icon="✅",
    layout="wide"
)

st.title("Verificación de Entorno para Despliegue")

st.markdown("### Información del Sistema")
col1, col2 = st.columns(2)

with col1:
    st.write(f"**Python Versión:** {platform.python_version()}")
    st.write(f"**Sistema Operativo:** {platform.system()} {platform.release()}")
    st.write(f"**Directorio de Trabajo:** {os.getcwd()}")

with col2:
    st.write(f"**Streamlit Versión:** {st.__version__}")
    st.write(f"**Python Path:** {sys.executable}")

st.markdown("### Verificación de Archivos")

required_files = [
    "main.py",
    "requirements.txt",
    ".streamlit/config.toml",
    "setup.sh",
    "Procfile",
    "runtime.txt"
]

modules = [f"modulos/{m}" for m in [
    "intro.py", 
    "commits.py", 
    "branches.py", 
    "remote.py", 
    "merge_conflicts.py", 
    "github_workflow.py", 
    "evaluacion_final.py"
]]

all_files = required_files + modules

for file in all_files:
    if os.path.exists(file):
        st.success(f"✅ {file} encontrado")
    else:
        st.error(f"❌ {file} no encontrado")

st.markdown("### Verificación de Dependencias")

try:
    import pandas
    st.success(f"✅ pandas {pandas.__version__} instalado")
except ImportError:
    st.error("❌ pandas no instalado")

try:
    import matplotlib
    st.success(f"✅ matplotlib {matplotlib.__version__} instalado")
except ImportError:
    st.error("❌ matplotlib no instalado")

try:
    import PIL
    st.success(f"✅ pillow {PIL.__version__} instalado")
except ImportError:
    st.error("❌ pillow no instalado")

try:
    import numpy
    st.success(f"✅ numpy {numpy.__version__} instalado")
except ImportError:
    st.error("❌ numpy no instalado")

st.markdown("### Todo listo para el despliegue")
st.success("""
Si todos los archivos necesarios están presentes y las dependencias están instaladas, 
tu aplicación está lista para ser desplegada en Streamlit Community Cloud.

Asegúrate de que tu repositorio esté público en GitHub para poder desplegarlo.
""")
