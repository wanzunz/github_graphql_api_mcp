# GitHub GraphQL API MCP

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [Español](README_es.md) | [Français](README_fr.md)

Un outil basé sur MCP (Model Context Protocol) pour interroger et utiliser l'API GraphQL de GitHub. Ce projet fournit un serveur qui vous permet d'explorer le schéma GraphQL de GitHub et d'exécuter des requêtes GraphQL via des outils clients MCP (comme Claude AI).

## Table des Matières

- [Pourquoi utiliser l'API GraphQL de GitHub](#pourquoi-utiliser-lapi-graphql-de-github)
- [Scénarios d'application](#scénarios-dapplication)
- [Caractéristiques](#caractéristiques)
- [Comparaison avec le serveur MCP officiel GitHub](#comparaison-avec-le-serveur-mcp-officiel-github)
- [Prérequis](#prérequis)
- [Installation et Utilisation](#installation-et-utilisation)
- [Configurer dans Claude Desktop](#configurer-dans-claude-desktop)
- [Outils disponibles](#outils-disponibles)
- [Exemples d'utilisation](#exemples-dutilisation)
- [Remarques](#remarques)
- [Licence](#licence)

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

## Comparaison avec le serveur MCP officiel GitHub

Comparé au [github-mcp-server](https://github.com/github/github-mcp-server) officiel, ce projet offre des avantages distincts dans des scénarios spécifiques :

| Fonctionnalité | GitHub GraphQL API MCP | Serveur MCP officiel GitHub |
|----------------|------------------------|-----------------------------|
| **Mécanisme Principal** | Requête GraphQL unique | Plusieurs API REST / Outils granulaires |
| **Récupération de Données** | **En une fois** : Récupère les détails du dépôt, les issues, les PR, l'historique et les versions en une seule requête | **Étapes multiples** : Nécessite d'enchaîner `search_repositories`, `get_file_contents`, `list_commits`, etc. |
| **Efficacité** | Élevée. Minimise la latence réseau et les allers-retours. | Plus faible pour la collecte de données complexes. Latence élevée due aux appels d'outils séquentiels. |
| **Utilisation de Tokens** | **Optimisée**. Ne renvoie que les champs demandés. | **Plus élevée**. Les sorties des outils intermédiaires (réponses JSON complètes) consomment la fenêtre contextuelle. |
| **Flexibilité** | **Élevée**. Le client définit la structure exacte des données nécessaires. | **Fixe**. Le client doit travailler avec des structures de réponse API prédéfinies. |
| **Couverture API** | **Complète**. Accès à tout champ exposé par l'API GraphQL de GitHub. | **Partielle**. Limitée aux points de terminaison REST spécifiques codés en dur par les mainteneurs. |
| **Introspection** | **Intégrée**. L'IA peut interroger le schéma pour découvrir dynamiquement de nouveaux champs d'API. | **Aucune**. L'IA dépend de ses données d'entraînement ; ne peut pas découvrir de nouvelles fonctionnalités d'API sans mises à jour de l'outil. |
| **Maintenabilité** | **Mises à jour sans code**. Nécessite souvent simplement une mise à jour du fichier de schéma pour prendre en charge les nouvelles fonctionnalités GitHub. | **Code lourd**. Nécessite l'écriture de nouveaux gestionnaires Go et définitions de structures pour chaque nouvelle fonctionnalité. |
| **Complexité** | Nécessite que le LLM écrive du GraphQL (soutenu par des outils d'introspection de schéma). | Plus facile pour les LLM qui préfèrent les appels de fonctions simples, mais plus difficile de gérer l'état entre les appels. |

**Exemple** : Pour obtenir les "dernières mises à jour importantes d'un projet", cet outil peut récupérer les versions, les commits récents et les issues ouvertes **en une seule fois**, alors que le serveur officiel pourrait nécessiter plus de 5 appels d'outils séparés et allers-retours.

### Pourquoi cela compte pour les agents IA

1.  **Efficacité de la Fenêtre Contextuelle** : Les outils officiels renvoient souvent des objets JSON massifs (par exemple, un objet dépôt complet pourrait dépasser 5 Ko). Avec GraphQL, vous ne récupérez que le `name` et la `description`, économisant 99% des tokens. C'est crucial pour les longues conversations et les tâches complexes.
2.  **Raisonnement Complexe** : Les agents IA ont souvent besoin de traverser des relations (par exemple, "Trouver l'auteur de la PR qui a fermé cette Issue"). Dans les outils REST/Officiels, c'est un processus en plusieurs étapes "Rechercher -> Obtenir ID -> Obtenir PR -> Obtenir Auteur". Dans GraphQL, c'est une seule requête imbriquée, permettant à l'IA de se concentrer sur le raisonnement logique plutôt que sur la plomberie des données.
3.  **Adaptabilité Future** : Lorsque GitHub ajoute une nouvelle fonctionnalité (par exemple, un nouveau champ sur les Discussions), ce serveur MCP peut la prendre en charge immédiatement via l'introspection de schéma, tandis que le serveur officiel attend une mise à jour du code.

## Prérequis

- Python 3.10 ou supérieur
- Token d'accès personnel GitHub (pour accéder à l'API GitHub)
- Poetry (outil de gestion de dépendances recommandé)

## Installation et Utilisation

Nous recommandons d'utiliser [uv](https://github.com/astral-sh/uv) pour la gestion, qui est actuellement l'outil de gestion de projet Python le plus rapide et le plus simple. Alternativement, vous pouvez utiliser pip standard.

### Méthode 1 : Utilisation de uv (Recommandé, Le plus rapide)

Avec uv, vous n'avez pas besoin de créer manuellement des environnements virtuels ou d'installer des dépendances ; il gère tout pour vous automatiquement.

1.  **Installer uv** (Passer si déjà installé) :
    ```bash
    # MacOS / Linux
    curl -lsSf https://astral.sh/uv/install.sh | sh

    # Windows
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

2.  **Configurer les variables d'environnement** :
    Copiez `.env.example` vers `.env` et remplissez votre Token GitHub :
    ```bash
    cp .env.example .env
    # Éditez le fichier .env et remplissez votre token
    ```

3.  **Exécution en un clic** :
    ```bash
    uv run github_graphql_api_mcp_server.py
    ```
    *uv créera automatiquement un environnement virtuel, téléchargera et installera toutes les dépendances, puis démarrera le serveur.*

### Méthode 2 : Pip standard

Si vous préférez ne pas installer d'outils supplémentaires, vous pouvez utiliser la méthode Python traditionnelle :

1.  **Créer et Activer l'Environnement Virtuel** :
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    ```

2.  **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configurer les variables d'environnement** :
    Créez et configurez le fichier `.env` comme indiqué ci-dessus.

4.  **Exécuter** :
    ```bash
    python github_graphql_api_mcp_server.py
    ```

## Configurer dans Claude Desktop

Vous pouvez configurer ce serveur MCP dans l'application de bureau Claude pour un démarrage en un clic :

1. Ouvrez l'application de bureau Claude
2. Allez dans les paramètres, trouvez la section de configuration du serveur MCP
3. Ajoutez la configuration suivante (modifiez selon votre chemin réel) :

```json
{
    "mcpServers": {
        "github_mcp": {
            "command": "/path/to/uv",
            "args": [
                "run",
                "--directory",
                "<chemin du projet>",
                "github_graphql_api_mcp_server.py"
            ]
        }
    }
}
```

Exemple de configuration (utilisation de uv) :

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

Si vous utilisez Python standard (Méthode 2) :

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