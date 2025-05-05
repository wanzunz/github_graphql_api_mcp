from mcp.server.fastmcp import FastMCP
from graphql import build_schema, OperationType
from graphql.utilities import print_schema, print_value, print_introspection_schema, print_type  
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create an MCP server
mcp = FastMCP("github_graphql_api_mcp_server")

with open('schema.docs.graphql', 'r', encoding='utf-8') as f:
    schema_content = f.read()

schema = build_schema(schema_content)
text = print_schema(schema)

query_type = schema.query_type


@mcp.tool()
def print_type_field(type_name: str, type_fields_name: str):
    """A tool to query GitHub GraphQL schema root type fields. You need to provide root_type_name and type_fields_name
Args:
type_name: root type like `QUERY` or `MUTATION`
type_fields_name: field name like `repository` based on root type documentation
Returns:
str: Documentation content for the specified field
"""
    object_type = schema.get_root_type(OperationType[type_name])
    if hasattr(object_type, "fields"):
        type_name_field = object_type.fields[type_fields_name]
        return print_type_field_docs(type_fields_name, type_name_field)
    else:
        print("No fields attribute")


def print_type_field_docs(name, field):
    doc_str = f"# {name}\n"
    if hasattr(field, 'description') and field.description:
        doc_str += f"{field.description}\n"
    else:
        doc_str += "No description provided."
    doc_str += "## Parameters \n"
    for arg_name, arg in field.args.items():
        doc_str += f"### `{arg_name}: {arg.type}`\n{arg.description}\n"

    doc_str += "## Return Type \n"
    # doc_str += f"### `{str(field.type)}`\n{field.type.of_type.description}\n"
    doc_str += f"### `{str(field.type)}`\n"
    return doc_str

@mcp.tool()
def graphql_schema_root_type(type_name: str):
    """A tool to query GitHub GraphQL schema root types. You need to provide the root type name (QUERY/MUTATION)
Args:
    type_name: root type (QUERY or MUTATION)
Returns:
    str: Documentation content
"""
    graphql_type = schema.get_root_type(OperationType[type_name])
    doc_str = (f"# Type Name: {graphql_type.name}\n")
    if hasattr(graphql_type, 'description') and graphql_type.description:
        doc_str += (f"Description: {graphql_type.description}\n")
    else:
        doc_str += ("No description provided.\n")

    if hasattr(graphql_type, 'fields'):
        doc_str += ("## Fields:\n")
        for field_name, field in graphql_type.fields.items():
            field_description = getattr(field, 'description', "No description\n\n")
            doc_str += (f"### {field_name} \n ```markdown\n{field_description}\n```\n ")
    return doc_str


@mcp.tool()
def graphql_schema_type(type_name: str):
    """A tool to query specific type documentation in GitHub GraphQL schema. You need to provide the type_name
Args:
    type_name: Type name like `SecurityAdvisoryConnection`
Returns:
    str: Documentation content
"""
    type_1 = schema.get_type(type_name)
    return print_type(type_1)


GITHUB_API_URL = "https://api.github.com/graphql"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

@mcp.tool()
def call_github_graphql(graphql: str) -> str:
    """A tool to execute GitHub GraphQL API queries. Before using, it's recommended to check the documentation first, and include ID fields in your queries for easier follow-up operations
    Args:
        graphql: The GraphQL query
    Returns:
        str: Execution result
    """
    try:
        # Set request headers including authorization
        headers = {
            "Content-Type": "application/json"
        }
        if GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
        # Send POST request
        response = requests.post(GITHUB_API_URL, headers=headers, json={'query': graphql})

        # Check response status
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"request failed: {response.status_code} - {response.text}")
    except Exception as e:
        return f'{e}.'

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run()