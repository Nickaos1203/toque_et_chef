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
- Python et JavaScript pour le code ;
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
```
toque_et_chef/
        |--.venv
        |--django_app/
                |--comments/
                        |--templates/
                                |--comments/
                                        |--comment_create.html
                                        |--comment_delete.html
                                        |--comments_list.html
                                        |--my_comments
                        |--__init__.py
                        |--admin.py
                        |--app.py
                        |--forms.py
                        |--models.py
                        |--tests.py
                        |--urls.py
                        |--views.py                       
                |--django_app/
                        |--__init__.py
                        |--asgi.py
                        |--settings.py
                        |--urls.py
                        |--wsgi.py
                |--recipes/
                        |--management/
                                |--commands/
                                        |--__init__.py
                                        |--refresh_rag.py
                                |--__init__.py
                        |--templates/
                                |--recipes/
                                        |--home.html
                                        |--my_recipes.html
                                        |--recipe_create.html
                                        |--recipe_delete.html
                                        |--recipe_update.html
                                        |--recipes_detail.html
                                        |--recipes_list.html
                        |--__init__.py
                        |--admin.py
                        |--app.py
                        |--forms.py
                        |--models.py
                        |--rag_system.py
                        |--tests.py
                        |--urls.py
                        |--views.py
                |--theme/
                |--users/
                        |--templates/
                                |--users/
                                        |--login.html
                                        |--profile.html
                                        |--register.html
                        |--__init__.py
                        |--admin.py
                        |--app.py
                        |--forms.py
                        |--models.py
                        |--tests.py
                        |--urls.py
                        |--views.py
                |--manage.py
        |--web_scraping/
                |--web_scraping/
                        |--spiders
                                |--__init__.py
                                |--appetizer_spider.py
                                |--dessert_spider.py
                                |--dishes_appetizer.py
                        |--__init__.py
                        |--items.py
                        |--middlewares.py
                        |--pipelines.py
                        |--settings.py
                |--__init__.py
                |--fusion_filrs.py
                |--scrapy.cfg
                |--script_db.py
        |--.env
        |--.gitignore
        |--README.md
        |--requirements.txt





```



## 🚀 Lancement du projet

#### Pré-requis
- Assurez-vous d'avoir installer python
- Assurez-vous d'être  Windows
- Assurez-vous d'avoir installer node et npm
- Assurez-vous d'utiliser la version 17 de PostgreSQL

#### Initialisation du projet
```bash
git clone https://github.com/Nickaos1203/toque_et_chef.git
cd toque_et_chef
```

#### Création et activation de l'environnement virtuel
```bash
python -m venv .venv
source .venv/Scripts/activate
```

#### Installation des dépendances
```bash
pip install -r requirements.txt
```

#### Création du fichier .env
- Créer le fichier .env
```bash
touch .env
```
- Ajouter le scripts suivant suivantes au fichier .env :
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME={le nom de votre base de données PostgreSQL}
DB_USER={votre nom d'utilisateur PostgreSQL}
DB_PASSWORD={votre mot de passe PostgreSQL}
DB_HOST=localhost
DB_PORT=5433
SECRET_KEY={votre clé secrète}
NPM_PATH={chemin vers npm}
API_KEY_GROQ={clé secrète de l'api de Groq}
```
- Note : Lancer cette commande pour trouver le chemin vers npm:
```bash
which npm
```

#### Création de la base de données
```bash
cd django_app
python manage.py makemigrations
python manage.py migrate
```
#### Lancer Tailwind
```bash
python manage.py tailwind install
python manage.py tailwind start
```

#### Lancer Django
```bash
python manage.py runserver
```

#### Création et insertion des données de recettes de cuisine (optionnel)
- Entrer dans le dossier web_scraping :
```bash
cd ../../webscraping
```
- Lancer le scraping des données :
```bash
scrapy crawl appetize_spider -o appetizer_dataset.json
scrapy crawl dishes_spider -o dishe_dataset.json
scrapy crawl dessert_spider -o dessert_dataset.json
```
- Fusionner les fichiers json :
```bash
python fusion_files.py
```
- Injection dans la base de données :
```bash
python script_db.py
```
