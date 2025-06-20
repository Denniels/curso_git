#!/bin/bash

# Este script se ejecutará en el entorno de Streamlit Cloud
# para configurar el entorno antes de iniciar la aplicación

# Crear directorio de configuración si no existe
mkdir -p ~/.streamlit

# Copiar archivo de configuración
cp .streamlit/config.toml ~/.streamlit/config.toml

# Mensaje de éxito
echo "✅ Configuración completada correctamente."
