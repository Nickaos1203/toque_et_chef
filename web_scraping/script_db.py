# Connexion à la base de données postgresql
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# Vérification du chargement des variables secrètes
for var in ['db_name', 'db_user', 'db_password', 'db_port']:
    val = os.getenv(var)
    print(f"{var} → {repr(val)}")



def add_recipes(title, image_url, season, category, duration, level, cost, number, persons_number, ingredients, steps):
    # Connexion with 'toque_et_chef' database
    conn = psycopg2.connect(
        database=os.getenv("db_name"),
        user=os.getenv("db_user"),
        host='localhost',
        password=os.getenv("db_password"),
        port=os.getenv("db_port")
    )
    cur = conn.cursor()

    request = """
        INSERT INTO recipes_recipe (
            title, image_url, season, category, duration, level, cost, number, persons_number, ingredients, steps
            )
        VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            );
        """

    cur.execute(request, (title, image_url, season, category, duration, level, cost, number, persons_number, ingredients, steps))
    conn.commit()
    cur.close()
    conn.close()