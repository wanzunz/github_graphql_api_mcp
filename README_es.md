# GitHub GraphQL API MCP

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [Español](README_es.md) | [Français](README_fr.md)

Una herramienta basada en MCP (Model Control Protocol) para consultar y utilizar la API GraphQL de GitHub. Este proyecto proporciona un servidor que te permite explorar el esquema GraphQL de GitHub y ejecutar consultas GraphQL a través de herramientas cliente MCP (como Claude AI).

## Por qué usar la API GraphQL de GitHub

La API GraphQL de GitHub ofrece ventajas significativas sobre las API REST tradicionales:

- **Recuperación precisa de datos**: GraphQL permite a los clientes especificar exactamente qué campos necesitan, evitando datos excesivos
- **Consumo reducido de tokens**: Al solicitar solo los campos necesarios, el tamaño de respuesta de la API se reduce significativamente, disminuyendo el consumo de tokens del modelo de IA
- **Una sola solicitud para datos relacionados**: Una consulta puede recuperar múltiples recursos relacionados, reduciendo el número de solicitudes
- **Auto-documentación**: A través de su sistema de documentación integrado, puedes consultar y entender directamente el esquema de la API sin documentación externa
- **Sistema de tipos fuerte**: Proporciona verificación de tipos, reduciendo errores

Este proyecto aprovecha estas ventajas para proporcionar herramientas que te ayudan a explorar efectivamente el esquema de la API GraphQL de GitHub y ejecutar consultas optimizadas, proporcionando a los asistentes de IA capacidades eficientes de recuperación de datos de GitHub.

## Escenarios de aplicación

### Funciones básicas

Esta herramienta implementa fácilmente las siguientes operaciones comunes:

1. **Consulta de información básica del repositorio**: Obtener nombre del repositorio, descripción, conteo de estrellas, lista de ramas y otra información básica
2. **Recuperación de datos de issues**: Consultar listas de issues, detalles o contenido de comentarios para repositorios específicos
3. **Acceso a perfiles de usuario**: Recuperar perfiles personales de usuarios, estadísticas de contribución y otra información pública
4. **Vista de estado de Pull Request**: Obtener estado básico de PR, contenido de comentarios e información de fusión
5. **Consulta de dependencias del proyecto**: Recuperar listas de paquetes de dependencias del proyecto e información de versiones

### Funciones avanzadas exploratorias

Con las capacidades flexibles de consulta de GraphQL, también puedes intentar implementar las siguientes funciones de análisis avanzado:

1. **Análisis de tendencias de contribución del repositorio**: Analizar la frecuencia de actualización de código y la participación de contribuyentes agregando datos de commits, evaluando la actividad del proyecto
2. **Gestión y clasificación de issues**: Organizar datos de issues según condiciones personalizadas, descubrir problemas que necesitan atención prioritaria y mejorar la eficiencia de gestión de proyectos
3. **Análisis de patrones de revisión de código**: Analizar comentarios de PR y procesos de revisión, identificar patrones comunes de problemas y optimizar el flujo de trabajo de revisión de código
4. **Visualización de la red de contribuyentes**: Construir relaciones de colaboración entre contribuyentes del proyecto, descubrir contribuyentes clave y áreas de experiencia
5. **Evaluación de salud de dependencias**: Evaluar la frecuencia de actualización y posibles problemas de seguridad de las dependencias del proyecto, proporcionando sugerencias de gestión de dependencias

## Características

- Consulta de tipos raíz del esquema GraphQL de GitHub (Query/Mutation)
- Obtención de documentación detallada para tipos específicos
- Consulta de documentación y parámetros para campos específicos
- Ejecución directa de consultas de la API GraphQL de GitHub, recuperando con precisión los datos necesarios, reduciendo el consumo de tokens
- Soporte multilingüe (inglés/chino/japonés/español/francés)

## Requisitos previos

- Python 3.10 o superior
- Token de acceso personal de GitHub (para acceder a la API de GitHub)
- Poetry (herramienta de gestión de dependencias recomendada)

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/wanzunz/github_graphql_api_mcp.git
cd github_graphql_api_mcp
```

2. Instalar dependencias usando Poetry:

```bash
# Si aún no has instalado Poetry, instálalo primero:
# curl -sSL https://install.python-poetry.org | python3 -

# Instalar dependencias usando Poetry
poetry install

# Activar el entorno virtual
poetry shell
```

Si no usas Poetry, puedes usar el método tradicional:

```bash
# Crear y activar un entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
# o
.venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -e .
```

3. Configurar variables de entorno:

Crear un archivo `.env` y añadir tu token de acceso personal de GitHub:

```
GITHUB_TOKEN="your_github_token_here"
```

Puedes crearlo copiando el archivo `.env.example`:

```bash
cp .env.example .env
```

Luego edita el archivo `.env`, reemplazando `your_github_token_here` con tu token de GitHub real.

## Uso

### Iniciar el servidor

Asegúrate de haber activado el entorno virtual de Poetry (`poetry shell`), luego:

#### Ejecutar

```bash
python github_graphql_api_mcp_server.py
```

Después de iniciar el servidor, puedes conectarte a él a través de un cliente MCP (como Claude AI).

### Configurar en Claude Desktop

Puedes configurar este servidor MCP en la aplicación de escritorio Claude para inicio con un clic:

1. Abre la aplicación de escritorio Claude
2. Ve a configuración, encuentra la sección de configuración del servidor MCP
3. Añade la siguiente configuración (modifica según tu ruta real):

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "<ruta de tu intérprete de Python>",
            "args": [
                "--directory",
                "<ruta del proyecto>",
                "run",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

Ejemplo de configuración:

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/usr/bin/python3",
            "args": [
                "--directory",
                "/home/user/projects/github_graphql_api_mcp/",
                "run",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

Si usas conda u otras herramientas de gestión de entorno:

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/opt/miniconda3/bin/python",
            "args": [
                "--directory",
                "/Users/username/github/github_graphql_api_mcp/",
                "run",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

Después de la configuración, puedes iniciar el servidor MCP directamente desde la aplicación de escritorio Claude sin tener que iniciarlo manualmente.

### Herramientas disponibles

El servidor proporciona las siguientes herramientas:

1. **print_type_field**: Consultar campos de tipos raíz del esquema GraphQL de GitHub
2. **graphql_schema_root_type**: Obtener documentación para tipos raíz (Query/Mutation)
3. **graphql_schema_type**: Consultar documentación para tipos específicos
4. **call_github_graphql**: Ejecutar consultas de la API GraphQL de GitHub

### Ejemplos de uso

Después de conectarte al servidor con un cliente MCP, puedes:

1. Consultar documentación de tipo raíz:
   ```
   Usar la herramienta graphql_schema_root_type, parámetro type_name="QUERY"
   ```

2. Consultar campos de tipos específicos:
   ```
   Usar la herramienta print_type_field, parámetros type_name="QUERY", type_fields_name="repository"
   ```

3. Consultar documentación para tipos específicos:
   ```
   Usar la herramienta graphql_schema_type, parámetro type_name="Repository"
   ```

4. Ejecutar consultas GraphQL:
   ```
   Usar la herramienta call_github_graphql, parámetro:
   graphql="""
   query {
     viewer {
       login
       name
     }
   }
   """
   ```

## Notas

- Asegúrate de que tu token de GitHub tenga los permisos apropiados antes de usar
- El token se almacena en el archivo `.env`, que no debe ser comprometido en sistemas de control de versiones
- Las consultas deben cumplir con los límites de uso de la API de GitHub

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - una licencia muy permisiva que permite a los usuarios usar, modificar, distribuir y comercializar libremente este software, siempre que mantengan el aviso de copyright y declaración de licencia.

Consulta la [Licencia MIT](https://opensource.org/licenses/MIT) para términos detallados. 