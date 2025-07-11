# Connexion à la base de données postgresql
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# Vérification du chargement des variables secrètes
for var in ['db_name', 'db_user', 'db_password', 'db_port']:
    val = os.getenv(var)
    print(f"{var} → {repr(val)}")


conn = psycopg2.connect(
    database=os.getenv("db_name"),
    user=os.getenv("db_user"),
    host='localhost',
    password=os.getenv("db_password"),
    port=os.getenv("db_port")
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE recipes(
        id INTEGER PRIMARY KEY,
        title VARCHAR(150) NOT NULL UNIQUE,
        image VARCHAR(200) NOT NULL UNIQUE,
        season VARCHAR(20),
        category VARCHAR(20),
        duration VARCHAR(20),
        level VARCHAR(30),
        cost VARCHAR(30),
        number INTEGER,
        persons_number VARCHAR(30),
        ingredients TEXT NOT NULL,
        steps TEXT NOT NULL,
        date DATE NOT NULL DEFAULT CURRENT_DATE,
        author VARCHAR(50));
    """)

conn.commit()
cur.close()
conn.close()