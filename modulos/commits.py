import streamlit as st

def mostrar_contenido():
    st.markdown("<h2 class='module-header'>Commits y Control de Versiones</h2>", unsafe_allow_html=True)
    
    # Tabs para organizar el contenido
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Primeros Pasos", "Ciclo de Vida", "Buenas Prácticas", "Comandos Avanzados", "Quiz"])
    
    with tab1:
        st.markdown("### Primeros Pasos con Commits")
        
        st.markdown("""
        Los **commits** son la unidad fundamental de trabajo en Git. Cada commit captura un punto específico 
        en la historia de tu proyecto, permitiéndote volver a ese estado en cualquier momento.
        """)
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("#### Creando tu primer repositorio")
            
            st.code("""
            # Iniciar un nuevo repositorio
            mkdir mi-proyecto
            cd mi-proyecto
            git init
            """)
            
            st.markdown("""
            <div class='highlight'>
            El comando <code>git init</code> crea un subdirectorio oculto <code>.git</code> que contiene 
            toda la estructura necesaria para el control de versiones.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### Tu primer commit")
            
            st.code("""
            # Crear un archivo de ejemplo
            echo "# Mi Proyecto" > README.md
            
            # Añadir el archivo al área de preparación
            git add README.md
            
            # Confirmar los cambios
            git commit -m "Primer commit: añadir README"
            """)
        
        with col2:
            st.image("https://git-scm.com/book/en/v2/images/commit-and-tree.png", caption="Estructura de un commit")
            
            st.markdown("""
            <div class='tip'>
            <b>Consejo:</b> Crea un archivo <code>README.md</code> para documentar tu proyecto.
            Este archivo suele ser lo primero que ven las personas al visitar tu repositorio.
            </div>
            """, unsafe_allow_html=True)
        
        # Simulador de primer commit
        st.markdown("### Simulador de Primer Commit")
        
        nombre_proyecto = st.text_input("Nombre de tu proyecto:", placeholder="mi-awesome-project")
        descripcion = st.text_area("Descripción (para el README):", placeholder="Este proyecto es...")
        
        if nombre_proyecto and descripcion:
            st.markdown("#### Comandos para ejecutar:")
            
            st.code(f"""
            mkdir {nombre_proyecto}
            cd {nombre_proyecto}
            git init
            echo "# {nombre_proyecto}\n\n{descripcion}" > README.md
            git add README.md
            git commit -m "Primer commit: inicializar proyecto"
            """)
            
            st.success("¡Estás listo para crear tu primer repositorio Git!")
    
    with tab2:
        st.markdown("### Ciclo de Vida de los Archivos en Git")
        
        st.markdown("""
        Los archivos en Git pasan por distintos estados a medida que trabajas con ellos:
        """)
        
        # Diagrama del ciclo de vida
        st.image("https://git-scm.com/book/en/v2/images/lifecycle.png", caption="Ciclo de vida de los archivos en Git")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            1. **Sin seguimiento (Untracked)**: Archivos que Git no conoce todavía
            2. **Modificado (Modified)**: Archivos que han cambiado pero no están preparados para commit
            3. **Preparado (Staged)**: Archivos marcados para incluirse en el próximo commit
            4. **Confirmado (Committed)**: Archivos almacenados en el historial de Git
            """)
        
        with col2:
            st.markdown("#### Comandos principales del ciclo")
            
            st.code("""
            # Ver el estado actual
            git status
            
            # Añadir archivos al área de preparación
            git add archivo.txt
            git add .  # Añadir todos los archivos
            
            # Confirmar cambios preparados
            git commit -m "Mensaje descriptivo"
            """)
        
        st.markdown("### Herramientas interactivas")
        
        # Simulador de ciclo de vida
        st.markdown("#### Simulador de ciclo de vida")
        
        archivo = st.selectbox(
            "Selecciona un archivo para simular su ciclo:",
            ["index.html", "estilos.css", "app.js"]
        )
        
        accion = st.radio(
            "¿Qué acción quieres realizar?",
            ["Crear archivo (Untracked)", "Modificar archivo (Modified)", "Preparar para commit (Staged)", "Confirmar cambios (Committed)"]
        )
        
        if accion == "Crear archivo (Untracked)":
            st.code(f"""
            # Crear el archivo {archivo}
            touch {archivo}
            
            # Verificar estado
            git status  # Mostrará {archivo} como "Untracked file"
            """)
            
        elif accion == "Modificar archivo (Modified)":
            st.code(f"""
            # Modificar el archivo {archivo}
            echo "Contenido nuevo" >> {archivo}
            
            # Verificar estado
            git status  # Mostrará {archivo} como "modified"
            """)
            
        elif accion == "Preparar para commit (Staged)":
            st.code(f"""
            # Preparar el archivo {archivo} para commit
            git add {archivo}
            
            # Verificar estado
            git status  # Mostrará {archivo} como "Changes to be committed"
            """)
            
        elif accion == "Confirmar cambios (Committed)":
            mensaje = st.text_input("Mensaje de commit:", placeholder="Actualizar archivo...")
            if mensaje:
                st.code(f"""
                # Confirmar cambios en {archivo}
                git commit -m "{mensaje}"
                
                # Verificar estado
                git status  # Área de trabajo limpia si no hay más cambios
                """)
    
    with tab3:
        st.markdown("### Buenas Prácticas para Commits")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            Un buen commit debe ser:
            
            1. **Atómico**: Representa un cambio lógico único
            2. **Completo**: Incluye todos los archivos necesarios para ese cambio
            3. **Descriptivo**: Tiene un mensaje claro que explica el propósito
            
            Seguir estas prácticas mejora la mantenibilidad y facilita la colaboración.
            """)
            
            st.markdown("#### Mensajes de Commit Efectivos")
            
            st.markdown("""
            Un buen mensaje de commit debería:
            
            - Comenzar con un verbo en imperativo: "Añadir", "Corregir", "Actualizar"
            - Ser breve pero informativo (primera línea ≤ 50 caracteres)
            - Explicar "qué" y "por qué", no el "cómo"
            - Incluir número de issue/ticket cuando sea relevante
            
            <div class='highlight'>
            Estructura recomendada:
            <pre>
            Resumen corto y conciso (≤ 50 caracteres)
            
            Explicación más detallada si es necesario. Mantén las líneas 
            a aproximadamente 72 caracteres. La línea en blanco que separa 
            el resumen del cuerpo es crucial.
            
            - Se pueden incluir puntos clave
            - O detalles adicionales
            
            Fixes #123  # Referencia a issues
            </pre>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### Ejemplos")
            
            st.markdown("""
            <div class='tip'>
            <b>Buen mensaje:</b><br>
            "Añadir validación de formulario de contacto"
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='warning'>
            <b>Mal mensaje:</b><br>
            "Cambios"
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='tip'>
            <b>Buen mensaje (con cuerpo):</b><br>
            "Corregir cálculo de impuestos en carrito de compras
            
            - Soluciona el redondeo incorrecto
            - Añade pruebas unitarias para diferentes escenarios
            - Actualiza documentación
            
            Fixes #456"
            </div>
            """, unsafe_allow_html=True)
        
        # Práctica de mensajes de commit
        st.markdown("### Mejora tus mensajes de commit")
        
        caso = st.selectbox(
            "Selecciona un escenario:",
            [
                "Has añadido un nuevo botón en la página de inicio",
                "Has corregido un error en el cálculo de fechas",
                "Has refactorizado el código de autenticación",
                "Has actualizado dependencias del proyecto"
            ]
        )
        
        mal_mensaje = {
            "Has añadido un nuevo botón en la página de inicio": "Cambios en index",
            "Has corregido un error en el cálculo de fechas": "Fix bug",
            "Has refactorizado el código de autenticación": "Mejoras en código",
            "Has actualizado dependencias del proyecto": "Dependencias"
        }
        
        st.markdown(f"""
        <div class='warning'>
        <b>Mensaje original (deficiente):</b><br>
        "{mal_mensaje[caso]}"
        </div>
        """, unsafe_allow_html=True)
        
        mejor_mensaje = st.text_input("Escribe un mejor mensaje de commit:", placeholder="Añadir...")
        
        if mejor_mensaje:
            # Análisis básico del mensaje
            analisis = []
            if len(mejor_mensaje.split()[0]) > 0 and mejor_mensaje.split()[0].endswith("r"):
                analisis.append("✅ Comienza con un verbo en imperativo")
            else:
                analisis.append("❌ Debería comenzar con un verbo en imperativo (ej: 'Añadir', 'Corregir')")
                
            if len(mejor_mensaje) <= 50:
                analisis.append("✅ Longitud adecuada (≤ 50 caracteres)")
            else:
                analisis.append("❌ Demasiado largo (> 50 caracteres)")
                
            if len(mejor_mensaje.split()) >= 3:
                analisis.append("✅ Suficientemente descriptivo")
            else:
                analisis.append("❌ Podría ser más descriptivo")
            
            st.markdown("#### Análisis de tu mensaje:")
            for punto in analisis:
                st.markdown(punto)
    
    with tab4:
        st.markdown("### Comandos Avanzados de Commits")
        
        # Acordeón para comandos avanzados
        with st.expander("🔍 Ver el historial de commits"):
            st.code("""
            # Ver historial básico
            git log
            
            # Ver historial en una línea por commit
            git log --oneline
            
            # Ver historial con gráfico de ramas
            git log --graph --oneline --all
            
            # Ver cambios detallados en cada commit
            git log -p
            
            # Ver estadísticas resumidas
            git log --stat
            """)
            
            st.markdown("""
            <div class='tip'>
            <b>Consejo:</b> Puedes crear un alias para formatos complejos de log:
            <pre>git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"</pre>
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("🔄 Modificar commits"):
            st.markdown("""
            #### Modificar el último commit
            
            Si olvidaste añadir un archivo o quieres corregir el mensaje:
            """)
            
            st.code("""
            # Modificar el último commit añadiendo cambios
            git add archivo-olvidado.txt
            git commit --amend
            
            # Modificar solo el mensaje del último commit
            git commit --amend -m "Nuevo mensaje corregido"
            """)
            
            st.markdown("""
            <div class='warning'>
            <b>¡Precaución!</b> Nunca modifiques commits que ya hayas compartido con otros (pusheado a un repositorio remoto).
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("↩️ Revertir cambios"):
            st.markdown("""
            #### Deshacer cambios
            """)
            
            st.code("""
            # Deshacer cambios en el área de preparación
            git restore --staged <archivo>  # Git moderno
            git reset HEAD <archivo>        # Git antiguo
            
            # Descartar cambios en el directorio de trabajo
            git restore <archivo>           # Git moderno
            git checkout -- <archivo>       # Git antiguo
            
            # Revertir un commit (crea un nuevo commit que deshace los cambios)
            git revert <commit-hash>
            
            # Eliminar commits (¡peligroso si ya se han compartido!)
            git reset --soft HEAD~1   # Elimina el último commit pero mantiene los cambios preparados
            git reset --mixed HEAD~1  # Elimina el último commit y desmarcar cambios (por defecto)
            git reset --hard HEAD~1   # Elimina el último commit y DESCARTA los cambios (¡cuidado!)
            """)
        
        with st.expander("🏷️ Etiquetar versiones (Tags)"):
            st.markdown("""
            Las etiquetas son referencias a puntos específicos en la historia de Git, útiles para marcar versiones:
            """)
            
            st.code("""
            # Crear una etiqueta ligera
            git tag v1.0.0
            
            # Crear una etiqueta anotada (recomendada)
            git tag -a v1.0.0 -m "Versión 1.0.0 - Primera versión estable"
            
            # Ver etiquetas
            git tag
            
            # Ver información detallada de una etiqueta
            git show v1.0.0
            
            # Etiquetar un commit anterior
            git tag -a v0.9.0 <commit-hash> -m "Versión beta"
            
            # Compartir etiquetas (no se envían por defecto)
            git push origin v1.0.0    # Enviar una etiqueta específica
            git push origin --tags    # Enviar todas las etiquetas
            """)
        
        # Práctica interactiva de comandos avanzados
        st.markdown("### Simulador de escenarios avanzados")
        
        escenario = st.selectbox(
            "Selecciona un escenario para practicar:",
            [
                "Modificar el último commit porque olvidaste un archivo",
                "Revertir un commit que introdujo un error",
                "Etiquetar la versión actual como release",
                "Ver el historial de cambios de forma visual"
            ]
        )
        
        if escenario == "Modificar el último commit porque olvidaste un archivo":
            archivo_olvidado = st.text_input("Nombre del archivo olvidado:", placeholder="config.json")
            if archivo_olvidado:
                st.code(f"""
                # Añadir el archivo olvidado
                git add {archivo_olvidado}
                
                # Modificar el último commit para incluirlo
                git commit --amend --no-edit  # Mantener el mismo mensaje
                
                # O si quieres cambiar también el mensaje:
                # git commit --amend -m "Nuevo mensaje con {archivo_olvidado} incluido"
                """)
        
        elif escenario == "Revertir un commit que introdujo un error":
            st.markdown("""
            Primero, identifica el commit a revertir:
            """)
            st.code("""
            git log --oneline  # Anota el hash del commit problemático
            """)
            
            commit_hash = st.text_input("Hash del commit a revertir:", placeholder="a1b2c3d")
            if commit_hash:
                st.code(f"""
                # Revertir el commit (creará un nuevo commit que deshace los cambios)
                git revert {commit_hash}
                
                # Si no quieres abrir el editor para el mensaje:
                # git revert --no-edit {commit_hash}
                """)
        
        elif escenario == "Etiquetar la versión actual como release":
            version = st.text_input("Número de versión:", placeholder="1.0.0")
            descripcion = st.text_area("Descripción de la versión:", placeholder="Primera versión estable con...")
            
            if version and descripcion:
                st.code(f"""
                # Crear una etiqueta anotada
                git tag -a v{version} -m "{descripcion}"
                
                # Verificar que se creó correctamente
                git show v{version}
                
                # Compartir la etiqueta con el repositorio remoto
                git push origin v{version}
                """)
        
        elif escenario == "Ver el historial de cambios de forma visual":
            formato = st.radio(
                "Selecciona un formato:",
                ["Básico (una línea por commit)", "Gráfico de ramas", "Detallado con cambios", "Personalizado"]
            )
            
            if formato == "Básico (una línea por commit)":
                st.code("""
                git log --oneline
                """)
            elif formato == "Gráfico de ramas":
                st.code("""
                git log --graph --oneline --all --decorate
                """)
            elif formato == "Detallado con cambios":
                st.code("""
                git log -p
                """)
            elif formato == "Personalizado":
                st.code("""
                git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
                """)
                
                st.markdown("""
                <div class='tip'>
                Puedes guardar este formato como un alias para usarlo fácilmente:
                <pre>git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"</pre>
                
                Y luego simplemente usar:
                <pre>git lg</pre>
                </div>
                """, unsafe_allow_html=True)
    
    with tab5:
        st.markdown("<h3 class='subheader'>Quiz: Commits y Control de Versiones</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        Comprueba tu conocimiento sobre commits y control de versiones:
        """)
        
        # Pregunta 1
        q1 = st.radio(
            "1. ¿Qué comando se usa para iniciar un nuevo repositorio Git?",
            ["git start", "git create", "git init", "git new"]
        )
        
        # Pregunta 2
        q2 = st.radio(
            "2. ¿Cuál es el propósito del comando 'git add'?",
            [
                "Crear un nuevo archivo", 
                "Añadir archivos al área de preparación (staging)",
                "Añadir un comentario al commit",
                "Añadir un repositorio remoto"
            ]
        )
        
        # Pregunta 3
        q3 = st.radio(
            "3. ¿Qué opción de 'git commit' te permite modificar el último commit realizado?",
            [
                "--redo",
                "--modify",
                "--amend",
                "--update"
            ]
        )
        
        # Pregunta 4
        q4 = st.radio(
            "4. ¿Cuál es la mejor práctica para un mensaje de commit?",
            [
                "Debe ser lo más largo y detallado posible", 
                "Debe comenzar con un verbo en imperativo y ser conciso",
                "Siempre debe incluir el nombre del autor",
                "No importa el formato mientras explique los cambios"
            ]
        )
        
        # Pregunta 5
        q5 = st.radio(
            "5. ¿Qué comando usarías para ver el historial de commits con un gráfico visual de las ramas?",
            [
                "git history --visual",
                "git log --tree",
                "git log --graph",
                "git show --branches"
            ]
        )
        
        # Botón para verificar respuestas
        if st.button("Verificar Respuestas"):
            score = 0
            
            if q1 == "git init":
                score += 1
            
            if q2 == "Añadir archivos al área de preparación (staging)":
                score += 1
                
            if q3 == "--amend":
                score += 1
                
            if q4 == "Debe comenzar con un verbo en imperativo y ser conciso":
                score += 1
                
            if q5 == "git log --graph":
                score += 1
            
            st.success(f"¡Obtuviste {score} de 5 respuestas correctas!")
            
            if score == 5:
                st.balloons()
                st.markdown("### 🏆 ¡Excelente! Dominas los conceptos de commits y control de versiones.")
            elif score >= 3:
                st.markdown("### 👍 ¡Buen trabajo! Estás comprendiendo bien los conceptos clave.")
            else:
                st.markdown("### 📚 Revisa nuevamente el material para reforzar tus conocimientos sobre commits.")
