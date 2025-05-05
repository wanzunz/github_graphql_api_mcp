# GitHub GraphQL API MCP

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [Español](README_es.md) | [Français](README_fr.md)

Un outil basé sur MCP (Model Control Protocol) pour interroger et utiliser l'API GraphQL de GitHub. Ce projet fournit un serveur qui vous permet d'explorer le schéma GraphQL de GitHub et d'exécuter des requêtes GraphQL via des outils clients MCP (comme Claude AI).

## Pourquoi utiliser l'API GraphQL de GitHub

L'API GraphQL de GitHub offre des avantages significatifs par rapport aux API REST traditionnelles :

- **Récupération précise des données** : GraphQL permet aux clients de spécifier exactement quels champs ils ont besoin, évitant les données excessives
- **Consommation réduite de tokens** : En ne demandant que les champs nécessaires, la taille de la réponse API est considérablement réduite, diminuant la consommation de tokens du modèle d'IA
- **Une seule requête pour les données liées** : Une requête peut récupérer plusieurs ressources liées, réduisant le nombre de requêtes
- **Auto-documentation** : Grâce à son système de documentation intégré, vous pouvez directement interroger et comprendre le schéma de l'API sans documentation externe
- **Système de typage fort** : Fournit une vérification des types, réduisant les erreurs

Ce projet exploite ces avantages pour fournir des outils qui vous aident à explorer efficacement le schéma de l'API GraphQL de GitHub et à exécuter des requêtes optimisées, offrant aux assistants IA des capacités efficaces de récupération de données GitHub.

## Scénarios d'application

### Fonctions de base

Cet outil implémente facilement les opérations courantes suivantes :

1. **Requête d'informations de base sur le dépôt** : Obtenir le nom du dépôt, la description, le nombre d'étoiles, la liste des branches et d'autres informations de base
2. **Récupération des données des issues** : Interroger les listes d'issues, les détails ou le contenu des commentaires pour des dépôts spécifiques
3. **Accès au profil utilisateur** : Récupérer les profils personnels des utilisateurs, les statistiques de contribution et d'autres informations publiques
4. **Vue du statut des Pull Requests** : Obtenir le statut de base des PR, le contenu des commentaires et les informations de fusion
5. **Requête des dépendances du projet** : Récupérer les listes de paquets de dépendances du projet et les informations de version

### Fonctions avancées exploratoires

Avec les capacités de requête flexibles de GraphQL, vous pouvez également essayer d'implémenter les fonctions d'analyse avancées suivantes :

1. **Analyse des tendances de contribution au dépôt** : Analyser la fréquence de mise à jour du code et la participation des contributeurs en agrégeant les données de commit, évaluant l'activité du projet
2. **Gestion et classification des issues** : Organiser les données des issues selon des conditions personnalisées, découvrir les problèmes qui nécessitent une attention prioritaire et améliorer l'efficacité de la gestion de projet
3. **Analyse des modèles de revue de code** : Analyser les commentaires de PR et les processus de revue, identifier les modèles de problèmes communs et optimiser le flux de travail de revue de code
4. **Visualisation du réseau de contributeurs** : Construire des relations de collaboration entre les contributeurs du projet, découvrir les contributeurs clés et les domaines d'expertise
5. **Évaluation de la santé des dépendances** : Évaluer la fréquence de mise à jour et les problèmes de sécurité potentiels des dépendances du projet, fournissant des suggestions de gestion des dépendances

## Caractéristiques

- Interrogation des types racine du schéma GraphQL de GitHub (Query/Mutation)
- Obtention de documentation détaillée pour des types spécifiques
- Interrogation de la documentation et des paramètres pour des champs spécifiques
- Exécution directe des requêtes de l'API GraphQL de GitHub, récupérant précisément les données nécessaires, réduisant la consommation de tokens
- Support multilingue (anglais/chinois/japonais/espagnol/français)

## Prérequis

- Python 3.10 ou supérieur
- Token d'accès personnel GitHub (pour accéder à l'API GitHub)
- Poetry (outil de gestion de dépendances recommandé)

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/wanzunz/github_graphql_api_mcp.git
cd github_graphql_api_mcp
```

2. Installer les dépendances avec Poetry :

```bash
# Si vous n'avez pas encore installé Poetry, installez-le d'abord :
# curl -sSL https://install.python-poetry.org | python3 -

# Installer les dépendances avec Poetry
poetry install

# Activer l'environnement virtuel
poetry shell
```

Si vous n'utilisez pas Poetry, vous pouvez utiliser la méthode traditionnelle :

```bash
# Créer et activer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
# ou
.venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -e .
```

3. Configurer les variables d'environnement :

Créer un fichier `.env` et ajouter votre token d'accès personnel GitHub :

```
GITHUB_TOKEN="your_github_token_here"
```

Vous pouvez le créer en copiant le fichier `.env.example` :

```bash
cp .env.example .env
```

Puis éditez le fichier `.env`, en remplaçant `your_github_token_here` par votre token GitHub réel.

## Utilisation

### Démarrer le serveur

Assurez-vous d'avoir activé l'environnement virtuel Poetry (`poetry shell`), puis :

#### Exécuter

```bash
python github_graphql_api_mcp_server.py
```

Une fois le serveur démarré, vous pouvez vous y connecter via un client MCP (comme Claude AI).

### Configurer dans Claude Desktop

Vous pouvez configurer ce serveur MCP dans l'application de bureau Claude pour un démarrage en un clic :

1. Ouvrez l'application de bureau Claude
2. Allez dans les paramètres, trouvez la section de configuration du serveur MCP
3. Ajoutez la configuration suivante (modifiez selon votre chemin réel) :

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "<chemin de votre interpréteur Python>",
            "args": [
                "--directory",
                "<chemin du projet>",
                "run",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

Exemple de configuration :

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

Si vous utilisez conda ou d'autres outils de gestion d'environnement :

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

Après la configuration, vous pouvez démarrer le serveur MCP directement depuis l'application de bureau Claude sans avoir à le démarrer manuellement.

### Outils disponibles

Le serveur fournit les outils suivants :

1. **print_type_field** : Interroger les champs des types racine du schéma GraphQL de GitHub
2. **graphql_schema_root_type** : Obtenir la documentation pour les types racine (Query/Mutation)
3. **graphql_schema_type** : Interroger la documentation pour des types spécifiques
4. **call_github_graphql** : Exécuter des requêtes de l'API GraphQL de GitHub

### Exemples d'utilisation

Après vous être connecté au serveur avec un client MCP, vous pouvez :

1. Interroger la documentation du type racine :
   ```
   Utiliser l'outil graphql_schema_root_type, paramètre type_name="QUERY"
   ```

2. Interroger les champs de types spécifiques :
   ```
   Utiliser l'outil print_type_field, paramètres type_name="QUERY", type_fields_name="repository"
   ```

3. Interroger la documentation pour des types spécifiques :
   ```
   Utiliser l'outil graphql_schema_type, paramètre type_name="Repository"
   ```

4. Exécuter des requêtes GraphQL :
   ```
   Utiliser l'outil call_github_graphql, paramètre :
   graphql="""
   query {
     viewer {
       login
       name
     }
   }
   """
   ```

#### Capture d'écran d'exemple

Voici un exemple d'utilisation de GitHub GraphQL API MCP avec Claude :

![Exemple d'utilisation de GitHub GraphQL API MCP](img/github_graphql_usage_example.png)

## Remarques

- Assurez-vous que votre token GitHub a les autorisations appropriées avant utilisation
- Le token est stocké dans le fichier `.env`, qui ne doit pas être commit dans les systèmes de contrôle de version
- Les requêtes doivent respecter les limites d'utilisation de l'API GitHub

## Licence

Ce projet est sous licence MIT - une licence très permissive qui permet aux utilisateurs d'utiliser, modifier, distribuer et commercialiser librement ce logiciel, à condition qu'ils conservent l'avis de copyright et la déclaration de licence.

Voir la [Licence MIT](https://opensource.org/licenses/MIT) pour les termes détaillés. 