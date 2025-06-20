# Curso Interactivo de Git y GitHub

Una aplicación web interactiva desarrollada con Streamlit que funciona como un curso modular sobre Git y GitHub, desde conceptos básicos hasta avanzados, con enfoque práctico y didáctico.

## Características

- **Enfoque modular**: Contenido organizado en módulos progresivos
- **Interactividad**: Ejercicios prácticos, simuladores de comandos Git y GitHub
- **Evaluación continua**: Quizzes en cada módulo y evaluación final
- **Interfaz amigable**: Navegación intuitiva y diseño responsivo
- **Material visual**: Diagramas, ejemplos y explicaciones visuales

## Módulos Incluidos

1. **Introducción a Git**: Conceptos básicos, instalación y configuración
2. **Commits y Control de Versiones**: Trabajo con commits, buenas prácticas
3. **Ramas y Fusiones**: Gestión de ramas, estrategias de fusión
4. **Repositorios Remotos**: Trabajo con GitHub y otras plataformas
5. **Resolución de Conflictos**: Identificación y solución de conflictos
6. **Flujo de Trabajo en GitHub**: PRs, forks, issues y buenas prácticas
7. **Evaluación Final**: Evaluación integradora con todos los conceptos

## Requisitos

- Python 3.8 o superior
- Streamlit y otras dependencias (ver requirements.txt)

## Instalación

1. Clona este repositorio:
```
git clone https://github.com/tu-usuario/curso-git.git
```

2. Instala las dependencias:
```
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```
streamlit run main.py
```

## Despliegue en Streamlit Community Cloud

Este proyecto está configurado para ser desplegado fácilmente en [Streamlit Community Cloud](https://streamlit.io/cloud).

Pasos para el despliegue:

1. Crea una cuenta en [Streamlit Community Cloud](https://share.streamlit.io/)
2. Sube tu código a un repositorio público de GitHub
3. En Streamlit Community Cloud, haz clic en "New app"
4. Selecciona tu repositorio, rama y el archivo principal (`main.py`)
5. Haz clic en "Deploy!"

La aplicación estará disponible en una URL pública con el formato: `https://[tu-nombre-de-usuario]-[nombre-del-repo]-[nombre-del-archivo].streamlit.app`

## Estructura del Proyecto

```
curso_git/
├── main.py                    # Punto de entrada de la aplicación
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Este archivo
└── modulos/                   # Carpeta con los módulos del curso
    ├── intro.py               # Introducción a Git
    ├── commits.py             # Commits y control de versiones
    ├── branches.py            # Ramas y fusiones
    ├── remote.py              # Repositorios remotos
    ├── merge_conflicts.py     # Resolución de conflictos
    ├── github_workflow.py     # Flujo de trabajo en GitHub
    └── evaluacion_final.py    # Evaluación final integradora
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este curso:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

## Licencia

[MIT](LICENSE)
