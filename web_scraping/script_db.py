# Connexion à la base de données postgresql
import psycopg2
import json
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
import os

# Chargement des variables secrètes
load_dotenv()


# Vérification du chargement des variables secrètes
print("Vérification des variables secrètes")
for var in ['db_name', 'db_user', 'db_password', 'db_port']:
    val = os.getenv(var)
    print(f"{var} → {repr(val)}")


# Connexion with 'toque_et_chef' database
conn = psycopg2.connect(
    database=os.getenv("db_name"),
    user=os.getenv("db_user"),
    host='localhost',
    password=os.getenv("db_password"),
    port=os.getenv("db_port")
)
cur = conn.cursor()


# Chargement des données du dataset
print("Chargement du dataset")
with open('recipes_dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


# Insération des données dans la base de données
print("Insertion dans la base de données postgresql")
for row in data:
    cur.execute("""
        INSERT INTO recipes_recipe (
            title, image_url, season, category, duration, level, cost, number, persons_number, ingredients, steps, date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """,
        (row['title'], row['image_url'], row['season'], row['category'], row['duration'], row['level'], row['cost'], row['number'], row['persons_number'], row['ingredients'], row['steps'], datetime.today())
        )

print("les données sont dans la base de données")
conn.commit()
cur.close()
conn.close()