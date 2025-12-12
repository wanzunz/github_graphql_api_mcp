# GitHub GraphQL API MCP

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [Español](README_es.md) | [Français](README_fr.md)

Una herramienta basada en MCP (Model Context Protocol) para consultar y utilizar la API GraphQL de GitHub. Este proyecto proporciona un servidor que te permite explorar el esquema GraphQL de GitHub y ejecutar consultas GraphQL a través de herramientas cliente MCP (como Claude AI).

## Tabla de Contenidos

- [Por qué usar la API GraphQL de GitHub](#por-qué-usar-la-api-graphql-de-github)
- [Escenarios de aplicación](#escenarios-de-aplicación)
- [Características](#características)
- [Comparación con el Servidor MCP oficial de GitHub](#comparación-con-el-servidor-mcp-oficial-de-github)
- [Requisitos previos](#requisitos-previos)
- [Instalación y Uso](#instalación-y-uso)
- [Configurar en Claude Desktop](#configurar-en-claude-desktop)
- [Herramientas disponibles](#herramientas-disponibles)
- [Ejemplos de uso](#ejemplos-de-uso)
- [Notas](#notas)
- [Licencia](#licencia)

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

## Comparación con el Servidor MCP oficial de GitHub

En comparación con el [github-mcp-server](https://github.com/github/github-mcp-server) oficial, este proyecto ofrece ventajas distintivas en escenarios específicos:

| Característica | GitHub GraphQL API MCP | Servidor MCP oficial de GitHub |
|----------------|------------------------|--------------------------------|
| **Mecanismo Central** | Consulta GraphQL única | Múltiples API REST / Herramientas granulares |
| **Recuperación de Datos** | **Una sola vez**: Obtiene detalles del repositorio, issues, PRs, historial y lanzamientos en una sola solicitud | **Pasos múltiples**: Requiere encadenar `search_repositories`, `get_file_contents`, `list_commits`, etc. |
| **Eficiencia** | Alta. Minimiza la latencia de red y los viajes de ida y vuelta. | Menor para la recopilación de datos complejos. Alta latencia debido a llamadas secuenciales a herramientas. |
| **Uso de Tokens** | **Optimizado**. Devuelve solo los campos solicitados. | **Mayor**. Las salidas de herramientas intermedias (respuestas JSON completas) consumen la ventana de contexto. |
| **Flexibilidad** | **Alta**. El cliente define la estructura exacta de datos necesaria. | **Fija**. El cliente debe trabajar con estructuras de respuesta de API predefinidas. |
| **Cobertura de API** | **Completa**. Acceso a cualquier campo expuesto por la API GraphQL de GitHub. | **Parcial**. Limitado a los endpoints REST específicos codificados por los mantenedores. |
| **Introspección** | **Integrada**. La IA puede consultar el esquema para aprender dinámicamente sobre nuevos campos de la API. | **Ninguna**. La IA depende de sus datos de entrenamiento; no puede descubrir nuevas características de la API sin actualizaciones de la herramienta. |
| **Mantenibilidad** | **Actualizaciones sin código**. A menudo solo requiere una actualización del archivo de esquema para soportar nuevas características de GitHub. | **Código pesado**. Requiere escribir nuevos manejadores en Go y definiciones de estructuras para cada nueva característica. |
| **Complejidad** | Requiere que el LLM escriba GraphQL (apoyado por herramientas de introspección de esquema). | Más fácil para LLMs que prefieren llamadas a funciones simples, pero más difícil de gestionar el estado entre llamadas. |

**Ejemplo**: Para obtener las "últimas actualizaciones importantes de un proyecto", esta herramienta puede obtener lanzamientos, commits recientes e issues abiertos de **una sola vez**, mientras que el servidor oficial podría requerir más de 5 llamadas a herramientas separadas y viajes de ida y vuelta.

### Por qué esto importa para los Agentes de IA

1.  **Eficiencia de la Ventana de Contexto**: Las herramientas oficiales a menudo devuelven objetos JSON masivos (por ejemplo, un objeto de repositorio completo podría ser de más de 5KB). Con GraphQL, obtienes solo el `name` y `description`, ahorrando el 99% de los tokens. Esto es crucial para conversaciones largas y tareas complejas.
2.  **Razonamiento Complejo**: Los agentes de IA a menudo necesitan atravesar relaciones (por ejemplo, "Encontrar el autor del PR que cerró este Issue"). En herramientas REST/Oficiales, este es un proceso de varios pasos "Buscar -> Obtener ID -> Obtener PR -> Obtener Autor". En GraphQL, es una sola consulta anidada, permitiendo que la IA se centre en el razonamiento lógico en lugar de la fontanería de datos.
3.  **Adaptabilidad Futura**: Cuando GitHub añade una nueva característica (por ejemplo, un nuevo campo en Discussions), este servidor MCP puede soportarlo inmediatamente a través de la introspección del esquema, mientras que el servidor oficial espera una actualización de código.

## Requisitos previos

- Python 3.10 o superior
- Token de acceso personal de GitHub (para acceder a la API de GitHub)
- Poetry (herramienta de gestión de dependencias recomendada)

## Instalación y Uso

Recomendamos usar [uv](https://github.com/astral-sh/uv) para la gestión, que es actualmente la herramienta de gestión de proyectos Python más rápida y sencilla. Alternativamente, puedes usar pip estándar.

### Método 1: Usando uv (Recomendado, Más rápido)

Con uv, no necesitas crear manualmente entornos virtuales ni instalar dependencias; maneja todo por ti automáticamente.

1.  **Instalar uv** (Saltar si ya está instalado):
    ```bash
    # MacOS / Linux
    curl -lsSf https://astral.sh/uv/install.sh | sh

    # Windows
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

2.  **Configurar Variables de Entorno**:
    Copia `.env.example` a `.env` y rellena tu Token de GitHub:
    ```bash
    cp .env.example .env
    # Edita el archivo .env y rellena tu token
    ```

3.  **Ejecución con un clic**:
    ```bash
    uv run github_graphql_api_mcp_server.py
    ```
    *uv creará automáticamente un entorno virtual, descargará e instalará todas las dependencias, y luego iniciará el servidor.*

### Método 2: Pip estándar

Si prefieres no instalar herramientas adicionales, puedes usar el método tradicional de Python:

1.  **Crear y Activar Entorno Virtual**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    ```

2.  **Instalar Dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configurar Variables de Entorno**:
    Crea y configura el archivo `.env` como se indicó anteriormente.

4.  **Ejecutar**:
    ```bash
    python github_graphql_api_mcp_server.py
    ```

## Configurar en Claude Desktop

Puedes configurar este servidor MCP en la aplicación de escritorio Claude para inicio con un clic:

1. Abre la aplicación de escritorio Claude
2. Ve a configuración, encuentra la sección de configuración del servidor MCP
3. Añade la siguiente configuración (modifica según tu ruta real):

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/path/to/uv",
            "args": [
                "run",
                "--directory",
                "<ruta del proyecto>",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

Ejemplo de configuración (usando uv):

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/Users/username/.cargo/bin/uv",
            "args": [
                "run",
                "--directory",
                "/Users/username/github/github_graphql_api_mcp/",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

Si usas Python estándar (Método 2):

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/path/to/project/.venv/bin/python",
            "args": [
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

#### Captura de pantalla de ejemplo

A continuación se muestra un ejemplo de uso de GitHub GraphQL API MCP con Claude:

![Ejemplo de uso de GitHub GraphQL API MCP](img/github_graphql_usage_example.png)

## Notas

- Asegúrate de que tu token de GitHub tenga los permisos apropiados antes de usar
- El token se almacena en el archivo `.env`, que no debe ser comprometido en sistemas de control de versiones
- Las consultas deben cumplir con los límites de uso de la API de GitHub

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - una licencia muy permisiva que permite a los usuarios usar, modificar, distribuir y comercializar libremente este software, siempre que mantengan el aviso de copyright y declaración de licencia.

Consulta la [Licencia MIT](https://opensource.org/licenses/MIT) para términos detallados. 