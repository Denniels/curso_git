# Guía de Despliegue en Streamlit Community Cloud

Este documento proporciona instrucciones detalladas para desplegar tu aplicación "Curso Interactivo de Git y GitHub" en Streamlit Community Cloud.

## Requisitos Previos

1. Una cuenta en [GitHub](https://github.com/)
2. Una cuenta en [Streamlit Community Cloud](https://streamlit.io/cloud)

## Pasos para el Despliegue

### 1. Preparar tu Repositorio en GitHub

1. Crea un nuevo repositorio público en GitHub (o usa uno existente)
2. Sube tu código al repositorio:

```bash
# Inicializa Git si aún no lo has hecho
git init

# Añade el repositorio remoto
git remote add origin https://github.com/tu-usuario/nombre-del-repo.git

# Añade todos los archivos
git add .

# Commit inicial
git commit -m "Versión inicial del Curso de Git y GitHub"

# Sube el código a GitHub
git push -u origin main
```

### 2. Desplegar en Streamlit Community Cloud

1. Ve a [Streamlit Community Cloud](https://share.streamlit.io/)
2. Inicia sesión con tu cuenta de GitHub
3. Haz clic en "New app"
4. En la sección "Repository", selecciona tu repositorio
5. En "Branch", selecciona la rama principal (normalmente `main`)
6. En "Main file path", introduce `main.py`
7. Opcionalmente, puedes configurar recursos avanzados como Python version y packages
8. Haz clic en "Deploy!"

### 3. Verificar el Despliegue

Una vez completado el despliegue:

1. La aplicación estará disponible en una URL con el formato:
   `https://[tu-nombre-de-usuario]-[nombre-del-repo]-main-[random-string].streamlit.app`

2. Verifica que todos los módulos funcionan correctamente:
   - Navegación entre módulos
   - Visualización de contenido
   - Funcionamiento de los quizzes
   - Interactividad de los simuladores

### 4. Compartir tu Aplicación

Una vez que la aplicación esté desplegada correctamente, puedes:

1. Compartir la URL con tus usuarios
2. Añadir la URL a tu perfil de GitHub o LinkedIn
3. Incluir la URL en tu CV o portafolio

## Solución de Problemas

Si encuentras problemas durante el despliegue:

1. **Errores de Dependencias**: Verifica que todas las dependencias estén correctamente listadas en `requirements.txt`
2. **Errores de Importación**: Asegúrate de que las rutas de importación sean relativas y correctas
3. **Errores de Archivos**: Verifica que todos los archivos necesarios estén incluidos en el repositorio
4. **Logs de Error**: Revisa los logs de la aplicación en Streamlit Community Cloud para identificar problemas específicos

## Actualizaciones Futuras

Para actualizar tu aplicación desplegada:

1. Realiza cambios en tu código local
2. Haz commit y push a GitHub:
   ```bash
   git add .
   git commit -m "Descripción de los cambios"
   git push
   ```
3. Streamlit Community Cloud detectará automáticamente los cambios y redesplegará la aplicación

## Recursos Adicionales

- [Documentación de Streamlit](https://docs.streamlit.io/)
- [Mejores prácticas para despliegue en Streamlit](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app)
- [Foro de la comunidad de Streamlit](https://discuss.streamlit.io/)
