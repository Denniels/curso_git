import streamlit as st

def mostrar_contenido():
    st.markdown("<h2 class='module-header'>Flujo de Trabajo en GitHub</h2>", unsafe_allow_html=True)
    
    # Tabs para organizar el contenido
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Introducción a GitHub", "Forks y Pull Requests", "Colaboración Efectiva", "Buenas Prácticas", "Quiz"])
    
    with tab1:
        st.markdown("### GitHub: Más que un Repositorio Git")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            **GitHub** es una plataforma web que proporciona alojamiento para repositorios Git y añade características adicionales
            para la colaboración y gestión de proyectos de software.
            
            <div class='highlight'>
            GitHub facilita la colaboración en proyectos open source y privados, implementando un flujo de trabajo basado en ramas,
            forks y pull requests que ha revolucionado el desarrollo colaborativo.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            #### Características principales de GitHub:
            
            - 📋 **Issues**: Sistema de seguimiento de tareas, bugs y mejoras
            - 🔄 **Pull Requests**: Proponer, revisar y discutir cambios
            - 🔍 **Code Review**: Revisiones de código colaborativas
            - 📊 **Project Boards**: Gestión de proyectos tipo Kanban
            - 📅 **Milestones**: Agrupación de issues por objetivos
            - 🔔 **Notifications**: Sistema de alertas para actividades
            - 📝 **Wiki**: Documentación colaborativa
            - 📈 **Insights**: Métricas y análisis del proyecto
            - 🚀 **Actions**: Automatización de CI/CD y workflows
            - 🛡️ **Security**: Análisis de vulnerabilidades
            """)
        
        with col2:
            # Imagen de GitHub
            st.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=200)
            
            st.markdown("""
            <div class='tip'>
            <b>¿Sabías que?</b> GitHub fue adquirido por Microsoft en 2018 por 7.500 millones de dólares,
            pero mantiene su independencia operativa.
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### GitHub vs. Git")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Git
            
            - Sistema de control de versiones distribuido
            - Software de línea de comandos
            - Funciona localmente (no requiere internet)
            - Enfocado en tracking de cambios y ramas
            - Creado por Linus Torvalds para Linux
            """)
        
        with col2:
            st.markdown("""
            #### GitHub
            
            - Plataforma web basada en Git
            - Interfaz gráfica + API
            - Servicios en la nube (requiere internet)
            - Enfocado en colaboración y gestión de proyectos
            - Creado por Tom Preston-Werner, Chris Wanstrath y PJ Hyett
            """)
        
        # Interfaz de GitHub
        st.markdown("### Interfaz de GitHub")
        
        st.markdown("""
        Familiarizarse con la interfaz de GitHub es esencial para trabajar en equipo:
        """)
        
        # Navegación principal
        with st.expander("🧭 Navegación Principal"):
            st.markdown("""
            La barra de navegación superior contiene:
            
            - **Barra de búsqueda**: Buscar repositorios, código, usuarios
            - **Pull requests**: Ver PRs asignados o creados por ti
            - **Issues**: Ver issues asignados o creados por ti
            - **Notifications** (campana): Ver notificaciones pendientes
            - **New** (signo +): Crear nuevo repositorio, organización, etc.
            - **Perfil**: Acceder a tu perfil, configuraciones, etc.
            """)
        
        # Página de repositorio
        with st.expander("📁 Página de Repositorio"):
            st.markdown("""
            La página principal de un repositorio contiene:
            
            - **Code**: Explorador de archivos del repositorio
            - **Issues**: Sistema de tickets para tareas/bugs
            - **Pull requests**: Propuestas de cambios
            - **Actions**: Configuración de CI/CD y automatizaciones
            - **Projects**: Tableros Kanban para gestión
            - **Wiki**: Documentación del proyecto
            - **Security**: Análisis de vulnerabilidades
            - **Insights**: Estadísticas del proyecto
            - **Settings**: Configuración del repositorio (para admins)
            
            Además, la página principal muestra:
            
            - README.md renderizado
            - Estadísticas (estrellas, forks, etc.)
            - Información sobre el último commit
            - Lista de contribuidores
            """)
        
        # Explorador de código
        with st.expander("🔍 Explorador de Código"):
            st.markdown("""
            Al navegar por el código, puedes:
            
            - Ver archivos y carpetas organizados jerárquicamente
            - Leer el contenido de los archivos con resaltado de sintaxis
            - Ver el historial de cambios de un archivo (botón "History")
            - Editar archivos directamente en el navegador
            - Navegar entre ramas y tags
            - Buscar en el repositorio
            - Ver y descargar versiones específicas (releases)
            """)
        
        # Simulador de creación de cuenta
        st.markdown("### Primeros Pasos en GitHub")
        
        st.markdown("""
        Para comenzar a utilizar GitHub, necesitas:
        
        1. **Crear una cuenta** en [github.com](https://github.com)
        2. **Configurar tu perfil**
        3. **Configurar SSH** o tokens de acceso personal
        4. **Crear o clonar** un repositorio
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Configurar Git para GitHub")
            
            st.code("""
            # Configurar nombre de usuario
            git config --global user.name "Tu Nombre"
            
            # Configurar email (usa el mismo de tu cuenta GitHub)
            git config --global user.email "tu.email@ejemplo.com"
            
            # Configurar autenticación (recomendado: SSH)
            # 1. Generar clave SSH
            ssh-keygen -t ed25519 -C "tu.email@ejemplo.com"
            
            # 2. Añadir clave a agente SSH
            eval "$(ssh-agent -s)"
            ssh-add ~/.ssh/id_ed25519
            
            # 3. Copiar clave pública
            cat ~/.ssh/id_ed25519.pub
            # (Añadir esta clave en GitHub > Settings > SSH and GPG keys)
            """)
        
        with col2:
            st.markdown("#### Crear un repositorio")
            
            st.markdown("""
            **Desde la web:**
            
            1. Haz clic en "+" en la esquina superior derecha
            2. Selecciona "New repository"
            3. Completa la información:
               - Nombre del repositorio
               - Descripción (opcional)
               - Público o privado
               - Inicializar con README (recomendado)
            4. Haz clic en "Create repository"
            
            **Desde un proyecto existente:**
            
            ```bash
            # En la carpeta de tu proyecto
            git init
            git add .
            git commit -m "Initial commit"
            git branch -M main
            git remote add origin git@github.com:username/repo.git
            git push -u origin main
            ```
            """)
    
    with tab2:
        st.markdown("### Forks y Pull Requests")
        
        st.markdown("""
        El flujo de trabajo basado en **forks** y **pull requests** es uno de los conceptos más importantes
        para colaborar en proyectos de GitHub, especialmente en proyectos open source.
        """)
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("#### ¿Qué es un Fork?")
            
            st.markdown("""
            Un **fork** es una copia personal de un repositorio de otra persona u organización.
            
            - Se aloja en tu cuenta de GitHub
            - Te permite experimentar libremente sin afectar el proyecto original
            - Mantiene una conexión con el repositorio original (upstream)
            - Es el primer paso para contribuir a proyectos ajenos
            
            <div class='highlight'>
            El fork te da una "zona de pruebas" segura para trabajar antes de proponer cambios al proyecto original.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### ¿Qué es un Pull Request?")
            
            st.markdown("""
            Un **pull request (PR)** es una propuesta para integrar cambios de una rama a otra, normalmente
            desde tu fork al repositorio original.
            
            - Permite a los mantenedores revisar tus cambios
            - Proporciona un espacio para discusión y feedback
            - Puede ser actualizado con nuevos commits
            - Puede incluir múltiples archivos y commits
            - Puede pasar por pruebas automatizadas (CI/CD)
            
            <div class='highlight'>
            El pull request es el mecanismo principal para la revisión de código colaborativa en GitHub.
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Imagen de flujo de fork y PR
            st.image("https://docs.github.com/assets/cb-23923/mw-1000/images/help/pull_requests/pull-request-fork-branch-merge.webp", caption="Flujo de Fork y Pull Request")
            
            st.markdown("""
            <div class='tip'>
            <b>Terminología importante:</b>
            
            - <b>Upstream</b>: El repositorio original del que hiciste fork
            - <b>Origin</b>: Tu fork del repositorio
            - <b>Base branch</b>: Rama destino para tus cambios (ej. main)
            - <b>Head branch</b>: Rama con tus cambios
            </div>
            """, unsafe_allow_html=True)
        
        # El flujo de trabajo con fork y PR
        st.markdown("### El Flujo de Trabajo Completo")
        
        st.markdown("""
        A continuación se muestra el flujo completo para contribuir a un proyecto usando fork y pull request:
        """)
        
        # Diagrama de flujo
        col1, col2, col3 = st.columns([1, 3, 1])
        
        with col2:
            st.markdown("""
            1. **Fork** del repositorio original → **Tu fork**
            2. **Clone** de tu fork a tu máquina local
            3. Crear una **rama de características**
            4. Realizar **cambios** y commits
            5. **Push** de la rama a tu fork
            6. Crear un **Pull Request** al repositorio original
            7. Responder a la **revisión de código**
            8. Los mantenedores **fusionan** tu PR
            9. **Sincronizar** tu fork con el repositorio original
            """)
        
        # Acordeón para los pasos detallados
        with st.expander("1️⃣ Hacer Fork y Clonar"):
            st.markdown("""
            **Paso 1: Hacer fork del repositorio**
            
            1. Navega al repositorio que quieres contribuir
            2. Haz clic en el botón "Fork" en la esquina superior derecha
            3. Selecciona tu cuenta como destino
            
            **Paso 2: Clonar tu fork localmente**
            
            ```bash
            # Reemplaza USERNAME y REPO con los valores correctos
            git clone https://github.com/USERNAME/REPO.git
            cd REPO
            
            # Añadir el repositorio original como "upstream"
            git remote add upstream https://github.com/ORIGINAL-OWNER/REPO.git
            
            # Verificar los remotos configurados
            git remote -v
            # origin    https://github.com/USERNAME/REPO.git (fetch)
            # origin    https://github.com/USERNAME/REPO.git (push)
            # upstream  https://github.com/ORIGINAL-OWNER/REPO.git (fetch)
            # upstream  https://github.com/ORIGINAL-OWNER/REPO.git (push)
            ```
            """)
        
        with st.expander("2️⃣ Crear Rama y Hacer Cambios"):
            st.markdown("""
            **Paso 3: Crear una rama para tus cambios**
            
            ```bash
            # Asegúrate de estar actualizado con upstream
            git fetch upstream
            git checkout main
            git merge upstream/main
            
            # Crear una nueva rama
            git checkout -b feature/mi-nueva-caracteristica
            ```
            
            **Paso 4: Hacer cambios y commits**
            
            ```bash
            # Hacer cambios en los archivos...
            
            # Añadir los cambios
            git add .
            
            # Hacer commit con un mensaje descriptivo
            git commit -m "Añadir nueva funcionalidad para X"
            
            # Si es necesario, hacer más cambios y commits...
            ```
            """)
        
        with st.expander("3️⃣ Push y Crear Pull Request"):
            st.markdown("""
            **Paso 5: Push de tu rama a tu fork**
            
            ```bash
            git push origin feature/mi-nueva-caracteristica
            ```
            
            **Paso 6: Crear un Pull Request**
            
            1. Ve a tu fork en GitHub
            2. Deberías ver un banner sugiriendo crear un PR, o puedes ir a la pestaña "Pull requests"
            3. Haz clic en "New pull request"
            4. Asegúrate de que:
               - Base repository: el repositorio original
               - Base branch: main (o la rama correcta)
               - Head repository: tu fork
               - Compare branch: feature/mi-nueva-caracteristica
            5. Haz clic en "Create pull request"
            6. Añade un título descriptivo
            7. Añade una descripción detallada (qué, por qué, cómo)
            8. Haz clic en "Create pull request"
            """)
        
        with st.expander("4️⃣ Revisión y Actualizaciones"):
            st.markdown("""
            **Paso 7: Responder a la revisión de código**
            
            1. Los mantenedores revisarán tu PR y pueden solicitar cambios
            2. Puedes ver los comentarios en la interfaz de GitHub
            
            **Para actualizar tu PR con cambios adicionales:**
            
            ```bash
            # Asegúrate de estar en tu rama de características
            git checkout feature/mi-nueva-caracteristica
            
            # Hacer más cambios
            # ...
            
            # Añadir y hacer commit
            git add .
            git commit -m "Ajustar X según revisión"
            
            # Push de los nuevos cambios
            git push origin feature/mi-nueva-caracteristica
            ```
            
            El PR se actualizará automáticamente con tus nuevos commits.
            """)
        
        with st.expander("5️⃣ Fusión y Sincronización"):
            st.markdown("""
            **Paso 8: Fusión del Pull Request**
            
            Una vez que tu PR es aprobado, los mantenedores lo fusionarán con el repositorio principal.
            
            **Paso 9: Sincronizar tu fork**
            
            Después de que tu PR sea fusionado, debes actualizar tu fork:
            
            ```bash
            # Cambiar a la rama principal
            git checkout main
            
            # Obtener los cambios del repositorio original
            git fetch upstream
            
            # Fusionar los cambios a tu rama local
            git merge upstream/main
            
            # Actualizar tu fork en GitHub
            git push origin main
            
            # Opcional: eliminar tu rama de características
            git branch -d feature/mi-nueva-caracteristica
            git push origin --delete feature/mi-nueva-caracteristica
            ```
            """)
        
        # Simulador de Pull Request
        st.markdown("### Simulador de Pull Request")
        
        pr_title = st.text_input("Título del Pull Request:", placeholder="Añadir función de búsqueda avanzada")
        
        pr_description = st.text_area(
            "Descripción del Pull Request:",
            placeholder="## Cambios realizados\n\n- Añadida nueva función de búsqueda\n- Mejorada la interfaz de usuario\n\n## Por qué es necesario\n\nLos usuarios necesitaban una forma más eficiente de...",
            height=150
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            base_repo = st.text_input("Repositorio base (upstream):", value="original/proyecto")
            base_branch = st.selectbox("Rama base:", ["main", "develop", "staging"])
        
        with col2:
            head_repo = st.text_input("Tu fork:", value="tu-usuario/proyecto")
            head_branch = st.text_input("Tu rama:", value="feature/nueva-funcionalidad")
        
        if st.button("Crear Pull Request (Simulación)"):
            if pr_title and pr_description:
                st.success(f"¡Pull Request '{pr_title}' creado exitosamente!")
                
                st.markdown(f"""
                ### Pull Request: {pr_title}
                
                **De:** `{head_repo}:{head_branch}`  
                **A:** `{base_repo}:{base_branch}`
                
                ---
                
                {pr_description}
                
                ---
                
                **Estado:** Abierto  
                **Revisores:** Sin asignar  
                """)
                
                st.info("En un PR real, podrías asignar revisores, etiquetas, proyectos y milestones.")
            else:
                st.error("Por favor, completa al menos el título y la descripción.")
    
    with tab3:
        st.markdown("### Colaboración Efectiva en GitHub")
        
        st.markdown("""
        GitHub ofrece numerosas herramientas para facilitar la colaboración en equipo más allá de los pull requests.
        """)
        
        # Issues
        with st.expander("🎫 Issues: Gestión de Tareas y Bugs"):
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.markdown("""
                Los **Issues** son el sistema de tickets de GitHub para rastrear tareas, mejoras, bugs y cualquier tipo de tarea pendiente.
                
                **Características principales:**
                
                - Títulos y descripciones con soporte Markdown
                - Etiquetas personalizables (bugs, mejoras, etc.)
                - Asignación a responsables
                - Milestones para agrupar por objetivos
                - Referencia automática a otros issues o PRs
                - Comentarios para discusión
                - Estado abierto/cerrado
                - Plantillas personalizables
                
                **Buenas prácticas:**
                
                - Usa títulos claros y descriptivos
                - Incluye pasos para reproducir bugs
                - Añade capturas de pantalla o GIFs si es posible
                - Usa etiquetas consistentemente
                - Cierra issues con mensajes de commit cuando sea apropiado
                """)
            
            with col2:
                st.markdown("""
                <div class='tip'>
                <b>Consejo Pro:</b> Puedes cerrar automáticamente issues con mensajes de commit usando palabras clave como "Fixes", "Closes", o "Resolves" seguido del número de issue.
                
                Ejemplo:
                <pre>git commit -m "Añadir validación de formulario. Fixes #42"</pre>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div class='highlight'>
                <b>Plantillas de Issues</b>
                
                Puedes crear plantillas en <code>.github/ISSUE_TEMPLATE/</code> para estandarizar la información.
                </div>
                """, unsafe_allow_html=True)
        
        # Revisiones de código
        with st.expander("🔍 Code Reviews: La Clave para la Calidad"):
            st.markdown("""
            Las **revisiones de código** son fundamentales para mantener la calidad y compartir conocimiento en el equipo.
            
            **En GitHub, puedes:**
            
            - Revisar archivos específicos o todo el PR
            - Añadir comentarios en líneas específicas
            - Sugerir cambios exactos (con botón de aplicar)
            - Aprobar o solicitar cambios formalmente
            - Marcar comentarios como resueltos
            
            **Tipos de revisión:**
            
            1. **Comment**: Feedback general sin aprobación/rechazo
            2. **Approve**: Aprobación para fusionar
            3. **Request changes**: Requiere correcciones antes de fusionar
            
            **Buenas prácticas como revisor:**
            
            - Sé respetuoso y constructivo
            - Explica el "por qué", no solo el "qué"
            - Diferencia entre sugerencias importantes y preferencias de estilo
            - Menciona lo bueno, no solo lo que hay que corregir
            - Sé oportuno en tus revisiones
            
            **Buenas prácticas como autor:**
            
            - Haz PRs pequeños y enfocados
            - Añade descripciones detalladas
            - Responde a todos los comentarios
            - No te tomes las críticas personalmente
            - Aprovecha para aprender
            """)
            
            st.image("https://docs.github.com/assets/cb-42604/mw-1000/images/help/pull_requests/pull-request-review-view-changes.webp", caption="Interfaz de revisión de código en GitHub")
        
        # Discussions
        with st.expander("💬 Discussions: Conversaciones Estructuradas"):
            st.markdown("""
            **GitHub Discussions** es una característica que proporciona un espacio para conversaciones que no encajan bien como issues o pull requests.
            
            **Ideal para:**
            
            - Preguntas y respuestas
            - Anuncios y noticias
            - Ideas y feedback
            - Mostrar y compartir proyectos
            - Debates generales sobre el proyecto
            
            **Características:**
            
            - Categorías personalizables
            - Marcado de respuestas como solución
            - Votación de respuestas
            - Formato Markdown completo
            - Conversaciones anidadas
            
            **Para activar Discussions:**
            
            1. Ve a tu repositorio
            2. Pestaña Settings
            3. Sección "Features"
            4. Marca la opción "Discussions"
            
            Es especialmente útil para proyectos de código abierto con comunidades activas o proyectos internos que requieren discusiones más estructuradas que las issues.
            """)
        
        # Project Boards
        with st.expander("📋 Project Boards: Gestión Visual"):
            st.markdown("""
            Los **Project Boards** de GitHub son tableros Kanban para gestionar y priorizar el trabajo de forma visual.
            
            **Tipos de proyectos:**
            
            - **Proyectos clásicos**: Dentro de un repositorio o a nivel de organización
            - **Proyectos (beta)**: Nueva experiencia con más flexibilidad
            
            **Características:**
            
            - Columnas personalizables (To do, In progress, Done, etc.)
            - Automatización de movimiento de tarjetas
            - Integración con issues y PRs
            - Notas para tareas rápidas
            - Filtros y búsqueda
            - Asignación de responsables
            
            **Ejemplo de uso:**
            
            1. Crear un nuevo proyecto en la pestaña "Projects"
            2. Configurar columnas como "To do", "In progress", "Review", "Done"
            3. Añadir issues existentes o crear nuevas tarjetas
            4. Configurar automatización (ej. mover a "Done" cuando se cierra el issue)
            5. Arrastrar tarjetas entre columnas según avance el trabajo
            
            Es una excelente manera de visualizar el progreso del proyecto y gestionar prioridades.
            """)
            
            st.image("https://docs.github.com/assets/cb-77061/mw-1000/images/help/issues/project-board-basic-kanban-template.webp", caption="Project Board en GitHub")
        
        # Actions
        with st.expander("🤖 GitHub Actions: Automatización"):
            st.markdown("""
            **GitHub Actions** permite automatizar flujos de trabajo directamente en tu repositorio.
            
            **Casos de uso comunes:**
            
            - CI/CD: Construcción, pruebas y despliegue automáticos
            - Análisis de código y revisión de calidad
            - Publicación de paquetes
            - Notificaciones y alertas
            - Generación de documentación
            
            **Conceptos clave:**
            
            - **Workflow**: Proceso automatizado configurable
            - **Job**: Conjunto de pasos que se ejecutan en un runner
            - **Step**: Tarea individual que puede ejecutar comandos
            - **Action**: Unidad reutilizable de código
            - **Event**: Actividad que desencadena un workflow
            
            **Ejemplo de workflow básico:**
            """)
            
            st.code("""
            # .github/workflows/ci.yml
            name: CI
            
            on:
              push:
                branches: [ main ]
              pull_request:
                branches: [ main ]
            
            jobs:
              build:
                runs-on: ubuntu-latest
                
                steps:
                - uses: actions/checkout@v3
                
                - name: Set up Node.js
                  uses: actions/setup-node@v3
                  with:
                    node-version: 16
                    
                - name: Install dependencies
                  run: npm ci
                  
                - name: Run tests
                  run: npm test
                  
                - name: Build
                  run: npm run build
            """, language="yaml")
            
            st.markdown("""
            Los workflows se definen en archivos YAML en el directorio `.github/workflows/` de tu repositorio.
            """)
        
        # Simulador de Issue
        st.markdown("### Crear un Issue")
        
        issue_title = st.text_input("Título del Issue:", placeholder="Error en la validación del formulario de contacto")
        
        issue_type = st.selectbox(
            "Tipo de Issue:",
            ["🐛 Bug", "✨ Nueva funcionalidad", "📚 Documentación", "🔨 Mejora", "❓ Pregunta"]
        )
        
        issue_description = st.text_area(
            "Descripción:",
            placeholder="## Descripción\nDescribe el problema o sugerencia...\n\n## Pasos para reproducir\n1. Ir a...\n2. Hacer clic en...\n\n## Comportamiento esperado\nDebería...\n\n## Capturas de pantalla\n(Si aplica)",
            height=150
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            issue_priority = st.selectbox("Prioridad:", ["Alta", "Media", "Baja"])
            issue_assignee = st.text_input("Asignar a:", placeholder="username")
        
        with col2:
            issue_labels = st.multiselect(
                "Etiquetas:",
                ["bug", "enhancement", "documentation", "good first issue", "help wanted", "question", "invalid", "wontfix"]
            )
            issue_milestone = st.selectbox("Milestone:", ["v1.0", "v1.1", "v2.0", "Ninguno"])
        
        if st.button("Crear Issue (Simulación)"):
            if issue_title and issue_description:
                st.success(f"¡Issue '{issue_title}' creado exitosamente!")
                
                # Mostrar el issue creado
                labels_str = ", ".join([f"`{label}`" for label in issue_labels]) if issue_labels else "Ninguna"
                assignee_str = issue_assignee if issue_assignee else "Sin asignar"
                milestone_str = issue_milestone if issue_milestone != "Ninguno" else "Sin milestone"
                
                st.markdown(f"""
                ### Issue: {issue_title}
                
                **Tipo:** {issue_type}  
                **Prioridad:** {issue_priority}  
                **Asignado a:** {assignee_str}  
                **Etiquetas:** {labels_str}  
                **Milestone:** {milestone_str}
                
                ---
                
                {issue_description}
                
                ---
                
                **Estado:** Abierto  
                """)
            else:
                st.error("Por favor, completa al menos el título y la descripción.")
    
    with tab4:
        st.markdown("### Buenas Prácticas en GitHub")
        
        st.markdown("""
        Seguir buenas prácticas en GitHub mejora la colaboración, la calidad del código y la experiencia de todos los participantes.
        """)
        
        # Acordeón de buenas prácticas
        with st.expander("📝 Documentación Efectiva"):
            st.markdown("""
            Una buena documentación es crucial para cualquier proyecto colaborativo.
            
            #### README.md
            
            El README es lo primero que verán los visitantes de tu repositorio. Debe incluir:
            
            - **Título y descripción** clara del proyecto
            - **Badges** de estado (build, versión, licencia)
            - **Instalación** y configuración
            - **Uso** básico con ejemplos
            - **Contribución** (cómo pueden ayudar otros)
            - **Licencia**
            - **Créditos** y reconocimientos
            
            #### Otros archivos importantes
            
            - **CONTRIBUTING.md**: Guía detallada para contribuir
            - **CODE_OF_CONDUCT.md**: Normas de comportamiento
            - **SECURITY.md**: Cómo reportar vulnerabilidades
            - **CHANGELOG.md**: Historial de cambios
            - **LICENSE**: Términos legales de uso
            
            #### Wikis
            
            Para documentación más extensa, usa la Wiki de GitHub:
            
            - Guías de uso avanzado
            - Arquitectura del proyecto
            - Decisiones de diseño
            - FAQ
            """)
            
            st.code("""
            # Proyecto Awesome
            
            [![Build Status](https://img.shields.io/travis/usuario/proyecto.svg)](https://travis-ci.org/usuario/proyecto)
            [![Version](https://img.shields.io/npm/v/proyecto.svg)](https://www.npmjs.com/package/proyecto)
            [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
            
            Una descripción clara y concisa del proyecto y sus beneficios.
            
            ## Instalación
            
            ```bash
            npm install proyecto
            ```
            
            ## Uso
            
            ```javascript
            const proyecto = require('proyecto');
            
            proyecto.doAwesome();
            ```
            
            ## Características
            
            - Hace cosas increíbles
            - Resuelve problemas complejos
            - Fácil de usar
            
            ## Contribución
            
            Las contribuciones son bienvenidas! Por favor lee [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.
            
            ## Licencia
            
            Este proyecto está licenciado bajo la licencia MIT - ver [LICENSE](LICENSE) para más detalles.
            """, language="markdown")
        
        with st.expander("🌿 Estrategia de Ramificación"):
            st.markdown("""
            Una estrategia de ramificación clara facilita la colaboración y el mantenimiento.
            
            #### GitHub Flow
            
            Para proyectos con despliegue continuo:
            
            1. `main` siempre está listo para producción
            2. Crear ramas desde `main` para nuevos cambios
            3. Abrir PR temprano para discusión
            4. Merge a `main` tras revisión y CI
            5. Desplegar inmediatamente
            
            #### Git Flow
            
            Para proyectos con ciclos de release planificados:
            
            - `main`: código en producción
            - `develop`: próxima versión
            - `feature/*`: nuevas características
            - `release/*`: preparación para release
            - `hotfix/*`: correcciones urgentes
            
            #### Trunk-Based
            
            Para equipos experimentados con buena cobertura de pruebas:
            
            - Todos trabajan en `main` (trunk)
            - Ramas de muy corta duración
            - Feature toggles para funciones incompletas
            - CI riguroso
            
            #### Recomendaciones generales
            
            - Usar nombres descriptivos para las ramas
            - Mantener las ramas sincronizadas con `main`
            - Eliminar ramas después de fusionar
            - Proteger ramas importantes con reglas
            """)
        
        with st.expander("📊 Pull Requests Efectivos"):
            st.markdown("""
            Los pull requests son el centro de la colaboración en GitHub.
            
            #### Tamaño y enfoque
            
            - Mantén los PRs **pequeños y enfocados** en un solo objetivo
            - Ideal: <300 líneas de cambio
            - Un PR = Una funcionalidad, corrección o mejora
            
            #### Título y descripción
            
            - **Título claro** que resuma el propósito
            - Descripción detallada que incluya:
              - Qué cambios se han hecho
              - Por qué son necesarios
              - Cómo se implementaron
              - Cómo probar los cambios
              - Capturas o demos si aplica
            
            #### Revisión y discusión
            
            - Responde a todos los comentarios
            - Mantén una actitud constructiva
            - Actualiza el PR con nuevos commits
            - Usa "Resolve conversation" cuando esté resuelto
            
            #### Ejemplo de plantilla de PR
            """)
            
            st.code("""
            ## Descripción
            
            Breve descripción del cambio y su propósito.
            
            Fixes #123 (número de issue relacionado)
            
            ## Tipo de cambio
            
            - [ ] Corrección de bug
            - [ ] Nueva funcionalidad
            - [ ] Breaking change
            - [ ] Mejora de documentación
            
            ## Cómo se ha probado
            
            Describa las pruebas que realizó para verificar los cambios.
            
            ## Capturas de pantalla
            
            Si corresponde, agregue capturas de pantalla para ayudar a explicar su problema.
            
            ## Lista de verificación
            
            - [ ] El código sigue las pautas de estilo del proyecto
            - [ ] Se han añadido pruebas para los cambios
            - [ ] La documentación ha sido actualizada
            - [ ] Los cambios generan nuevas advertencias
            """, language="markdown")
        
        with st.expander("🔒 Seguridad y Permisos"):
            st.markdown("""
            La seguridad es una responsabilidad compartida en cualquier proyecto.
            
            #### Protección de ramas
            
            Configura reglas para ramas importantes:
            
            - Requerir revisión de PR antes de merge
            - Requerir verificación de status (CI/tests)
            - Requerir resolución de conversaciones
            - Prohibir push forzado
            - Restringir quién puede pushear
            
            Para configurar: Repositorio > Settings > Branches > Branch protection rules
            
            #### Secretos y datos sensibles
            
            - **Nunca** commits de secretos, API keys, contraseñas
            - Usa variables de entorno para desarrollo local
            - Usa GitHub Secrets para CI/CD
            - Utiliza `.gitignore` apropiadamente
            - Considera herramientas como git-crypt para casos especiales
            
            #### Dependencias y vulnerabilidades
            
            - Activa Dependabot alerts
            - Revisa regularmente las alertas de seguridad
            - Mantén las dependencias actualizadas
            - Considera escaneo de código SAST/DAST
            
            #### Permisos de repositorio
            
            - Usa permisos de "menor privilegio"
            - Crea equipos con roles específicos
            - Revisa colaboradores regularmente
            - Considera la verificación en dos pasos
            """)
        
        with st.expander("🤝 Etiqueta y Cultura"):
            st.markdown("""
            La forma en que interactuamos es tan importante como el código.
            
            #### Código de conducta
            
            Establece un código de conducta explícito:
            
            - Comportamiento esperado e inaceptable
            - Proceso de reporte y aplicación
            - Alcance (issues, PRs, eventos)
            
            GitHub tiene plantillas para ayudarte a crear uno.
            
            #### Comunicación respetuosa
            
            - Sé cortés y profesional
            - Enfócate en el código, no en la persona
            - Explica el "por qué", no solo el "qué"
            - Reconoce el buen trabajo
            - Asume buenas intenciones
            
            #### Mentoría y crecimiento
            
            - Etiqueta issues como "good first issue" para nuevos contribuidores
            - Proporciona feedback constructivo
            - Documenta procesos para reducir barreras de entrada
            - Celebra las primeras contribuciones
            
            #### Reconocimiento
            
            - Agradece a los contribuidores
            - Menciona a todos en release notes
            - Considera un archivo CONTRIBUTORS.md
            - Destaca contribuciones significativas
            """)
        
        # Checklist de buenas prácticas
        st.markdown("### Checklist de Buenas Prácticas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Documentación")
            
            docs_readme = st.checkbox("README.md completo y claro")
            docs_contributing = st.checkbox("Guía de contribución (CONTRIBUTING.md)")
            docs_code_of_conduct = st.checkbox("Código de conducta")
            docs_templates = st.checkbox("Plantillas de PR e Issues")
            docs_changelog = st.checkbox("Registro de cambios (CHANGELOG.md)")
            
            st.markdown("#### Estrategia de Ramas")
            
            branch_strategy = st.checkbox("Estrategia de ramificación definida")
            branch_protection = st.checkbox("Protección de ramas principales")
            branch_naming = st.checkbox("Convención de nombres para ramas")
        
        with col2:
            st.markdown("#### Revisión de Código")
            
            review_required = st.checkbox("Revisión obligatoria para PRs")
            review_codeowners = st.checkbox("Archivo CODEOWNERS configurado")
            review_style = st.checkbox("Linters y formatters automáticos")
            
            st.markdown("#### CI/CD y Automatización")
            
            ci_tests = st.checkbox("Tests automatizados en CI")
            ci_linting = st.checkbox("Verificación de estilo en CI")
            ci_deploy = st.checkbox("Despliegue automatizado")
        
        if st.button("Evaluar Prácticas"):
            # Contar checkboxes marcados
            docs_score = sum([docs_readme, docs_contributing, docs_code_of_conduct, docs_templates, docs_changelog])
            branch_score = sum([branch_strategy, branch_protection, branch_naming])
            review_score = sum([review_required, review_codeowners, review_style])
            ci_score = sum([ci_tests, ci_linting, ci_deploy])
            
            total_score = docs_score + branch_score + review_score + ci_score
            max_score = 14
            percentage = (total_score / max_score) * 100
            
            st.progress(percentage / 100)
            
            if percentage >= 80:
                st.success(f"¡Excelente! Tu proyecto sigue {total_score}/{max_score} buenas prácticas recomendadas.")
            elif percentage >= 50:
                st.warning(f"Bien, pero hay espacio para mejorar. Sigues {total_score}/{max_score} buenas prácticas recomendadas.")
            else:
                st.error(f"Necesitas mejorar significativamente. Solo sigues {total_score}/{max_score} buenas prácticas recomendadas.")
            
            # Sugerencias específicas
            st.markdown("### Recomendaciones para mejorar:")
            
            if docs_score < 3:
                st.markdown("- 📝 **Mejora tu documentación**: Un buen README y guías de contribución son esenciales.")
            
            if branch_score < 2:
                st.markdown("- 🌿 **Define mejor tu estrategia de ramas**: Protege tus ramas principales y establece convenciones claras.")
            
            if review_score < 2:
                st.markdown("- 🔍 **Fortalece tu proceso de revisión**: Haz obligatorias las revisiones y considera usar CODEOWNERS.")
            
            if ci_score < 2:
                st.markdown("- 🤖 **Automatiza más**: Implementa tests, linting y despliegue automatizados con GitHub Actions.")
    
    with tab5:
        st.markdown("<h3 class='subheader'>Quiz: Flujo de Trabajo en GitHub</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        Comprueba tu conocimiento sobre el flujo de trabajo en GitHub:
        """)
        
        # Pregunta 1
        q1 = st.radio(
            "1. ¿Qué es un 'fork' en GitHub?",
            [
                "Una rama dentro del repositorio original", 
                "Una copia del repositorio original en tu cuenta personal",
                "Un error en el código",
                "Una función para dividir archivos grandes"
            ]
        )
        
        # Pregunta 2
        q2 = st.radio(
            "2. ¿Cuál es el propósito principal de un Pull Request?",
            [
                "Descargar código del repositorio remoto", 
                "Proponer cambios y solicitar que sean revisados e integrados",
                "Crear una nueva rama",
                "Forzar la actualización del repositorio local"
            ]
        )
        
        # Pregunta 3
        q3 = st.radio(
            "3. En GitHub, ¿qué son los 'Issues'?",
            [
                "Errores que impiden que el código compile",
                "Conflictos de merge que deben resolverse",
                "Un sistema para rastrear tareas, mejoras y bugs del proyecto",
                "Mensajes de error generados por GitHub Actions"
            ]
        )
        
        # Pregunta 4
        q4 = st.radio(
            "4. ¿Qué significa 'upstream' en el contexto de GitHub?",
            [
                "El repositorio original del que hiciste fork", 
                "La rama principal (main o master)",
                "Una rama que está por delante de la tuya",
                "El último commit en el historial"
            ]
        )
        
        # Pregunta 5
        q5 = st.radio(
            "5. ¿Cuál de estas NO es una característica de GitHub Actions?",
            [
                "Automatización de flujos de trabajo", 
                "Integración continua (CI)",
                "Gestión de dependencias",
                "Edición colaborativa en tiempo real del mismo archivo"
            ]
        )
        
        # Botón para verificar respuestas
        if st.button("Verificar Respuestas"):
            score = 0
            
            if q1 == "Una copia del repositorio original en tu cuenta personal":
                score += 1
            
            if q2 == "Proponer cambios y solicitar que sean revisados e integrados":
                score += 1
                
            if q3 == "Un sistema para rastrear tareas, mejoras y bugs del proyecto":
                score += 1
                
            if q4 == "El repositorio original del que hiciste fork":
                score += 1
                
            if q5 == "Edición colaborativa en tiempo real del mismo archivo":
                score += 1
            
            st.success(f"¡Obtuviste {score} de 5 respuestas correctas!")
            
            if score == 5:
                st.balloons()
                st.markdown("### 🏆 ¡Perfecto! Dominas el flujo de trabajo en GitHub.")
            elif score >= 3:
                st.markdown("### 👍 ¡Buen trabajo! Tienes un buen entendimiento de GitHub.")
            else:
                st.markdown("### 📚 Revisa nuevamente el material para reforzar tus conocimientos sobre GitHub.")
