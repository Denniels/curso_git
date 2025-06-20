import streamlit as st

def mostrar_contenido():
    st.markdown("<h2 class='module-header'>Resolución de Conflictos</h2>", unsafe_allow_html=True)
    
    # Tabs para organizar el contenido
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["¿Qué son conflictos?", "Identificación", "Resolución Manual", "Herramientas", "Quiz"])
    
    with tab1:
        st.markdown("### Entendiendo los Conflictos en Git")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            Un **conflicto** en Git ocurre cuando dos ramas modifican la misma parte de un archivo de diferentes maneras, 
            y luego intentas fusionarlas. Git no puede decidir automáticamente qué cambio debe prevalecer.
            
            <div class='highlight'>
            Los conflictos son una parte normal del desarrollo colaborativo y aprender a resolverlos es una habilidad esencial.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            #### ¿Cuándo ocurren los conflictos?
            
            Los conflictos suelen ocurrir durante estas operaciones:
            
            1. **Merge**: Al fusionar una rama con otra
            2. **Pull**: Al obtener e integrar cambios remotos
            3. **Rebase**: Al reordenar commits sobre otra base
            4. **Cherry-pick**: Al aplicar commits específicos
            5. **Stash apply**: Al aplicar cambios guardados
            
            Git puede resolver automáticamente muchos cambios, pero necesita ayuda cuando las mismas líneas han sido modificadas de maneras diferentes.
            """)
            
            st.markdown("""
            #### Tipos de conflictos comunes
            
            1. **Conflicto de contenido**: Cambios en las mismas líneas
            2. **Conflicto de eliminación**: Un archivo fue modificado en una rama y eliminado en otra
            3. **Conflicto de modo**: Un archivo cambió de modo (ejecutable/no-ejecutable) en diferentes ramas
            4. **Conflicto de renombrado**: Un archivo fue renombrado en una rama y modificado en otra
            """)
        
        with col2:
            # Imagen conceptual de conflicto
            st.image("https://wac-cdn.atlassian.com/dam/jcr:0269bb2d-eb7f-43d8-acf5-5232f2e8affa/02.svg?cdnVersion=1194", caption="Conflicto en Git")
            
            st.markdown("""
            <div class='warning'>
            <b>Importante:</b> Los conflictos no son errores, son situaciones donde Git necesita tu decisión para continuar.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='tip'>
            <b>Prevención:</b> Puedes reducir los conflictos:
            
            - Sincronizando frecuentemente con el repositorio principal
            - Dividiendo el trabajo en unidades más pequeñas
            - Comunicándote bien con tu equipo sobre qué archivos está modificando cada uno
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Identificando Conflictos")
        
        st.markdown("""
        Cuando ocurre un conflicto, Git pausa la operación (merge, rebase, etc.) y marca los archivos en conflicto para que puedas resolverlos.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Mensajes de Conflicto")
            
            st.code("""
            $ git merge feature-branch
            Auto-merging index.html
            CONFLICT (content): Merge conflict in index.html
            Automatic merge failed; fix conflicts and then commit the result.
            """)
            
            st.markdown("""
            El comando `git status` muestra los archivos en conflicto:
            """)
            
            st.code("""
            $ git status
            On branch main
            You have unmerged paths.
              (fix conflicts and run "git commit")
              (use "git merge --abort" to abort the merge)
            
            Unmerged paths:
              (use "git add <file>..." to mark resolution)
              both modified:   index.html
            """)
        
        with col2:
            st.markdown("#### Marcadores de Conflicto")
            
            st.markdown("""
            Git inserta marcadores especiales en los archivos en conflicto:
            """)
            
            st.code("""
            <<<<<<< HEAD
            <h1>Página de Inicio</h1>
            <p>Bienvenido a nuestra aplicación</p>
            =======
            <h1>Página Principal</h1>
            <p>Bienvenido a nuestro sitio web</p>
            >>>>>>> feature-branch
            """, language="html")
            
            st.markdown("""
            **Interpretación:**
            
            - `<<<<<<< HEAD`: Inicio del contenido de la rama actual
            - `=======`: Separador entre las versiones en conflicto
            - `>>>>>>> feature-branch`: Fin del contenido de la rama que estás fusionando
            """)
        
        # Visualizador de conflictos
        st.markdown("### Visualizador de Conflictos")
        
        st.markdown("""
        Veamos cómo se generan los conflictos con un ejemplo práctico:
        """)
        
        st.markdown("""
        **Escenario:** Dos desarrolladores modifican el mismo archivo
        """)
        
        code_original = """function calcularTotal(items) {
  let total = 0;
  for (let i = 0; i < items.length; i++) {
    total += items[i].precio;
  }
  return total;
}"""

        st.markdown("**Archivo original:**")
        st.code(code_original, language="javascript")
        
        code_dev1 = """function calcularTotal(items) {
  let total = 0;
  for (let i = 0; i < items.length; i++) {
    total += items[i].precio * items[i].cantidad;
  }
  return total;
}"""

        st.markdown("**Cambios del Desarrollador 1 (rama main):**")
        st.code(code_dev1, language="javascript")
        
        code_dev2 = """function calcularTotal(items) {
  if (!items || items.length === 0) return 0;
  
  let total = 0;
  for (let i = 0; i < items.length; i++) {
    total += items[i].precio;
  }
  return total;
}"""

        st.markdown("**Cambios del Desarrollador 2 (rama feature):**")
        st.code(code_dev2, language="javascript")
        
        st.markdown("**Resultado al intentar fusionar:**")
        
        code_conflict = """function calcularTotal(items) {
<<<<<<< HEAD
  let total = 0;
  for (let i = 0; i < items.length; i++) {
    total += items[i].precio * items[i].cantidad;
  }
=======
  if (!items || items.length === 0) return 0;
  
  let total = 0;
  for (let i = 0; i < items.length; i++) {
    total += items[i].precio;
  }
>>>>>>> feature
  return total;
}"""

        st.code(code_conflict, language="javascript")
        
        st.markdown("""
        <div class='warning'>
        Ahora Git espera que resuelvas este conflicto antes de completar la fusión.
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### Resolución Manual de Conflictos")
        
        st.markdown("""
        La resolución de conflictos requiere que edites los archivos en conflicto para elegir qué cambios mantener.
        """)
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("#### Pasos para Resolver Conflictos")
            
            st.markdown("""
            1. **Identificar** los archivos en conflicto usando `git status`
            
            2. **Abrir** cada archivo en conflicto en tu editor
            
            3. **Editar** el archivo para resolver el conflicto:
               - Eliminar los marcadores (`<<<<<<<`, `=======`, `>>>>>>>`)
               - Mantener el código que deseas conservar
               - Puedes combinar cambios de ambas versiones si es apropiado
            
            4. **Marcar** como resuelto con `git add`
            
            5. **Continuar** el proceso:
               - Para merge: `git commit`
               - Para rebase: `git rebase --continue`
            """)
            
            st.markdown("#### Ejemplo de Resolución")
            
            st.code("""
            # 1. Ver el estado para identificar conflictos
            git status
            
            # 2. Editar el archivo en conflicto en tu editor favorito
            code index.html  # o vim, nano, etc.
            
            # 3. Después de resolver, marcar como resuelto
            git add index.html
            
            # 4. Completar el merge
            git commit
            
            # Git abrirá el editor con un mensaje predeterminado
            # Puedes aceptarlo o modificarlo
            """)
        
        with col2:
            st.markdown("""
            <div class='tip'>
            <b>Consejos para la resolución efectiva:</b>
            
            - Entiende ambos cambios antes de decidir
            - Comunícate con el otro desarrollador si es necesario
            - Considera la funcionalidad y no solo el código
            - Prueba el código después de resolver
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='warning'>
            Si te encuentras perdido y quieres empezar de nuevo:
            
            - Para abortar un merge: <code>git merge --abort</code>
            - Para abortar un rebase: <code>git rebase --abort</code>
            - Para abortar un cherry-pick: <code>git cherry-pick --abort</code>
            </div>
            """, unsafe_allow_html=True)
        
        # Simulador de resolución de conflictos
        st.markdown("### Simulador de Resolución de Conflictos")
        
        st.markdown("""
        Practica la resolución de conflictos con este ejemplo:
        """)
        
        conflict_file = """<<<<<<< HEAD
def calculate_discount(price, discount_percentage):
    return price - (price * discount_percentage / 100)
=======
def calculate_discount(price, discount_percentage):
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    return price * (1 - discount_percentage / 100)
>>>>>>> feature/improved-discount
"""
        
        st.code(conflict_file, language="python")
        
        st.markdown("**Edita el código para resolver el conflicto:**")
        
        resolved_code = st.text_area(
            "Código resuelto (elimina los marcadores y conserva el código correcto):",
            value=conflict_file,
            height=250
        )
        
        if st.button("Verificar Resolución"):
            # Verificar si los marcadores han sido eliminados
            if "<<<<<<< HEAD" not in resolved_code and \
               "=======" not in resolved_code and \
               ">>>>>>> feature/improved-discount" not in resolved_code:
                
                # Verificar que el código contiene las validaciones (de la rama feature)
                if "if discount_percentage < 0 or discount_percentage > 100" in resolved_code and \
                   "raise ValueError" in resolved_code:
                    
                    st.success("""
                    ¡Excelente! Has resuelto el conflicto correctamente y has mantenido la validación de la rama feature.
                    
                    Ahora completarías el proceso con:
                    ```
                    git add calculate_discount.py
                    git commit
                    ```
                    """)
                    
                    st.code("""
                    # Código final resuelto
                    def calculate_discount(price, discount_percentage):
                        if discount_percentage < 0 or discount_percentage > 100:
                            raise ValueError("Discount percentage must be between 0 and 100")
                        return price - (price * discount_percentage / 100)
                    """, language="python")
                    
                else:
                    st.warning("""
                    Has eliminado los marcadores de conflicto, pero es importante considerar los cambios de ambas versiones.
                    
                    La versión de la rama feature añade validación importante que probablemente deberías mantener.
                    """)
            else:
                st.error("""
                Todavía hay marcadores de conflicto en el código. 
                
                Debes eliminar las líneas con:
                - <<<<<<< HEAD
                - =======
                - >>>>>>> feature/improved-discount
                
                Y decidir qué código mantener.
                """)
    
    with tab4:
        st.markdown("### Herramientas para Resolución de Conflictos")
        
        st.markdown("""
        Existen numerosas herramientas que pueden facilitar la resolución de conflictos más allá de la edición manual de archivos.
        """)
        
        # Acordeón para diferentes herramientas
        with st.expander("🛠️ Herramientas Integradas en Git"):
            st.markdown("""
            Git incluye herramientas básicas para ayudar en la resolución:
            
            #### mergetool
            
            Git puede invocar una herramienta externa de fusión:
            
            ```bash
            # Configurar tu herramienta preferida
            git config --global merge.tool meld  # o kdiff3, vimdiff, etc.
            
            # Lanzar la herramienta para todos los archivos en conflicto
            git mergetool
            ```
            
            #### diff3
            
            Muestra el ancestro común además de las dos versiones en conflicto:
            
            ```bash
            # Configurar diff3 como estilo de conflicto
            git config --global merge.conflictstyle diff3
            ```
            
            Resultado:
            ```
            <<<<<<< HEAD
            líneas de la rama actual
            ||||||| ancestor
            líneas del ancestro común
            =======
            líneas de la rama a fusionar
            >>>>>>> branch-name
            ```
            """)
        
        with st.expander("💻 Editores de Código e IDEs"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                Los editores modernos tienen excelente soporte para resolver conflictos:
                
                #### Visual Studio Code
                
                - Muestra los conflictos con colores para diferenciar
                - Botones "Accept Current", "Accept Incoming", "Accept Both"
                - Visualización de cambios lado a lado
                
                #### JetBrains IDEs (IntelliJ, PyCharm, etc.)
                
                - Herramienta visual de merge de 3 paneles
                - Resolución por bloques o líneas
                - Navegación entre conflictos
                
                #### Sublime Merge
                
                - Interfaz limpia de tres vías
                - Integración perfecta con Sublime Text
                - Navegación rápida entre conflictos
                """)
            
            with col2:
                # Imagen de una herramienta de resolución de conflictos en un IDE
                st.image("https://code.visualstudio.com/assets/docs/editor/versioncontrol/merge-editor.png", caption="Editor de Merge en VS Code")
        
        with st.expander("🖥️ Herramientas Externas"):
            st.markdown("""
            Aplicaciones especializadas para resolución de conflictos:
            
            #### Meld
            
            - Comparación visual de tres vías
            - Interfaz intuitiva
            - Disponible en Windows, macOS y Linux
            - Gratis y open source
            
            #### Beyond Compare
            
            - Herramienta profesional de comparación
            - Visualización avanzada de diferencias
            - Manejo de directorios y archivos
            - Comercial con prueba gratuita
            
            #### KDiff3
            
            - Comparación y fusión de tres archivos o directorios
            - Resaltado de sintaxis
            - Open source
            - Potente pero con interfaz algo anticuada
            
            #### P4Merge
            
            - Herramienta gratuita de Perforce
            - Visualización gráfica de tres vías
            - Disponible en todas las plataformas
            """)
            
            st.code("""
            # Configurar P4Merge como herramienta de fusión
            git config --global merge.tool p4merge
            git config --global mergetool.p4merge.path "C:/Program Files/Perforce/p4merge.exe"
            git config --global mergetool.keepBackup false
            """)
        
        # Práctica interactiva con herramientas
        st.markdown("### Configuración Recomendada para VS Code")
        
        st.markdown("""
        Visual Studio Code es una excelente opción para resolver conflictos. Así puedes configurarlo:
        """)
        
        st.code("""
        # Configurar VS Code como herramienta de diff y merge
        git config --global diff.tool vscode
        git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE"
        
        git config --global merge.tool vscode
        git config --global mergetool.vscode.cmd "code --wait $MERGED"
        
        # Desactivar los archivos de backup
        git config --global mergetool.keepBackup false
        """)
        
        st.markdown("""
        <div class='tip'>
        <b>Extensiones recomendadas para VS Code:</b>
        
        - "Git Graph" para visualizar la historia del repositorio
        - "GitLens" para anotaciones y exploración avanzada
        - "Git History" para explorar y comparar revisiones
        </div>
        """, unsafe_allow_html=True)
        
        # Demo visual de resolución con herramienta
        st.markdown("### Demostración Visual")
        
        st.markdown("""
        Cuando resuelves un conflicto con una herramienta visual, generalmente verás una interfaz de tres paneles:
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**LOCAL (HEAD)**")
            st.code("""
            function calcularPrecio(base, impuesto) {
                return base * (1 + impuesto / 100);
            }
            """, language="javascript")
        
        with col2:
            st.markdown("**BASE (Común)**")
            st.code("""
            function calcularPrecio(base, impuesto) {
                return base + (base * impuesto / 100);
            }
            """, language="javascript")
        
        with col3:
            st.markdown("**REMOTE (Feature)**")
            st.code("""
            function calcularPrecio(base, impuesto) {
                if (impuesto < 0) {
                    throw new Error("Impuesto inválido");
                }
                return base + (base * impuesto / 100);
            }
            """, language="javascript")
        
        st.markdown("**Resultado después de resolver:**")
        st.code("""
        function calcularPrecio(base, impuesto) {
            if (impuesto < 0) {
                throw new Error("Impuesto inválido");
            }
            return base * (1 + impuesto / 100);
        }
        """, language="javascript")
        
        st.markdown("""
        <div class='highlight'>
        La resolución efectiva a menudo implica combinar lo mejor de ambos cambios, como en este ejemplo donde conservamos:
        <ul>
        <li>La validación de impuesto negativo de la versión REMOTE</li>
        <li>La fórmula matemática mejorada de la versión LOCAL</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab5:
        st.markdown("<h3 class='subheader'>Quiz: Resolución de Conflictos</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        Comprueba tu conocimiento sobre resolución de conflictos:
        """)
        
        # Pregunta 1
        q1 = st.radio(
            "1. ¿Cuándo ocurre un conflicto en Git?",
            [
                "Cuando un archivo es demasiado grande", 
                "Cuando dos ramas modifican el mismo archivo",
                "Cuando dos ramas modifican las mismas líneas de un archivo de diferentes maneras",
                "Cuando Git detecta errores de sintaxis en el código"
            ]
        )
        
        # Pregunta 2
        q2 = st.radio(
            "2. ¿Qué indica el marcador '<<<<<<< HEAD' en un archivo con conflictos?",
            [
                "El inicio del contenido de la rama actual", 
                "El inicio del contenido de la rama que estás fusionando",
                "Un error en el archivo",
                "El fin del archivo"
            ]
        )
        
        # Pregunta 3
        q3 = st.radio(
            "3. ¿Qué comando usarías para abortar un proceso de fusión con conflictos?",
            [
                "git conflict --abort",
                "git merge --stop",
                "git merge --abort",
                "git reset --hard"
            ]
        )
        
        # Pregunta 4
        q4 = st.radio(
            "4. Después de resolver manualmente los conflictos en un archivo, ¿qué debes hacer?",
            [
                "git conflict --resolved", 
                "git add <archivo>",
                "git resolve <archivo>",
                "git continue"
            ]
        )
        
        # Pregunta 5
        q5 = st.radio(
            "5. ¿Qué comando configura una herramienta externa para resolver conflictos?",
            [
                "git config conflict.tool",
                "git conflict --tool",
                "git config --global merge.tool <herramienta>",
                "git tool --set <herramienta>"
            ]
        )
        
        # Botón para verificar respuestas
        if st.button("Verificar Respuestas"):
            score = 0
            
            if q1 == "Cuando dos ramas modifican las mismas líneas de un archivo de diferentes maneras":
                score += 1
            
            if q2 == "El inicio del contenido de la rama actual":
                score += 1
                
            if q3 == "git merge --abort":
                score += 1
                
            if q4 == "git add <archivo>":
                score += 1
                
            if q5 == "git config --global merge.tool <herramienta>":
                score += 1
            
            st.success(f"¡Obtuviste {score} de 5 respuestas correctas!")
            
            if score == 5:
                st.balloons()
                st.markdown("### 🏆 ¡Perfecto! Dominas los conceptos de resolución de conflictos.")
            elif score >= 3:
                st.markdown("### 👍 ¡Buen trabajo! Tienes un buen entendimiento de cómo manejar conflictos.")
            else:
                st.markdown("### 📚 Revisa nuevamente el material para reforzar tus conocimientos sobre resolución de conflictos.")
