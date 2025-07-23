# 🧑‍🍳 Toque et Chef 🍱🍻

## 🔍️ Description de l'application
Toque et Chef est une application de recettes de cuisine moderne et intuitive, conçue pour tous les passionnés de gastronomie, du débutant au chef confirmé. Explorez des centaines de recettes variées, classées par ingrédients, types de plats, niveaux de difficulté et plus encore.

Mais ce qui rend Toque et Chef unique, c’est son chatbot intelligent intégré :
Posez simplement une question en langage naturel — comme "Je cherche une recette végétarienne avec des courgettes" ou "Que faire avec du poulet et du riz ?", et l’assistant vous propose instantanément des recettes pertinentes issues de la base de données interne.

## 🧐 Fonctionnalités
- Identification robuste de l'utilisateur (inscription, connexion, déconnexion) ;
- Gestion des droits avec des rôles différenciés (profils 'Administrateur' et 'Utilisateur)';
- CRUD complet (CREATE, READ, UPDATE, DELETE) avec les recettes de cuisine ;
- Possibilité de commenter les recettes de cuisine (CREATE, READ, DELETE) ;
- Interface responsive de l'application ;
- Chatbot permettant de suggérer des recettes de cuisine en fonction des questions posées par l'utilisateur. 

## 🔧 Technologies utilisées
- Scrapy : Collecte (scraping) de données de recettes de cuisine ;
- LangChain : Développement du RAG ;
- Django : Développement de l'application front-end et back-end ;
- Tailwind CSS avec Daisy UI : Développement front-end ;
- PostgreSQL : Base de données relationnelle ;
- Groq : LLM pour le RAG.

## 👽️ Système RAG
- Formulation d'une question sur les recettes de cuisine par l'utilisateur à l'assistant IA,
- L'assistant IA interprète la question,
- L'assistant IA cherche 3 recettes de cuisine en rapport à la question,
- L'assistant IA conçoit une réponse et la renvoit à l'utilisateur.

## 🌐 Endpoints

|   Endpoint                 |   Utilisateur requis   |   Description                             |
| -------------------------: | :--------------------: | :---------------------------------------: |
| `/`                        |   non                  | Page d'accueil (homepage)                 |
| `register/`                |   non                  | Page d'inscription                        |
| `login/`                   |   non                  | Page de connexion                         |
| `logout/`                  |   oui                  | Page de déconnexion                       |
| `users/`                   |   oui                  | Mise à jour du profil utilisateur         |
| `recipes/`                 |   non                  | Liste des recettes                        |
| `recipes/<int:id>`         |   non                  | Détail d'une recette                      |
| `recipes/create/`          |   oui                  | Créer une recette                         |
| `recipes/update/<int:id/`  |   oui                  | Page de connexion                         |
| `recipes/delete/`          |   oui                  | Supprimer une recette                     |
| `recipes/my-recipes/`      |   oui                  | Liste des recettes de l'utilisateur       |
| `comments/create/<int:id/` |   oui                  | Ajouter un commentaire à une recette      |
| `comments/delete/<int:id>/`|   oui                  | Supprimer un commentaire de l'utilisateur |
| `comments/my_comments/`    |   oui                  | Liste des commentaires de l'utilisateur   |
| `api/chabot/`              |   non                  | Interaction avec l'API de Groq            |

## 🏗️ Architecture

8

## 🚀 Lancement du projet

#### Pré-requis


#### Scraping des données


#### Création de la base de données PostgreSQL


#### Démarrage de l'application




