import streamlit as st

def mostrar_contenido():
    st.markdown("<h2 class='module-header'>Repositorios Remotos</h2>", unsafe_allow_html=True)
    
    # Tabs para organizar el contenido
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Conceptos Básicos", "GitHub y Alternativas", "Comandos Esenciales", "Buenas Prácticas", "Quiz"])
    
    with tab1:
        st.markdown("### Repositorios Remotos: Fundamentos")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            Un **repositorio remoto** es una versión de tu proyecto alojada en Internet o en una red.
            Permite la colaboración entre múltiples personas y sirve como copia de seguridad centralizada.
            
            <div class='highlight'>
            Trabajar con repositorios remotos te permite <b>compartir</b> tu trabajo y <b>obtener</b> cambios de otros colaboradores.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            #### Ventajas de los repositorios remotos:
            
            - 🔄 **Colaboración**: Múltiples personas pueden trabajar en el mismo proyecto
            - 💾 **Respaldo**: Copia de seguridad en la nube del código fuente
            - 📊 **Seguimiento**: Control de cambios y contribuciones de cada miembro
            - 🌐 **Accesibilidad**: Acceso al código desde cualquier lugar
            - 🛠️ **Herramientas**: Integración con CI/CD, revisión de código, etc.
            """)
            
            st.markdown("""
            #### Terminología clave:
            
            - **Origin**: Nombre convencional para el repositorio remoto principal
            - **Upstream**: Repositorio original del que se hizo fork
            - **Push**: Enviar cambios locales al repositorio remoto
            - **Pull/Fetch**: Obtener cambios del repositorio remoto
            - **Clone**: Crear una copia local de un repositorio remoto
            """)
        
        with col2:
            # Imagen de repositorio remoto
            st.image("https://git-scm.com/book/en/v2/images/remote-branches-1.png", caption="Repositorios locales y remotos")
            
            st.markdown("""
            <div class='tip'>
            <b>Local vs. Remoto</b>
            
            En Git, el repositorio local contiene toda la historia y ramas.
            El remoto es como un "espejo" con el que sincronizas mediante push y pull.
            
            Git es un sistema distribuido, lo que significa que cada desarrollador tiene una copia completa del repositorio.
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Plataformas de Alojamiento Git")
        
        st.markdown("""
        Existen varias plataformas que permiten alojar repositorios Git en la nube. Cada una tiene características particulares:
        """)
        
        # Acordeón para las diferentes plataformas
        with st.expander("🐙 GitHub"):
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.markdown("""
                **GitHub** es la plataforma más popular para alojar código. Propiedad de Microsoft desde 2018.
                
                **Características destacadas:**
                
                - Issues y Pull Requests para gestionar cambios
                - GitHub Actions para CI/CD
                - GitHub Pages para hosting web
                - Codespaces para desarrollo en la nube
                - Copilot para asistencia de código con IA
                - Proyectos para gestión de tareas
                - Amplia comunidad open source
                
                **Ideal para:** Todo tipo de proyectos, especialmente open source.
                
                [github.com](https://github.com)
                """)
            
            with col2:
                st.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=150)
        
        with st.expander("🦊 GitLab"):
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.markdown("""
                **GitLab** es una plataforma completa de DevOps con Git en su núcleo.
                
                **Características destacadas:**
                
                - CI/CD integrado muy potente
                - Gestión completa del ciclo de vida DevOps
                - Registry de contenedores integrado
                - Opciones de despliegue autoalojado o en la nube
                - Herramientas de seguridad y escaneo de código
                - Wiki y documentación integradas
                
                **Ideal para:** Empresas que buscan una solución DevOps completa.
                
                [gitlab.com](https://gitlab.com)
                """)
            
            with col2:
                st.image("https://about.gitlab.com/images/press/logo/png/gitlab-icon-rgb.png", width=150)
        
        with st.expander("🪣 Bitbucket"):
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.markdown("""
                **Bitbucket** es parte del ecosistema de Atlassian, con integración nativa con Jira y Confluence.
                
                **Características destacadas:**
                
                - Integración perfecta con Jira y otras herramientas de Atlassian
                - Pipelines para CI/CD
                - Repositorios privados gratuitos
                - Permisos granulares
                - Revisión de código incorporada
                
                **Ideal para:** Equipos que ya utilizan productos Atlassian.
                
                [bitbucket.org](https://bitbucket.org)
                """)
            
            with col2:
                st.image("https://wac-cdn.atlassian.com/dam/jcr:e75ffb0e-b3ee-40ca-8659-ecb93675a826/Bitbucket@2x-blue.png", width=150)
        
        with st.expander("💻 Gitea/Gogs"):
            st.markdown("""
            **Gitea** y **Gogs** son alternativas ligeras y autoalojadas.
            
            **Características destacadas:**
            
            - Bajo consumo de recursos
            - Fácil instalación (incluso en Raspberry Pi)
            - Interfaz similar a GitHub
            - Completamente autoalojado
            - Open source
            
            **Ideal para:** Pequeños equipos o uso personal con recursos limitados.
            
            [gitea.io](https://gitea.io) | [gogs.io](https://gogs.io)
            """)
        
        # Comparativa de plataformas
        st.markdown("### Comparativa de Plataformas Git")
        
        data = {
            "Plataforma": ["GitHub", "GitLab", "Bitbucket", "Gitea/Gogs"],
            "Fortalezas": ["Comunidad, Herramientas", "DevOps integrado, CI/CD", "Integración Atlassian", "Ligereza, Autoalojamiento"],
            "Modelo": ["Freemium", "Freemium/Enterprise", "Freemium", "100% Gratuito (Self-hosted)"],
            "Ideal para": ["Open Source, Todo tipo", "DevOps Enterprise", "Usuarios de Jira", "Autoalojamiento ligero"]
        }
        
        # Crear una tabla de comparación
        for i in range(len(data["Plataforma"])):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"**{data['Plataforma'][i]}**")
            with col2:
                st.markdown(f"Fortalezas: {data['Fortalezas'][i]}")
                st.markdown(f"Modelo: {data['Modelo'][i]}")
            with col3:
                st.markdown(f"Ideal para: {data['Ideal para'][i]}")
            st.markdown("---")
    
    with tab3:
        st.markdown("### Comandos Esenciales para Repositorios Remotos")
        
        # Acordeón para diferentes operaciones
        with st.expander("🔍 Clonar un Repositorio"):
            st.markdown("""
            **Clonar** significa crear una copia local completa de un repositorio remoto.
            """)
            
            st.code("""
            # Sintaxis básica
            git clone <url>
            
            # Ejemplos:
            git clone https://github.com/usuario/repo.git
            git clone git@github.com:usuario/repo.git  # Usando SSH
            
            # Clonar una rama específica
            git clone -b rama-especifica https://github.com/usuario/repo.git
            
            # Clonar a un directorio específico
            git clone https://github.com/usuario/repo.git mi-directorio
            """)
            
            st.markdown("""
            <div class='tip'>
            <b>HTTPS vs SSH:</b> HTTPS es más sencillo para empezar, pero SSH es más seguro y no requiere introducir contraseña cada vez.
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("🔗 Gestionar Repositorios Remotos"):
            st.markdown("""
            Puedes configurar múltiples repositorios remotos para un proyecto.
            """)
            
            st.code("""
            # Ver repositorios remotos configurados
            git remote -v
            
            # Añadir un nuevo repositorio remoto
            git remote add <nombre> <url>
            git remote add origin https://github.com/usuario/repo.git
            
            # Cambiar la URL de un remoto existente
            git remote set-url origin https://github.com/usuario/nuevo-repo.git
            
            # Eliminar un remoto
            git remote remove <nombre>
            
            # Renombrar un remoto
            git remote rename <antiguo> <nuevo>
            """)
        
        with st.expander("⬆️ Push: Enviar Cambios al Remoto"):
            st.markdown("""
            **Push** es el comando para enviar tus commits locales al repositorio remoto.
            """)
            
            st.code("""
            # Sintaxis básica
            git push <remoto> <rama>
            
            # Ejemplo común
            git push origin main
            
            # Configurar tracking y hacer push
            git push -u origin feature-branch  # -u configura el tracking
            
            # Push forzado (¡usar con precaución!)
            git push --force origin main  # ¡Peligroso! Sobrescribe la historia
            
            # Alternativa más segura al push forzado
            git push --force-with-lease origin main
            
            # Enviar todas las ramas locales
            git push --all origin
            
            # Enviar etiquetas
            git push --tags origin
            """)
            
            st.markdown("""
            <div class='warning'>
            <b>¡Precaución con --force!</b>
            
            El push forzado sobrescribe la historia remota y puede causar problemas para otros colaboradores.
            Úsalo solo cuando sea absolutamente necesario y estés seguro de las consecuencias.
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("⬇️ Fetch y Pull: Obtener Cambios del Remoto"):
            st.markdown("""
            **Fetch** descarga cambios del remoto sin integrarlos, mientras que **Pull** combina fetch y merge en un solo paso.
            """)
            
            st.code("""
            # Obtener cambios sin integrarlos (fetch)
            git fetch <remoto>
            git fetch origin
            
            # Obtener e integrar cambios (pull)
            git pull <remoto> <rama>
            git pull origin main
            
            # Pull con rebase en lugar de merge
            git pull --rebase origin main
            
            # Fetch de todas las ramas remotas
            git fetch --all
            """)
            
            st.markdown("""
            <div class='tip'>
            <b>Fetch vs Pull:</b>
            
            - <code>fetch</code> es más seguro porque solo descarga sin cambiar tu código
            - <code>pull</code> es más rápido pero puede crear commits de merge automáticos
            - El flujo <code>fetch</code> + revisar + <code>merge</code> da más control
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("🔄 Tracking de Ramas Remotas"):
            st.markdown("""
            Las ramas de seguimiento (tracking branches) conectan tus ramas locales con las remotas.
            """)
            
            st.code("""
            # Crear una rama local que sigue una remota
            git checkout -b feature origin/feature
            
            # Forma moderna (Git 2.23+)
            git switch -c feature origin/feature
            
            # Configurar una rama existente para seguir una remota
            git branch -u origin/feature feature
            
            # O si estás en la rama:
            git branch -u origin/feature
            
            # Ver qué ramas locales siguen a qué ramas remotas
            git branch -vv
            """)
        
        # Simulador de operaciones remotas
        st.markdown("### Simulador de Operaciones Remotas")
        
        operacion = st.selectbox(
            "Selecciona una operación remota:",
            [
                "Configurar un nuevo repositorio remoto para un proyecto existente",
                "Clonar un repositorio y trabajar en él",
                "Enviar cambios locales al repositorio remoto",
                "Actualizar tu repositorio local con cambios remotos"
            ]
        )
        
        if operacion == "Configurar un nuevo repositorio remoto para un proyecto existente":
            st.markdown("""
            Sigue estos pasos para conectar un proyecto local existente con un repositorio remoto nuevo:
            """)
            
            remoto_url = st.text_input("URL del repositorio remoto:", placeholder="https://github.com/usuario/repo.git o git@github.com:usuario/repo.git")
            
            if remoto_url:
                st.code(f"""
                # Asegúrate de tener un repositorio Git inicializado localmente
                # Si no lo tienes, ejecuta:
                # git init
                
                # Añadir el repositorio remoto
                git remote add origin {remoto_url}
                
                # Verificar que se agregó correctamente
                git remote -v
                
                # Hacer push de tu código al remoto (asumiendo que tienes commits)
                git push -u origin main
                
                # Si tu rama principal se llama 'master' en lugar de 'main':
                # git push -u origin master
                """)
                
                st.success("Ahora tu repositorio local está conectado al remoto y puedes sincronizar cambios.")
        
        elif operacion == "Clonar un repositorio y trabajar en él":
            st.markdown("""
            Para comenzar a trabajar con un repositorio existente:
            """)
            
            repo_url = st.text_input("URL del repositorio a clonar:", placeholder="https://github.com/usuario/repo.git")
            
            if repo_url:
                st.code(f"""
                # Clonar el repositorio
                git clone {repo_url}
                
                # Entrar al directorio del proyecto
                cd $(basename {repo_url} .git)
                
                # Ver las ramas disponibles
                git branch -a
                
                # Crear y cambiar a una nueva rama para tus cambios
                git checkout -b mi-nueva-caracteristica
                
                # [Realiza cambios en los archivos]
                
                # Añadir y confirmar cambios
                git add .
                git commit -m "Añadir nueva característica"
                
                # Enviar tu rama al repositorio remoto
                git push -u origin mi-nueva-caracteristica
                """)
                
                st.success("Ahora puedes seguir trabajando en tu rama y colaborar con otros.")
        
        elif operacion == "Enviar cambios locales al repositorio remoto":
            st.markdown("""
            Para enviar tus cambios locales al repositorio remoto:
            """)
            
            rama = st.text_input("Nombre de la rama:", value="main")
            
            st.code(f"""
            # Asegúrate de que todos tus cambios están confirmados
            git status
            
            # Si hay cambios sin confirmar:
            # git add .
            # git commit -m "Descripción de los cambios"
            
            # Opcional: Actualizar tu rama con los cambios remotos primero
            git pull origin {rama}
            
            # Enviar tus cambios al remoto
            git push origin {rama}
            """)
            
            st.markdown("""
            <div class='tip'>
            Si es la primera vez que envías esta rama, usa <code>git push -u origin {rama}</code> para configurar el tracking.
            </div>
            """, unsafe_allow_html=True)
        
        elif operacion == "Actualizar tu repositorio local con cambios remotos":
            st.markdown("""
            Para obtener los últimos cambios del repositorio remoto:
            """)
            
            metodo = st.radio(
                "Método preferido:",
                ["Pull (más rápido, menos control)", "Fetch + Merge (más control)"]
            )
            
            if metodo == "Pull (más rápido, menos control)":
                st.code("""
                # Asegúrate de estar en la rama correcta
                git checkout main
                
                # Obtener e integrar cambios en un solo paso
                git pull origin main
                
                # Opcional: usar rebase en lugar de merge
                # git pull --rebase origin main
                """)
            else:
                st.code("""
                # Asegúrate de estar en la rama correcta
                git checkout main
                
                # 1. Obtener los cambios sin integrarlos
                git fetch origin
                
                # 2. Ver qué cambios hay (opcional)
                git log HEAD..origin/main
                
                # 3. Integrar los cambios
                git merge origin/main
                
                # Alternativa: Usar rebase en lugar de merge
                # git rebase origin/main
                """)
                
                st.markdown("""
                <div class='tip'>
                El enfoque fetch + merge te da la oportunidad de revisar los cambios antes de integrarlos.
                </div>
                """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### Buenas Prácticas para Trabajo Remoto")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            #### Sincronización efectiva
            
            1. **Pull frecuente**: Actualiza tu código local regularmente para evitar conflictos grandes
            
            2. **Commit pequeños y frecuentes**: Es más fácil gestionar y revisar cambios pequeños
            
            3. **Push regularmente**: Evita acumular muchos commits locales sin respaldo
            
            4. **Ramas cortas**: Mantén las ramas de características lo más cortas posible en duración
            
            5. **Pull con rebase**: `git pull --rebase` para mantener un historial más limpio
            
            ```bash
            # Configurar rebase por defecto para pull
            git config --global pull.rebase true
            ```
            """)
            
            st.markdown("""
            #### Gestión de ramas remotas
            
            1. **Nomenclatura clara**: Usa prefijos como `feature/`, `bugfix/`, `hotfix/`
            
            2. **Limpieza regular**: Elimina ramas antiguas que ya se han fusionado
            
            ```bash
            # Eliminar ramas locales que ya no existen en el remoto
            git fetch --prune
            
            # Eliminar una rama remota
            git push origin --delete nombre-rama
            ```
            
            3. **Protege ramas principales**: Configura protección para `main`/`master` en GitHub/GitLab
            """)
        
        with col2:
            st.markdown("""
            <div class='tip'>
            <b>Consejo Pro</b>
            
            Configura tu editor de Git para facilitar la resolución de conflictos:
            
            ```bash
            git config --global merge.tool vscode
            git config --global mergetool.vscode.cmd 'code --wait $MERGED'
            ```
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='warning'>
            <b>Prácticas a evitar</b>
            
            - Push forzado en ramas compartidas
            - Commits con mensajes vagos
            - Mezclar múltiples características en un solo commit
            - Hacer commit de archivos temporales o generados
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### Autenticación y Seguridad")
        
        with st.expander("🔐 Configuración de SSH"):
            st.markdown("""
            SSH es el método recomendado para conectarse a repositorios remotos de forma segura sin necesidad de introducir contraseñas constantemente.
            """)
            
            st.code("""
            # Generar un nuevo par de claves SSH
            ssh-keygen -t ed25519 -C "tu.email@ejemplo.com"
            
            # Iniciar el agente SSH
            eval "$(ssh-agent -s)"
            
            # Añadir tu clave privada al agente
            ssh-add ~/.ssh/id_ed25519
            
            # Ver tu clave pública (para añadir a GitHub/GitLab)
            cat ~/.ssh/id_ed25519.pub
            """)
            
            st.markdown("""
            Luego, copia el contenido de tu clave pública y:
            
            **GitHub**: Perfil > Settings > SSH and GPG keys > New SSH key
            
            **GitLab**: Preferences > SSH Keys
            """)
        
        with st.expander("🔑 Credenciales HTTPS y Tokens"):
            st.markdown("""
            Si prefieres usar HTTPS, puedes usar credencial helpers o tokens de acceso personal.
            """)
            
            st.code("""
            # Configurar el credential helper (Windows)
            git config --global credential.helper wincred
            
            # Configurar el credential helper (macOS)
            git config --global credential.helper osxkeychain
            
            # Configurar el credential helper (Linux)
            git config --global credential.helper cache
            git config --global credential.helper 'cache --timeout=3600'
            """)
            
            st.markdown("""
            **Tokens de acceso personal**:
            
            Para GitHub/GitLab moderno, es recomendable usar tokens en lugar de contraseñas:
            
            1. GitHub: Settings > Developer settings > Personal access tokens
            2. Genera un token con los permisos necesarios
            3. Usa el token como contraseña cuando Git lo solicite
            """)
        
        with st.expander("📝 Archivos .gitignore"):
            st.markdown("""
            Los archivos `.gitignore` son cruciales para evitar commit accidental de archivos sensibles o innecesarios.
            """)
            
            st.code("""
            # Ejemplo de .gitignore para un proyecto Node.js
            
            # Dependencias
            node_modules/
            
            # Archivos de construcción
            /dist
            /build
            
            # Archivos de entorno
            .env
            .env.local
            
            # Logs
            logs
            *.log
            
            # Archivos del sistema operativo
            .DS_Store
            Thumbs.db
            
            # Archivos de configuración del IDE
            .idea/
            .vscode/
            *.sublime-project
            """)
            
            st.markdown("""
            Puedes encontrar plantillas de `.gitignore` para diferentes lenguajes y frameworks en:
            
            [github.com/github/gitignore](https://github.com/github/gitignore)
            """)
        
        # Widget interactivo para crear .gitignore
        st.markdown("### Generador de .gitignore")
        
        tecnologias = st.multiselect(
            "Selecciona tecnologías para tu .gitignore:",
            ["Node.js", "Python", "Java", "C++", "macOS", "Windows", "Linux", "Visual Studio Code", "JetBrains IDEs", "React", "Angular", "Vue.js"]
        )
        
        if tecnologias:
            gitignore_content = "# Archivo .gitignore generado\n\n"
            
            if "Node.js" in tecnologias:
                gitignore_content += """# Node.js
node_modules/
npm-debug.log
yarn-error.log
yarn-debug.log
.pnpm-debug.log
package-lock.json
yarn.lock
.npm/

"""
            
            if "Python" in tecnologias:
                gitignore_content += """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg
venv/
ENV/
.venv/
.pytest_cache/

"""
            
            if "Java" in tecnologias:
                gitignore_content += """# Java
*.class
*.log
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar
hs_err_pid*
.classpath
.project
.settings/
target/
.idea/
*.iml
*.iws
*.ipr
.gradle/
build/

"""
            
            if "C++" in tecnologias:
                gitignore_content += """# C++
*.d
*.slo
*.lo
*.o
*.obj
*.gch
*.pch
*.so
*.dylib
*.dll
*.lai
*.la
*.a
*.lib
*.exe
*.out
*.app

"""
            
            if "macOS" in tecnologias:
                gitignore_content += """# macOS
.DS_Store
.AppleDouble
.LSOverride
Icon
._*
.Spotlight-V100
.Trashes

"""
            
            if "Windows" in tecnologias:
                gitignore_content += """# Windows
Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/
*.cab
*.msi
*.msm
*.msp
*.lnk

"""
            
            if "Linux" in tecnologias:
                gitignore_content += """# Linux
*~
.fuse_hidden*
.directory
.Trash-*
.nfs*

"""
            
            if "Visual Studio Code" in tecnologias:
                gitignore_content += """# Visual Studio Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
*.code-workspace
.history/

"""
            
            if "JetBrains IDEs" in tecnologias:
                gitignore_content += """# JetBrains IDEs
.idea/
*.iml
*.iws
*.ipr
*.iws
out/
.idea_modules/

"""
            
            if "React" in tecnologias:
                gitignore_content += """# React
.DS_*
*.log
logs
**/*.backup.*
**/*.back.*
node_modules/
bower_components/
*.sublime*
psd
thumb
sketch
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
build/

"""
            
            if "Angular" in tecnologias:
                gitignore_content += """# Angular
/dist/
/bazel-out
/integration/bazel/bazel-*
e2e_test.*
node_modules/
tools/gulp-tasks/cldr/cldr-data/
# Include when developing application packages.
pubspec.lock
.c9
.idea/
.devcontainer/*
!.devcontainer/README.md
!.devcontainer/recommended-devcontainer.json
!.devcontainer/recommended-Dockerfile
.settings/
.vscode/launch.json
.vscode/settings.json
.vscode/tasks.json
*.swo
*.swp
modules/.settings
modules/.vscode
.vimrc
.nvimrc

"""
            
            if "Vue.js" in tecnologias:
                gitignore_content += """# Vue.js
.DS_Store
node_modules
/dist
/tests/e2e/videos/
/tests/e2e/screenshots/
# local env files
.env.local
.env.*.local
# Log files
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
# Editor directories and files
.idea
.vscode
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

"""
            
            st.code(gitignore_content)
            
            st.markdown("""
            <div class='tip'>
            Para usar este .gitignore, crea un archivo llamado <code>.gitignore</code> en la raíz de tu repositorio y copia el contenido anterior.
            </div>
            """, unsafe_allow_html=True)
    
    with tab5:
        st.markdown("<h3 class='subheader'>Quiz: Repositorios Remotos</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        Comprueba tu conocimiento sobre repositorios remotos:
        """)
        
        # Pregunta 1
        q1 = st.radio(
            "1. ¿Cuál es el comando para clonar un repositorio remoto?",
            ["git remote clone", "git pull", "git clone", "git fetch"]
        )
        
        # Pregunta 2
        q2 = st.radio(
            "2. ¿Qué comando usarías para enviar tus cambios locales al repositorio remoto?",
            [
                "git commit", 
                "git push",
                "git upload",
                "git send"
            ]
        )
        
        # Pregunta 3
        q3 = st.radio(
            "3. ¿Cuál es la diferencia principal entre 'git fetch' y 'git pull'?",
            [
                "No hay diferencia, son sinónimos",
                "git fetch sólo funciona con GitHub, git pull con cualquier remoto",
                "git fetch descarga cambios sin integrarlos, git pull descarga e integra en un solo paso",
                "git fetch es más rápido pero menos seguro que git pull"
            ]
        )
        
        # Pregunta 4
        q4 = st.radio(
            "4. ¿Qué comando te muestra los repositorios remotos configurados?",
            [
                "git show remotes", 
                "git list remotes",
                "git remote -v",
                "git remotes list"
            ]
        )
        
        # Pregunta 5
        q5 = st.radio(
            "5. Para añadir un nuevo repositorio remoto llamado 'upstream', ¿qué comando usarías?",
            [
                "git add upstream https://github.com/original/repo.git",
                "git remote add upstream https://github.com/original/repo.git",
                "git upstream add https://github.com/original/repo.git",
                "git remote new upstream https://github.com/original/repo.git"
            ]
        )
        
        # Botón para verificar respuestas
        if st.button("Verificar Respuestas"):
            score = 0
            
            if q1 == "git clone":
                score += 1
            
            if q2 == "git push":
                score += 1
                
            if q3 == "git fetch descarga cambios sin integrarlos, git pull descarga e integra en un solo paso":
                score += 1
                
            if q4 == "git remote -v":
                score += 1
                
            if q5 == "git remote add upstream https://github.com/original/repo.git":
                score += 1
            
            st.success(f"¡Obtuviste {score} de 5 respuestas correctas!")
            
            if score == 5:
                st.balloons()
                st.markdown("### 🏆 ¡Perfecto! Dominas los conceptos de repositorios remotos.")
            elif score >= 3:
                st.markdown("### 👍 ¡Buen trabajo! Tienes un buen entendimiento del trabajo con remotos.")
            else:
                st.markdown("### 📚 Revisa nuevamente el material para reforzar tus conocimientos sobre repositorios remotos.")
