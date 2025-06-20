import streamlit as st
import base64

def mostrar_contenido():
    st.markdown("<h2 class='module-header'>Introducción a Git</h2>", unsafe_allow_html=True)
    
    # Tabs para organizar el contenido
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["¿Qué es Git?", "Conceptos Básicos", "Instalación", "Configuración", "Quiz"])
    
    with tab1:
        st.markdown("### ¿Qué es Git y por qué deberías usarlo?")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            **Git** es un sistema de control de versiones distribuido diseñado para rastrear cambios en el código fuente durante el desarrollo de software.
            
            Fue creado por **Linus Torvalds** en 2005 para el desarrollo del kernel de Linux, y desde entonces se ha convertido en el estándar de la industria.
            
            <div class='highlight'>
            A diferencia de los sistemas centralizados, Git permite que cada desarrollador tenga una copia completa del historial del proyecto,
            lo que facilita el trabajo sin conexión y la colaboración descentralizada.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### Ventajas de Git:")
            st.markdown("""
            - 🚀 **Velocidad**: Las operaciones son rápidas y eficientes
            - 🌿 **Ramificación simplificada**: Crear y fusionar ramas es sencillo
            - 🔄 **Trabajo sin conexión**: No requiere conexión constante a un servidor
            - 🔍 **Integridad**: Todo en Git tiene un checksum para prevenir corrupción
            - 📊 **Sistema distribuido**: Todos tienen una copia completa del repositorio
            """)
        
        with col2:
            # Diagrama conceptual de Git (se usaría una imagen real en producción)
            st.image("https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png", width=200)
            
            st.markdown("""
            <div class='tip'>
            <b>¿Sabías que?</b> El nombre "Git" puede interpretarse como "tonto" en inglés británico. 
            Linus Torvalds bromeó diciendo: "Soy un ego tan grande que llamo a todos mis proyectos con mi nombre. 
            Primero Linux, ahora Git".
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Conceptos Básicos de Git")
        
        st.markdown("""
        Para entender Git, es importante familiarizarse con estos conceptos fundamentales:
        """)
        
        # Acordeón para conceptos
        with st.expander("💾 **Repositorio**"):
            st.markdown("""
            Un repositorio (o "repo") es como una carpeta de proyecto que contiene todos los archivos y el historial completo de cambios.
            
            **Repositorio Local**: Ubicado en tu computadora.  
            **Repositorio Remoto**: Ubicado en un servidor (como GitHub, GitLab, etc.).
            """)
        
        with st.expander("📝 **Commit**"):
            st.markdown("""
            Un commit es una "fotografía" de tu proyecto en un momento específico. Cada commit tiene:
            - Un identificador único (hash SHA-1)
            - Un mensaje descriptivo
            - Información sobre quién y cuándo lo creó
            - Referencia al commit anterior (excepto el primer commit)
            """)
            
            st.code("""
            # Ejemplo de cómo se hace un commit
            git add archivo.txt
            git commit -m "Añadir archivo de configuración inicial"
            """)
        
        with st.expander("🌿 **Rama (Branch)**"):
            st.markdown("""
            Una rama es una línea independiente de desarrollo. La rama principal suele llamarse `main` o `master`.
            
            Las ramas permiten:
            - Trabajar en características sin afectar el código principal
            - Experimentar con cambios que podrían descartarse
            - Colaborar en equipos sin interferir con el trabajo de otros
            """)
            
            st.code("""
            # Crear y cambiar a una nueva rama
            git branch nueva-caracteristica
            git checkout nueva-caracteristica
            
            # O en un solo comando
            git checkout -b nueva-caracteristica
            """)
        
        with st.expander("🔄 **Fusión (Merge)**"):
            st.markdown("""
            El proceso de combinar cambios de una rama a otra.
            
            ```
            # Fusionar la rama 'caracteristica' en 'main'
            git checkout main
            git merge caracteristica
            ```
            """)
        
        with st.expander("📊 **Áreas de Git**"):
            st.markdown("""
            Git maneja los archivos en tres áreas principales:
            
            1. **Directorio de trabajo**: Donde editas los archivos
            2. **Área de preparación (staging)**: Donde preparas los cambios para el próximo commit
            3. **Repositorio Git**: Donde se almacenan los cambios confirmados
            
            El flujo típico es:
            - Modificar archivos en el directorio de trabajo
            - Preparar cambios con `git add`
            - Confirmar cambios con `git commit`
            """)
            
            # Aquí iría un diagrama del flujo de trabajo de Git
            st.image("https://git-scm.com/book/en/v2/images/areas.png", caption="Las tres áreas de Git")
    
    with tab3:
        st.markdown("### Instalación de Git")
        
        # Pestañas para diferentes sistemas operativos
        os_tab1, os_tab2, os_tab3 = st.tabs(["Windows", "macOS", "Linux"])
        
        with os_tab1:
            st.markdown("""
            #### Instalación en Windows
            
            1. Descarga el instalador desde [git-scm.com](https://git-scm.com/download/win)
            2. Ejecuta el instalador y sigue las instrucciones
            3. Puedes aceptar las opciones predeterminadas o personalizarlas según tus necesidades
            
            Una vez instalado, puedes verificar la instalación abriendo Git Bash o CMD y ejecutando:
            ```
            git --version
            ```
            """)
            
            st.warning("Asegúrate de tener permisos de administrador para instalar software en Windows.")
        
        with os_tab2:
            st.markdown("""
            #### Instalación en macOS
            
            **Opción 1: Homebrew**
            
            Si tienes [Homebrew](https://brew.sh/) instalado:
            ```
            brew install git
            ```
            
            **Opción 2: Instalador**
            
            1. Descarga el instalador desde [git-scm.com](https://git-scm.com/download/mac)
            2. Sigue las instrucciones del instalador
            
            **Opción 3: Xcode Command Line Tools**
            
            ```
            xcode-select --install
            ```
            
            Verifica la instalación:
            ```
            git --version
            ```
            """)
        
        with os_tab3:
            st.markdown("""
            #### Instalación en Linux
            
            **Debian/Ubuntu**:
            ```
            sudo apt-get update
            sudo apt-get install git
            ```
            
            **Fedora**:
            ```
            sudo dnf install git
            ```
            
            **Arch Linux**:
            ```
            sudo pacman -S git
            ```
            
            Verifica la instalación:
            ```
            git --version
            ```
            """)
        
        st.success("¡Git es multiplataforma! Funciona igual en Windows, macOS y Linux.")
    
    with tab4:
        st.markdown("### Configuración Inicial de Git")
        
        st.markdown("""
        Después de instalar Git, debes configurar tu identidad. Esto es importante porque cada commit usará esta información:
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Configuración Global")
            
            st.code("""
            # Configurar nombre de usuario
            git config --global user.name "Tu Nombre"
            
            # Configurar correo electrónico
            git config --global user.email "tu.email@ejemplo.com"
            """)
            
            st.markdown("""
            <div class='tip'>
            Usa la misma dirección de correo electrónico que utilizas en GitHub u otros servicios de alojamiento de Git.
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### Configuración Opcional")
            
            st.code("""
            # Configurar editor predeterminado
            git config --global core.editor "code --wait"  # VS Code
            
            # Configurar herramienta de diferencias
            git config --global diff.tool "vscode"
            
            # Alias útiles
            git config --global alias.co checkout
            git config --global alias.br branch
            git config --global alias.st status
            """)
        
        st.markdown("#### Verificar Configuración")
        
        st.code("""
        # Ver todas las configuraciones
        git config --list
        
        # Ver una configuración específica
        git config user.name
        """)
        
        # Widget interactivo para practicar la configuración
        st.markdown("### Practica la configuración")
        
        nombre = st.text_input("Tu nombre para Git:", placeholder="Ejemplo: María García")
        email = st.text_input("Tu correo electrónico para Git:", placeholder="ejemplo@correo.com")
        
        if nombre and email:
            st.code(f"""
            git config --global user.name "{nombre}"
            git config --global user.email "{email}"
            """)
            
            if st.button("Copiar comandos"):
                st.success("¡Comandos copiados al portapapeles!")
    
    with tab5:
        st.markdown("<h3 class='subheader'>Quiz: Introducción a Git</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        Pon a prueba tus conocimientos con este pequeño cuestionario:
        """)
        
        # Pregunta 1
        q1 = st.radio(
            "1. ¿Quién creó Git?",
            ["Richard Stallman", "Linus Torvalds", "Guido van Rossum", "Mark Zuckerberg"]
        )
        
        # Pregunta 2
        q2 = st.radio(
            "2. ¿Cuál de las siguientes NO es una ventaja de Git?",
            [
                "Permite trabajar sin conexión a internet", 
                "Facilita la creación y fusión de ramas", 
                "Requiere un servidor central siempre activo",
                "Mantiene un historial completo de cambios"
            ]
        )
        
        # Pregunta 3
        q3 = st.radio(
            "3. ¿Qué comando usarías para configurar tu nombre de usuario en Git?",
            [
                "git username set 'Mi Nombre'",
                "git set --user 'Mi Nombre'",
                "git config --global user.name 'Mi Nombre'",
                "git --config name 'Mi Nombre'"
            ]
        )
        
        # Pregunta 4
        q4 = st.radio(
            "4. ¿Qué es un repositorio en Git?",
            [
                "Solo el servidor donde se aloja el código", 
                "Una carpeta de proyecto que contiene los archivos y el historial de cambios",
                "Un backup manual del código",
                "La interfaz gráfica de Git"
            ]
        )
        
        # Pregunta 5
        q5 = st.radio(
            "5. ¿Cuál es el comando para verificar la versión de Git instalada?",
            [
                "git --ver",
                "git check version",
                "git --version",
                "git -v"
            ]
        )
        
        # Botón para verificar respuestas
        if st.button("Verificar Respuestas"):
            score = 0
            
            if q1 == "Linus Torvalds":
                score += 1
            
            if q2 == "Requiere un servidor central siempre activo":
                score += 1
                
            if q3 == "git config --global user.name 'Mi Nombre'":
                score += 1
                
            if q4 == "Una carpeta de proyecto que contiene los archivos y el historial de cambios":
                score += 1
                
            if q5 == "git --version":
                score += 1
            
            st.success(f"¡Obtuviste {score} de 5 respuestas correctas!")
            
            if score == 5:
                st.balloons()
                st.markdown("### 🏆 ¡Perfecto! Dominas los conceptos básicos de Git.")
            elif score >= 3:
                st.markdown("### 👍 ¡Buen trabajo! Estás en el camino correcto.")
            else:
                st.markdown("### 📚 Revisa nuevamente el material para reforzar tus conocimientos.")

# Función para convertir una imagen a base64 (para incrustar imágenes)
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')
