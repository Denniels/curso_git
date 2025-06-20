import streamlit as st

def mostrar_contenido():
    st.markdown("<h2 class='module-header'>Ramas y Fusiones</h2>", unsafe_allow_html=True)
    
    # Tabs para organizar el contenido
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Conceptos de Ramas", "Creación y Navegación", "Fusiones", "Estrategias de Ramificación", "Quiz"])
    
    with tab1:
        st.markdown("### Conceptos Fundamentales de Ramas")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            Las **ramas (branches)** son una de las características más poderosas de Git. Permiten:
            
            - Desarrollar funcionalidades de forma aislada
            - Trabajar en paralelo en diferentes características
            - Experimentar sin afectar al código principal
            - Gestionar versiones y lanzamientos
            
            <div class='highlight'>
            En Git, una rama es simplemente un puntero móvil a un commit. La rama predeterminada se llama tradicionalmente <code>master</code>, aunque actualmente muchos proyectos usan <code>main</code>.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            #### ¿Cómo funcionan las ramas?
            
            Cuando creas una rama nueva:
            
            1. Git crea un nuevo puntero que apunta al mismo commit donde estás actualmente
            2. Al hacer nuevos commits en esa rama, el puntero avanza automáticamente
            3. La rama `HEAD` marca la rama activa en la que estás trabajando
            """)
        
        with col2:
            # Imagen conceptual de ramas
            st.image("https://git-scm.com/book/en/v2/images/branch-and-history.png", caption="Ramas en Git")
            
            st.markdown("""
            <div class='tip'>
            <b>¿Por qué usar ramas?</b>
            
            Las ramas permiten mantener un flujo de trabajo organizado, especialmente en equipos. Cada característica, corrección de errores o experimento puede tener su propia rama.
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Creación y Navegación entre Ramas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Comandos Básicos")
            
            st.code("""
            # Ver todas las ramas
            git branch
            
            # Crear una nueva rama
            git branch nueva-caracteristica
            
            # Cambiar a una rama existente
            git checkout nueva-caracteristica
            
            # Crear y cambiar a una nueva rama (atajo)
            git checkout -b otra-caracteristica
            
            # En Git moderno (2.23+)
            git switch nueva-caracteristica      # Cambiar
            git switch -c otra-caracteristica    # Crear y cambiar
            """)
        
        with col2:
            st.markdown("#### Buenas Prácticas")
            
            st.markdown("""
            - Usa nombres descriptivos para las ramas
              - `feature/login-system`
              - `bugfix/header-alignment`
              - `docs/api-reference`
            
            - Mantén las ramas enfocadas en un solo propósito
            
            - Elimina ramas después de fusionarlas
              ```
              git branch -d rama-fusionada
              ```
            
            - Actualiza tus ramas con la rama principal regularmente
              ```
              git checkout feature-branch
              git rebase main
              ```
            """)
        
        # Simulador de creación de ramas
        st.markdown("### Simulador de Trabajo con Ramas")
        
        tipo_rama = st.selectbox(
            "Tipo de rama a crear:",
            ["feature (nueva característica)", "bugfix (corrección de error)", "hotfix (corrección urgente)", "release (preparación de versión)", "docs (documentación)"]
        )
        
        nombre_funcionalidad = st.text_input("Nombre descriptivo:", placeholder="login-system, navbar-responsive, etc.")
        
        if tipo_rama and nombre_funcionalidad:
            prefijo = tipo_rama.split()[0]
            nombre_rama = f"{prefijo}/{nombre_funcionalidad}"
            
            st.markdown(f"#### Trabajando con la rama: `{nombre_rama}`")
            
            st.code(f"""
            # Asegúrate de estar en la rama principal actualizada
            git checkout main
            git pull
            
            # Crear y cambiar a la nueva rama
            git checkout -b {nombre_rama}
            
            # Ahora puedes trabajar en tu característica...
            # (haz cambios en los archivos)
            
            # Añadir y confirmar tus cambios
            git add .
            git commit -m "Añadir {nombre_funcionalidad}"
            
            # Cuando termines, puedes publicar tu rama (opcional)
            git push -u origin {nombre_rama}
            """)
            
            st.success(f"¡Rama `{nombre_rama}` lista para desarrollo!")
    
    with tab3:
        st.markdown("### Fusiones (Merging)")
        
        st.markdown("""
        La **fusión** es el proceso de integrar los cambios de una rama en otra. Es una operación fundamental
        cuando trabajas con ramas en Git.
        """)
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("#### Tipos de Fusiones")
            
            st.markdown("""
            Git realiza principalmente dos tipos de fusiones:
            
            1. **Fast-forward (avance rápido)**: Cuando no hay commits adicionales en la rama de destino desde que se creó la rama a fusionar.
            
            2. **Recursive/Three-way (tres vías)**: Cuando ambas ramas han evolucionado de forma independiente y Git necesita crear un nuevo commit de fusión.
            """)
            
            st.markdown("#### Realizar una Fusión")
            
            st.code("""
            # 1. Cambiar a la rama de destino (donde quieres incorporar los cambios)
            git checkout main
            
            # 2. Fusionar la otra rama en la actual
            git merge feature-branch
            
            # 3. (Opcional) Resolver conflictos si los hay
            
            # 4. (Opcional) Eliminar la rama fusionada si ya no es necesaria
            git branch -d feature-branch
            """)
        
        with col2:
            # Imagen sobre fusiones
            st.image("https://git-scm.com/book/en/v2/images/basic-merging-1.png", caption="Fusión de ramas")
            
            st.markdown("""
            <div class='warning'>
            <b>Conflictos de fusión</b>
            
            Los conflictos ocurren cuando se modifican las mismas líneas de un archivo en ambas ramas.
            Git no puede decidir automáticamente qué cambios conservar y requerirá intervención manual.
            </div>
            """, unsafe_allow_html=True)
        
        # Simulador de fusión
        st.markdown("### Escenarios de Fusión")
        
        escenario_fusion = st.radio(
            "Selecciona un escenario de fusión:",
            ["Fusión simple (fast-forward)", "Fusión con commit de merge", "Fusión con conflictos"]
        )
        
        if escenario_fusion == "Fusión simple (fast-forward)":
            st.markdown("""
            En este escenario, la rama principal no ha cambiado desde que creaste tu rama de características:
            """)
            
            st.image("https://git-scm.com/book/en/v2/images/basic-branching-4.png", caption="Antes de la fusión fast-forward")
            
            st.code("""
            # Asegúrate de tener todos los cambios confirmados en tu rama
            git status
            
            # Cambiar a la rama principal
            git checkout main
            
            # Realizar la fusión
            git merge feature-branch
            
            # El resultado será algo como:
            # "Fast-forward"
            # (resumen de archivos cambiados)
            
            # Opcional: eliminar la rama de características
            git branch -d feature-branch
            """)
            
            st.image("https://git-scm.com/book/en/v2/images/basic-branching-5.png", caption="Después de la fusión fast-forward")
            
        elif escenario_fusion == "Fusión con commit de merge":
            st.markdown("""
            En este escenario, tanto la rama principal como tu rama de características han evolucionado:
            """)
            
            st.image("https://git-scm.com/book/en/v2/images/basic-merging-1.png", caption="Antes de la fusión recursiva")
            
            st.code("""
            # Cambiar a la rama principal
            git checkout main
            
            # Realizar la fusión
            git merge feature-branch
            
            # Git abrirá el editor para escribir un mensaje de commit de fusión
            # Puedes aceptar el mensaje predeterminado o personalizarlo
            
            # El resultado será algo como:
            # "Merge branch 'feature-branch'"
            # (resumen de archivos cambiados)
            """)
            
            st.image("https://git-scm.com/book/en/v2/images/basic-merging-2.png", caption="Después de la fusión recursiva")
            
        elif escenario_fusion == "Fusión con conflictos":
            st.markdown("""
            En este escenario, hay cambios en las mismas líneas de los mismos archivos en ambas ramas:
            """)
            
            st.code("""
            # Intentar la fusión
            git checkout main
            git merge feature-branch
            
            # Git mostrará algo como:
            # "CONFLICT (content): Merge conflict in archivo.txt"
            # "Automatic merge failed; fix conflicts and then commit the result."
            
            # 1. Abre los archivos con conflictos y verás marcadores:
            # <<<<<<< HEAD
            # Contenido en la rama actual (main)
            # =======
            # Contenido en la rama que estás fusionando (feature-branch)
            # >>>>>>> feature-branch
            
            # 2. Edita los archivos para resolver los conflictos
            # 3. Elimina los marcadores de conflicto
            
            # 4. Marca los archivos como resueltos
            git add archivo.txt
            
            # 5. Completa la fusión con un commit
            git commit
            
            # Git usará un mensaje predeterminado indicando la fusión
            """)
            
            # Editor simulado para resolución de conflictos
            st.markdown("#### Simulador de Resolución de Conflictos")
            
            st.markdown("""
            Archivo: `index.html` con conflicto:
            """)
            
            conflicto = """<<<<<<< HEAD
<h1>Página de Inicio</h1>
<p>Bienvenido a nuestra aplicación</p>
=======
<h1>Página Principal</h1>
<p>Bienvenido a nuestro sitio web</p>
>>>>>>> feature/homepage-redesign"""
            
            st.code(conflicto, language="html")
            
            solucion = st.text_area(
                "Edita para resolver el conflicto (elimina los marcadores <<<, === y >>> y deja solo el contenido que quieres conservar):",
                value=conflicto,
                height=200
            )
            
            if st.button("Verificar Resolución"):
                if "<<<<<<< HEAD" not in solucion and "=======" not in solucion and ">>>>>>> feature/homepage-redesign" not in solucion:
                    st.success("¡Conflicto resuelto correctamente! Ahora puedes continuar con el proceso de fusión.")
                    
                    st.code("""
                    # Marcar el archivo como resuelto
                    git add index.html
                    
                    # Completar la fusión
                    git commit
                    """)
                else:
                    st.error("Todavía hay marcadores de conflicto en el archivo. Debes eliminar todos los marcadores <<<, ===, y >>> para resolver correctamente el conflicto.")
    
    with tab4:
        st.markdown("### Estrategias de Ramificación")
        
        st.markdown("""
        Existen varios flujos de trabajo (workflows) populares que definen cómo usar las ramas en proyectos. Cada uno tiene sus propias ventajas según el tamaño del equipo y la complejidad del proyecto.
        """)
        
        # Acordeón para diferentes estrategias
        with st.expander("🌱 Git Flow"):
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.markdown("""
                **Git Flow** es uno de los modelos de ramificación más conocidos, creado por Vincent Driessen.
                
                Utiliza las siguientes ramas:
                
                - **master/main**: Código en producción
                - **develop**: Código para la próxima versión
                - **feature/\***: Nuevas características
                - **release/\***: Preparación para lanzamiento
                - **hotfix/\***: Correcciones urgentes para producción
                
                Es ideal para proyectos con ciclos de lanzamiento planificados.
                """)
                
                st.code("""
                # Ejemplo de flujo Git Flow
                
                # Iniciar una característica
                git checkout develop
                git checkout -b feature/nueva-funcionalidad
                
                # Finalizar una característica
                git checkout develop
                git merge --no-ff feature/nueva-funcionalidad
                git branch -d feature/nueva-funcionalidad
                
                # Iniciar un lanzamiento
                git checkout develop
                git checkout -b release/1.0.0
                
                # Finalizar un lanzamiento
                git checkout main
                git merge --no-ff release/1.0.0
                git tag -a v1.0.0
                git checkout develop
                git merge --no-ff release/1.0.0
                git branch -d release/1.0.0
                """)
                
            with col2:
                st.image("https://nvie.com/img/git-model@2x.png", caption="Modelo Git Flow")
        
        with st.expander("🚀 GitHub Flow"):
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.markdown("""
                **GitHub Flow** es un modelo más simple ideal para despliegues continuos.
                
                Principios clave:
                
                - La rama principal (`main`) siempre está lista para producción
                - Crear ramas descriptivas para nuevos trabajos
                - Abrir Pull Requests para iniciar discusiones
                - Merge a `main` solo después de revisión y aprobación
                - Desplegar inmediatamente después del merge
                
                Es ideal para equipos que despliegan frecuentemente.
                """)
                
                st.code("""
                # Ejemplo de GitHub Flow
                
                # Crear una rama para trabajar
                git checkout -b mejora-formulario-contacto
                
                # Hacer cambios, commit y push
                git add .
                git commit -m "Mejorar validación del formulario"
                git push -u origin mejora-formulario-contacto
                
                # Abrir Pull Request en GitHub
                # Después de revisión y aprobación:
                
                git checkout main
                git pull
                git merge --no-ff mejora-formulario-contacto
                git push
                
                # Desplegar a producción
                # Eliminar la rama
                git branch -d mejora-formulario-contacto
                """)
                
            with col2:
                st.image("https://user-images.githubusercontent.com/7321362/52080877-5a7a5f00-2565-11e9-9ccd-e2478ad3e2a3.png", caption="GitHub Flow")
        
        with st.expander("🔄 Trunk-Based Development"):
            st.markdown("""
            **Trunk-Based Development** es un enfoque donde los desarrolladores colaboran en una única rama (trunk/main).
            
            Características principales:
            
            - Commits pequeños y frecuentes directamente en la rama principal
            - Uso de Feature Flags para ocultar funcionalidades incompletas
            - Integración continua (CI) para validar cada cambio
            - Las ramas de características son de vida muy corta (1-2 días máximo)
            
            Es ideal para equipos experimentados con buena cobertura de pruebas.
            """)
            
            st.code("""
            # Ejemplo de Trunk-Based Development
            
            # Actualizar la rama principal
            git checkout main
            git pull
            
            # Crear una pequeña rama para un cambio (opcional)
            git checkout -b pequeño-cambio
            
            # Hacer cambios, probar y confirmar
            git add .
            git commit -m "Implementar pequeño cambio"
            
            # Integrar rápidamente con main
            git checkout main
            git pull
            git merge pequeño-cambio
            git push
            git branch -d pequeño-cambio
            """)
        
        # Comparativa de estrategias
        st.markdown("### Comparativa de Estrategias de Ramificación")
        
        data = {
            "Estrategia": ["Git Flow", "GitHub Flow", "Trunk-Based"],
            "Complejidad": ["Alta", "Media", "Baja"],
            "Ciclo de lanzamiento": ["Planificado", "Continuo", "Continuo"],
            "Ideal para": ["Proyectos grandes con versiones", "Despliegue continuo", "Equipos experimentados con CI/CD"],
            "Ventajas": ["Estructura clara, gestión de versiones", "Simple, favorece despliegue rápido", "Integración continua, menos conflictos"],
            "Desventajas": ["Complejo, potenciales conflictos grandes", "Requiere buena cultura de review", "Requiere pruebas automatizadas extensas"]
        }
        
        # Crear una tabla de comparación (en Streamlit real esto sería más elegante)
        for i in range(len(data["Estrategia"])):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"**{data['Estrategia'][i]}**")
            with col2:
                st.markdown(f"Complejidad: {data['Complejidad'][i]}")
                st.markdown(f"Ciclo: {data['Ciclo de lanzamiento'][i]}")
            with col3:
                st.markdown(f"Ideal: {data['Ideal para'][i]}")
            st.markdown("---")
        
        # Recomendador de estrategia
        st.markdown("### Recomendador de Estrategia")
        
        tamano_equipo = st.radio("Tamaño del equipo:", ["Pequeño (1-5)", "Mediano (6-15)", "Grande (16+)"])
        ciclo_lanzamiento = st.radio("Ciclo de lanzamiento:", ["Continuo (varias veces al día/semana)", "Regular (cada 2-4 semanas)", "Planificado (meses)"])
        nivel_experiencia = st.radio("Nivel de experiencia del equipo:", ["Principiante", "Intermedio", "Avanzado"])
        
        if st.button("Recomendar Estrategia"):
            if ciclo_lanzamiento == "Planificado (meses)" or tamano_equipo == "Grande (16+)":
                st.success("Recomendación: **Git Flow**")
                st.markdown("Git Flow proporciona estructura clara para equipos grandes o proyectos con lanzamientos planificados.")
            elif nivel_experiencia == "Avanzado" and ciclo_lanzamiento == "Continuo (varias veces al día/semana)":
                st.success("Recomendación: **Trunk-Based Development**")
                st.markdown("Trunk-Based Development funciona bien para equipos experimentados con integración continua y despliegue frecuente.")
            else:
                st.success("Recomendación: **GitHub Flow**")
                st.markdown("GitHub Flow ofrece un buen balance entre simplicidad y estructura para la mayoría de los equipos.")
    
    with tab5:
        st.markdown("<h3 class='subheader'>Quiz: Ramas y Fusiones</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        Comprueba tu conocimiento sobre ramas y fusiones en Git:
        """)
        
        # Pregunta 1
        q1 = st.radio(
            "1. ¿Qué comando crea una nueva rama y cambia a ella inmediatamente?",
            ["git branch nueva-rama", "git checkout nueva-rama", "git checkout -b nueva-rama", "git create nueva-rama"]
        )
        
        # Pregunta 2
        q2 = st.radio(
            "2. ¿Cuándo ocurre una fusión 'fast-forward'?",
            [
                "Cuando hay conflictos en la fusión", 
                "Cuando la rama de destino no ha avanzado desde que se creó la rama a fusionar",
                "Cuando se usa la opción --fast-forward",
                "Cuando se fusionan más de dos ramas a la vez"
            ]
        )
        
        # Pregunta 3
        q3 = st.radio(
            "3. ¿Qué indican estos marcadores en un archivo durante una fusión: <<<<<<< HEAD ... ======= ... >>>>>>> feature-branch?",
            [
                "Un error en el archivo que debe corregirse",
                "Comentarios automáticos generados por Git",
                "Un conflicto de fusión que debe resolverse manualmente",
                "Diferencias entre la versión local y remota"
            ]
        )
        
        # Pregunta 4
        q4 = st.radio(
            "4. ¿Cuál NO es una estrategia común de ramificación en Git?",
            [
                "Git Flow", 
                "GitHub Flow",
                "Trunk-Based Development",
                "Master-Only Flow"
            ]
        )
        
        # Pregunta 5
        q5 = st.radio(
            "5. Después de completar una fusión, ¿qué comando elimina la rama que ya no es necesaria?",
            [
                "git remove branch-name",
                "git branch -d branch-name",
                "git delete branch-name",
                "git branch --remove branch-name"
            ]
        )
        
        # Botón para verificar respuestas
        if st.button("Verificar Respuestas"):
            score = 0
            
            if q1 == "git checkout -b nueva-rama":
                score += 1
            
            if q2 == "Cuando la rama de destino no ha avanzado desde que se creó la rama a fusionar":
                score += 1
                
            if q3 == "Un conflicto de fusión que debe resolverse manualmente":
                score += 1
                
            if q4 == "Master-Only Flow":
                score += 1
                
            if q5 == "git branch -d branch-name":
                score += 1
            
            st.success(f"¡Obtuviste {score} de 5 respuestas correctas!")
            
            if score == 5:
                st.balloons()
                st.markdown("### 🏆 ¡Perfecto! Dominas el trabajo con ramas y fusiones.")
            elif score >= 3:
                st.markdown("### 👍 ¡Buen trabajo! Tienes un buen entendimiento de las ramas en Git.")
            else:
                st.markdown("### 📚 Revisa nuevamente el material para reforzar tus conocimientos sobre ramas y fusiones.")
