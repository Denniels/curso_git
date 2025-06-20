import streamlit as st
import random

def mostrar_contenido():
    st.markdown("<h2 class='module-header'>Evaluación Final del Curso Git y GitHub</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    ¡Felicidades por llegar hasta aquí! Esta evaluación final combina temas de todos los módulos del curso
    para comprobar tu dominio de Git y GitHub. 
    
    La evaluación consta de preguntas teóricas y prácticas que cubren todos los conceptos que hemos visto.
    """)
    
    # Inicialización del estado para seguimiento de respuestas
    if 'score' not in st.session_state:
        st.session_state.score = 0
    
    if 'max_score' not in st.session_state:
        st.session_state.max_score = 0
    
    if 'answered_questions' not in st.session_state:
        st.session_state.answered_questions = set()
    
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    
    # Botón para reiniciar la evaluación
    if st.session_state.submitted:
        if st.button("Reiniciar Evaluación"):
            st.session_state.score = 0
            st.session_state.max_score = 0
            st.session_state.answered_questions = set()
            st.session_state.submitted = False
            st.experimental_rerun()
    
    # Si no se ha enviado la evaluación, mostrar las preguntas
    if not st.session_state.submitted:
        # Sección 1: Fundamentos de Git
        st.markdown("<h3 class='subheader'>Sección 1: Fundamentos de Git</h3>", unsafe_allow_html=True)
        
        # Pregunta 1
        question_id = "q1"
        if question_id not in st.session_state.answered_questions:
            st.markdown("**1. ¿Cuál es el propósito principal de Git?**")
            
            q1 = st.radio(
                "Selecciona la opción correcta:",
                [
                    "Proporcionar alojamiento en la nube para código", 
                    "Realizar copias de seguridad de archivos",
                    "Controlar versiones de código fuente de forma distribuida",
                    "Compilar y ejecutar código automáticamente"
                ],
                key="q1"
            )
            
            # Botón para verificar esta pregunta
            if st.button("Verificar", key="check_q1"):
                st.session_state.max_score += 1
                if q1 == "Controlar versiones de código fuente de forma distribuida":
                    st.success("¡Correcto! Git es un sistema de control de versiones distribuido diseñado para rastrear cambios en el código fuente.")
                    st.session_state.score += 1
                else:
                    st.error("Incorrecto. Git es un sistema de control de versiones distribuido que permite rastrear cambios en el código fuente.")
                
                st.session_state.answered_questions.add(question_id)
        
        # Pregunta 2
        question_id = "q2"
        if question_id not in st.session_state.answered_questions:
            st.markdown("**2. Completa el comando para crear un nuevo repositorio Git local:**")
            
            q2 = st.text_input("Escribe el comando:", placeholder="git ...", key="q2")
            
            # Botón para verificar esta pregunta
            if st.button("Verificar", key="check_q2"):
                st.session_state.max_score += 1
                if q2.strip().lower() == "git init":
                    st.success("¡Correcto! El comando 'git init' inicializa un nuevo repositorio Git.")
                    st.session_state.score += 1
                else:
                    st.error("Incorrecto. El comando correcto es 'git init'.")
                
                st.session_state.answered_questions.add(question_id)
        
        # Pregunta 3
        question_id = "q3"
        if question_id not in st.session_state.answered_questions:
            st.markdown("**3. Relaciona cada término con su definición correcta:**")
            
            options = {
                "Repositorio": ["Lugar donde se almacena el historial de versiones", "Un commit específico", "Un archivo de configuración", "Una copia de seguridad"],
                "Commit": ["Comando para descargar cambios", "Una instantánea del proyecto en un momento específico", "Una rama alternativa", "El directorio de trabajo"],
                "Branch": ["Línea independiente de desarrollo", "El servidor remoto", "Conjunto de commits", "Una marca en el historial"]
            }
            
            user_answers = {}
            for term, defs in options.items():
                user_answers[term] = st.selectbox(f"¿Qué es un {term}?", defs, key=f"q3_{term}")
            
            # Botón para verificar esta pregunta
            if st.button("Verificar", key="check_q3"):
                st.session_state.max_score += 3
                
                correct_answers = {
                    "Repositorio": "Lugar donde se almacena el historial de versiones",
                    "Commit": "Una instantánea del proyecto en un momento específico",
                    "Branch": "Línea independiente de desarrollo"
                }
                
                score = 0
                results = []
                
                for term, correct in correct_answers.items():
                    if user_answers[term] == correct:
                        results.append(f"✅ {term}: Correcto")
                        score += 1
                    else:
                        results.append(f"❌ {term}: Incorrecto. La respuesta correcta es '{correct}'")
                
                for result in results:
                    st.markdown(result)
                
                st.session_state.score += score
                st.markdown(f"**Resultado de la pregunta: {score}/3 puntos**")
                
                st.session_state.answered_questions.add(question_id)
        
        # Sección 2: Commits y Control de Versiones
        st.markdown("<h3 class='subheader'>Sección 2: Commits y Control de Versiones</h3>", unsafe_allow_html=True)
        
        # Pregunta 4
        question_id = "q4"
        if question_id not in st.session_state.answered_questions:
            st.markdown("**4. Ordena los pasos para crear un commit:**")
            
            steps = [
                "Modificar archivos en el directorio de trabajo",
                "Ejecutar git add para preparar los cambios",
                "Ejecutar git commit -m 'mensaje' para confirmar los cambios",
                "Verificar el estado con git status"
            ]
            
            q4_options = steps.copy()
            random.shuffle(q4_options)
            
            q4 = {}
            st.write("Arrastra las opciones en el orden correcto:")
            for i in range(len(q4_options)):
                q4[i] = st.selectbox(f"Paso {i+1}:", q4_options, key=f"q4_{i}")
            
            # Botón para verificar esta pregunta
            if st.button("Verificar", key="check_q4"):
                st.session_state.max_score += 1
                
                # Verificar si el orden es correcto (permitiendo que el paso 4 esté en cualquier posición)
                correct_order = steps.copy()
                last_step = correct_order.pop()  # Remover "Verificar el estado"
                
                user_order = list(q4.values())
                
                # Verificar si los primeros 3 pasos están en orden correcto
                first_three_correct = True
                for i in range(len(correct_order)):
                    if user_order[i] != correct_order[i]:
                        first_three_correct = False
                        break
                
                # Verificar si el último paso está en la posición 4 o en otra posición
                last_step_included = last_step in user_order
                
                if first_three_correct and last_step_included:
                    st.success("¡Correcto! Has ordenado los pasos correctamente.")
                    st.markdown("""
                    El orden correcto es:
                    1. Modificar archivos en el directorio de trabajo
                    2. Ejecutar git add para preparar los cambios
                    3. Ejecutar git commit -m 'mensaje' para confirmar los cambios
                    
                    Nota: "Verificar el estado con git status" puede hacerse en cualquier momento del proceso.
                    """)
                    st.session_state.score += 1
                else:
                    st.error("""
                    Incorrecto. El orden correcto es:
                    1. Modificar archivos en el directorio de trabajo
                    2. Ejecutar git add para preparar los cambios
                    3. Ejecutar git commit -m 'mensaje' para confirmar los cambios
                    
                    Nota: "Verificar el estado con git status" puede hacerse en cualquier momento del proceso.
                    """)
                
                st.session_state.answered_questions.add(question_id)
        
        # Pregunta 5
        question_id = "q5"
        if question_id not in st.session_state.answered_questions:
            st.markdown("**5. Evalúa la calidad de los siguientes mensajes de commit:**")
            
            commit_messages = {
                "Arreglar bug": "Deficiente",
                "Implementar validación de formulario de contacto para prevenir inyección SQL": "Excelente",
                "Cambios": "Deficiente",
                "Actualizar documentación de API con nuevos endpoints y ejemplos de uso": "Excelente"
            }
            
            user_ratings = {}
            for msg, _ in commit_messages.items():
                user_ratings[msg] = st.radio(
                    f"Mensaje: '{msg}'",
                    ["Excelente", "Deficiente"],
                    key=f"q5_{msg}"
                )
            
            # Botón para verificar esta pregunta
            if st.button("Verificar", key="check_q5"):
                st.session_state.max_score += 4
                
                score = 0
                results = []
                
                for msg, correct in commit_messages.items():
                    if user_ratings[msg] == correct:
                        results.append(f"✅ '{msg}': Correcto - Es un mensaje {correct.lower()}")
                        score += 1
                    else:
                        results.append(f"❌ '{msg}': Incorrecto - Es un mensaje {correct.lower()}")
                
                for result in results:
                    st.markdown(result)
                
                st.markdown("""
                **Recordatorio sobre buenos mensajes de commit:**
                - Deben ser descriptivos y explicar el qué y el por qué
                - Deben ser concisos pero informativos
                - Deben comenzar con un verbo en imperativo
                """)
                
                st.session_state.score += score
                st.markdown(f"**Resultado de la pregunta: {score}/4 puntos**")
                
                st.session_state.answered_questions.add(question_id)
        
        # Sección 3: Ramas y Fusiones
        st.markdown("<h3 class='subheader'>Sección 3: Ramas y Fusiones</h3>", unsafe_allow_html=True)
        
        # Pregunta 6
        question_id = "q6"
        if question_id not in st.session_state.answered_questions:
            st.markdown("**6. Completa los comandos para trabajar con ramas:**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                q6_a = st.text_input("Crear una nueva rama:", placeholder="git ...", key="q6_a")
                q6_b = st.text_input("Cambiar a una rama existente:", placeholder="git ...", key="q6_b")
            
            with col2:
                q6_c = st.text_input("Fusionar una rama en la actual:", placeholder="git ...", key="q6_c")
                q6_d = st.text_input("Eliminar una rama:", placeholder="git ...", key="q6_d")
            
            # Botón para verificar esta pregunta
            if st.button("Verificar", key="check_q6"):
                st.session_state.max_score += 4
                
                correct_answers = {
                    "q6_a": ["git branch nombre-rama", "git branch"],
                    "q6_b": ["git checkout nombre-rama", "git checkout", "git switch nombre-rama", "git switch"],
                    "q6_c": ["git merge nombre-rama", "git merge"],
                    "q6_d": ["git branch -d nombre-rama", "git branch -d", "git branch --delete nombre-rama", "git branch --delete"]
                }
                
                score = 0
                results = []
                
                # Verificar cada respuesta (aceptando variantes)
                for key, answer in {"q6_a": q6_a, "q6_b": q6_b, "q6_c": q6_c, "q6_d": q6_d}.items():
                    is_correct = False
                    for correct in correct_answers[key]:
                        if answer.strip().lower().startswith(correct.lower()):
                            is_correct = True
                            break
                    
                    if is_correct:
                        score += 1
                        results.append(f"✅ '{answer}': Correcto")
                    else:
                        results.append(f"❌ '{answer}': Incorrecto - Respuesta correcta: '{correct_answers[key][0]}'")
                
                for result in results:
                    st.markdown(result)
                
                st.session_state.score += score
                st.markdown(f"**Resultado de la pregunta: {score}/4 puntos**")
                
                st.session_state.answered_questions.add(question_id)
        
        # Pregunta 7
        question_id = "q7"
        if question_id not in st.session_state.answered_questions:
            st.markdown("**7. Identifica el tipo de fusión en cada escenario:**")
            
            scenarios = {
                "Rama feature sin nuevos commits en main desde su creación": "Fast-forward",
                "Rama feature y main han evolucionado independientemente": "Recursive (Three-way)",
                "Dos desarrolladores modificaron las mismas líneas en diferentes ramas": "Conflicto de fusión"
            }
            
            user_answers = {}
            for scenario, _ in scenarios.items():
                user_answers[scenario] = st.selectbox(
                    f"Escenario: {scenario}",
                    ["Fast-forward", "Recursive (Three-way)", "Conflicto de fusión"],
                    key=f"q7_{scenario}"
                )
            
            # Botón para verificar esta pregunta
            if st.button("Verificar", key="check_q7"):
                st.session_state.max_score += 3
                
                score = 0
                results = []
                
                for scenario, correct in scenarios.items():
                    if user_answers[scenario] == correct:
                        results.append(f"✅ Correcto: '{scenario}' resulta en una fusión de tipo '{correct}'")
                        score += 1
                    else:
                        results.append(f"❌ Incorrecto: '{scenario}' resulta en una fusión de tipo '{correct}', no '{user_answers[scenario]}'")
                
                for result in results:
                    st.markdown(result)
                
                st.session_state.score += score
                st.markdown(f"**Resultado de la pregunta: {score}/3 puntos**")
                
                st.session_state.answered_questions.add(question_id)
        
        # Sección 4: Repositorios Remotos y GitHub
        st.markdown("<h3 class='subheader'>Sección 4: Repositorios Remotos y GitHub</h3>", unsafe_allow_html=True)
        
        # Pregunta 8
        question_id = "q8"
        if question_id not in st.session_state.answered_questions:
            st.markdown("**8. Completa los comandos para trabajar con repositorios remotos:**")
            
            remote_commands = {
                "Clonar un repositorio remoto": "git clone",
                "Descargar cambios sin fusionar": "git fetch",
                "Descargar y fusionar cambios remotos": "git pull",
                "Enviar cambios locales al remoto": "git push"
            }
            
            user_answers = {}
            for desc, _ in remote_commands.items():
                user_answers[desc] = st.text_input(
                    f"{desc}:",
                    placeholder="git ...",
                    key=f"q8_{desc}"
                )
            
            # Botón para verificar esta pregunta
            if st.button("Verificar", key="check_q8"):
                st.session_state.max_score += 4
                
                score = 0
                results = []
                
                for desc, correct in remote_commands.items():
                    if user_answers[desc].strip().lower().startswith(correct.lower()):
                        results.append(f"✅ '{user_answers[desc]}': Correcto")
                        score += 1
                    else:
                        results.append(f"❌ '{user_answers[desc]}': Incorrecto - Respuesta correcta: '{correct}'")
                
                for result in results:
                    st.markdown(result)
                
                st.session_state.score += score
                st.markdown(f"**Resultado de la pregunta: {score}/4 puntos**")
                
                st.session_state.answered_questions.add(question_id)
        
        # Pregunta 9
        question_id = "q9"
        if question_id not in st.session_state.answered_questions:
            st.markdown("**9. Escenario de GitHub: Identifica los pasos para contribuir a un proyecto open source:**")
            
            steps = [
                "Fork el repositorio original a tu cuenta",
                "Clonar tu fork localmente",
                "Crear una rama para tus cambios",
                "Realizar cambios y hacer commits",
                "Push de la rama a tu fork",
                "Crear un Pull Request al repositorio original"
            ]
            
            q9_options = steps.copy()
            random.shuffle(q9_options)
            
            q9 = {}
            st.write("Arrastra las opciones en el orden correcto:")
            for i in range(len(q9_options)):
                q9[i] = st.selectbox(f"Paso {i+1}:", q9_options, key=f"q9_{i}")
            
            # Botón para verificar esta pregunta
            if st.button("Verificar", key="check_q9"):
                st.session_state.max_score += 6
                
                user_order = list(q9.values())
                score = 0
                
                # Verificar cada paso en su posición correcta
                for i, step in enumerate(steps):
                    if i < len(user_order) and user_order[i] == step:
                        score += 1
                
                if score == len(steps):
                    st.success("¡Perfecto! Has ordenado todos los pasos correctamente.")
                else:
                    st.error(f"Has ordenado {score} de {len(steps)} pasos correctamente.")
                    
                    st.markdown("**El orden correcto es:**")
                    for i, step in enumerate(steps):
                        st.markdown(f"{i+1}. {step}")
                
                st.session_state.score += score
                st.markdown(f"**Resultado de la pregunta: {score}/{len(steps)} puntos**")
                
                st.session_state.answered_questions.add(question_id)
        
        # Sección 5: Resolución de Conflictos
        st.markdown("<h3 class='subheader'>Sección 5: Resolución de Conflictos</h3>", unsafe_allow_html=True)
        
        # Pregunta 10
        question_id = "q10"
        if question_id not in st.session_state.answered_questions:
            st.markdown("**10. Resuelve el siguiente conflicto de fusión:**")
            
            conflict_code = """<<<<<<< HEAD
function calcularPrecio(producto) {
  return producto.precio * 1.16; // Incluye IVA
}
=======
function calcularPrecio(producto) {
  if (!producto.precio) {
    throw new Error('El producto no tiene precio');
  }
  return producto.precio;
}
>>>>>>> feature/validacion-precio"""
            
            st.code(conflict_code, language="javascript")
            
            q10 = st.text_area(
                "Resuelve el conflicto (elimina los marcadores y combina el código apropiadamente):",
                height=200,
                key="q10"
            )
            
            # Botón para verificar esta pregunta
            if st.button("Verificar", key="check_q10"):
                st.session_state.max_score += 3
                
                # Verificar que se eliminaron los marcadores de conflicto
                markers_removed = True
                for marker in ["<<<<<<< HEAD", "=======", ">>>>>>> feature/validacion-precio"]:
                    if marker in q10:
                        markers_removed = False
                        break
                
                # Verificar que se incluyó la validación
                validation_included = "if (!producto.precio)" in q10 and "throw new Error" in q10
                
                # Verificar que se incluyó el cálculo del IVA
                iva_included = "* 1.16" in q10 or "* 1,16" in q10
                
                score = 0
                
                if markers_removed:
                    st.markdown("✅ Correctamente eliminaste los marcadores de conflicto")
                    score += 1
                else:
                    st.markdown("❌ Debes eliminar todos los marcadores de conflicto (`<<<<<<< HEAD`, `=======`, `>>>>>>> feature/validacion-precio`)")
                
                if validation_included:
                    st.markdown("✅ Correctamente incluiste la validación de precio")
                    score += 1
                else:
                    st.markdown("❌ Debes incluir la validación de precio de la rama feature")
                
                if iva_included:
                    st.markdown("✅ Correctamente mantuviste el cálculo del IVA")
                    score += 1
                else:
                    st.markdown("❌ Debes mantener el cálculo del IVA (multiplicación por 1.16)")
                
                if score == 3:
                    st.success("¡Excelente! Has resuelto el conflicto correctamente.")
                    st.code("""
function calcularPrecio(producto) {
  if (!producto.precio) {
    throw new Error('El producto no tiene precio');
  }
  return producto.precio * 1.16; // Incluye IVA
}""", language="javascript")
                else:
                    st.error("La resolución del conflicto no es óptima.")
                    st.markdown("""
                    Una buena resolución combinaría ambas versiones:
                    ```javascript
                    function calcularPrecio(producto) {
                      if (!producto.precio) {
                        throw new Error('El producto no tiene precio');
                      }
                      return producto.precio * 1.16; // Incluye IVA
                    }
                    ```
                    """)
                
                st.session_state.score += score
                st.markdown(f"**Resultado de la pregunta: {score}/3 puntos**")
                
                st.session_state.answered_questions.add(question_id)
        
        # Botón para enviar la evaluación completa
        if len(st.session_state.answered_questions) == 10:
            if st.button("Enviar Evaluación Final"):
                st.session_state.submitted = True
                st.experimental_rerun()
        else:
            st.info(f"Has completado {len(st.session_state.answered_questions)}/10 preguntas. Completa todas las preguntas para enviar la evaluación.")
    
    # Si la evaluación fue enviada, mostrar resultados
    if st.session_state.submitted:
        final_score = st.session_state.score
        max_possible = st.session_state.max_score
        percentage = (final_score / max_possible) * 100
        
        st.markdown(f"### Tu puntuación final: {final_score}/{max_possible} puntos ({percentage:.1f}%)")
        
        # Barra de progreso
        st.progress(percentage / 100)
        
        # Mensaje según la puntuación
        if percentage >= 90:
            st.success("🏆 ¡Excelente! Dominas Git y GitHub. Estás listo para aplicar estos conocimientos en proyectos reales.")
            st.balloons()
        elif percentage >= 75:
            st.success("👍 ¡Muy bien! Tienes un buen entendimiento de Git y GitHub. Practica un poco más para perfeccionar tus habilidades.")
        elif percentage >= 60:
            st.warning("🔍 ¡Buen intento! Comprendes los conceptos básicos, pero considera repasar algunos temas para fortalecer tu conocimiento.")
        else:
            st.error("📚 Es recomendable que repases los módulos del curso. Los conceptos de Git y GitHub requieren práctica continua.")
        
        # Recomendaciones personalizadas
        st.markdown("### Recomendaciones personalizadas:")
        
        # Estas recomendaciones son ficticias, en una implementación real se basarían en el análisis de respuestas específicas
        st.markdown("""
        1. **Práctica regular**: Crea un repositorio personal y practica los comandos diariamente
        2. **Colaboración**: Contribuye a proyectos open source para practicar el flujo de trabajo colaborativo
        3. **Automatización**: Explora GitHub Actions para automatizar tus flujos de trabajo
        4. **Recursos adicionales**: Consulta la documentación oficial y tutoriales avanzados
        """)
        
        # Certificado simbólico
        st.markdown("### ¡Felicitaciones por completar el curso!")
        
        # Aquí se podría incluir un certificado descargable o visualización del mismo
        st.markdown("""
        ```
        ╔══════════════════════════════════════════════════════════════════╗
        ║                                                                  ║
        ║                      CERTIFICADO DE FINALIZACIÓN                 ║
        ║                                                                  ║
        ║                           CURSO DE GIT Y GITHUB                  ║
        ║                                                                  ║
        ║  Este certifica que:                                             ║
        ║                                                                  ║
        ║  [TU NOMBRE]                                                     ║
        ║                                                                  ║
        ║  Ha completado satisfactoriamente el curso interactivo de        ║
        ║  Git y GitHub, demostrando conocimientos en control de           ║
        ║  versiones, colaboración y flujos de trabajo.                    ║
        ║                                                                  ║
        ║  Puntuación: {:.1f}%                                             ║
        ║                                                                  ║
        ║  Fecha: {}                                                     ║
        ║                                                                  ║
        ╚══════════════════════════════════════════════════════════════════╝
        ```
        """.format(percentage, "19 de junio de 2025"))
        
        # Próximos pasos
        st.markdown("### Próximos pasos:")
        
        st.markdown("""
        - **Git Avanzado**: Aprende sobre rebase interactivo, cherry-pick, bisect y más
        - **DevOps**: Explora la integración de Git en pipelines CI/CD
        - **GitHub Enterprise**: Descubre características avanzadas para equipos y empresas
        - **Contribución Open Source**: Aplica tus conocimientos contribuyendo a proyectos reales
        """)
        
        # Feedback del curso
        st.markdown("### Nos encantaría recibir tu feedback:")
        
        feedback = st.text_area("¿Qué te pareció el curso? ¿Hay algo que podríamos mejorar?", height=100)
        rating = st.slider("Califica el curso del 1 al 5:", min_value=1, max_value=5, value=5)
        
        if st.button("Enviar Feedback"):
            if feedback:
                st.success("¡Gracias por tu feedback! Lo tendremos en cuenta para mejorar el curso.")
            else:
                st.info("Por favor, escribe tu feedback antes de enviarlo.")
