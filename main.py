import streamlit as st
import os
import sys

# Agregar la ruta del proyecto al path para importar módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar los módulos del curso
from modulos import intro, commits, branches, remote, merge_conflicts, github_workflow, evaluacion_final

# Configuración de la página
st.set_page_config(
    page_title="Curso Interactivo de Git y GitHub",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #0F9D58;
        text-align: center;
        margin-bottom: 1rem;
    }
    .module-header {
        font-size: 1.8rem;
        color: #1E88E5;
        margin-top: 1rem;
    }
    .subheader {
        font-size: 1.5rem;
        color: #4285F4;
    }
    .highlight {
        background-color: #F1F8E9;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #0F9D58;
    }
    .tip {
        background-color: #E3F2FD;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #1E88E5;
    }
    .warning {
        background-color: #FFF8E1;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #FFC107;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#4CAF50,#2E7D32);
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 class='main-header'>Curso Interactivo de Git y GitHub</h1>", unsafe_allow_html=True)

# Función para mostrar información del autor y la versión
def show_about():
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **Curso de Git y GitHub**  
    Versión: 1.0.0  
    Desarrollado con Streamlit  
    © 2025
    """)

# Sidebar para navegación
st.sidebar.title("Navegación")
modulo = st.sidebar.radio(
    "Selecciona un módulo:",
    ["Introducción a Git", 
     "Commits y Control de Versiones", 
     "Ramas y Fusiones", 
     "Repositorios Remotos", 
     "Resolución de Conflictos", 
     "Flujo de Trabajo en GitHub",
     "Evaluación Final"]
)

# Mostrar progreso
progress_options = {
    "Introducción a Git": 1,
    "Commits y Control de Versiones": 2,
    "Ramas y Fusiones": 3,
    "Repositorios Remotos": 4,
    "Resolución de Conflictos": 5,
    "Flujo de Trabajo en GitHub": 6,
    "Evaluación Final": 7
}

total_modules = 7
current_progress = progress_options[modulo]
progress_percentage = current_progress / total_modules

st.sidebar.progress(progress_percentage)
st.sidebar.text(f"Progreso: {int(progress_percentage * 100)}%")

# Mostrar el módulo seleccionado
if modulo == "Introducción a Git":
    intro.mostrar_contenido()
elif modulo == "Commits y Control de Versiones":
    commits.mostrar_contenido()
elif modulo == "Ramas y Fusiones":
    branches.mostrar_contenido()
elif modulo == "Repositorios Remotos":
    remote.mostrar_contenido()
elif modulo == "Resolución de Conflictos":
    merge_conflicts.mostrar_contenido()
elif modulo == "Flujo de Trabajo en GitHub":
    github_workflow.mostrar_contenido()
elif modulo == "Evaluación Final":
    evaluacion_final.mostrar_contenido()

# Información adicional en el sidebar
show_about()

# Footer
st.markdown("---")
st.markdown("Desarrollado por Daniel Mardones, desarrolador Python y DataScientist.")
