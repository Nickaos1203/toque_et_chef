import pandas as pd


# Fichiers à fusionner
fichiers = ['appetizer_data.json', 'dishe_data.json', 'dessert.json']

# Lire les fichiers JSON (format NDJSON)
dataframes = []
for fichier in fichiers:
    try:
        df = pd.read_json(fichier, lines=True)
        dataframes.append(df)
    except ValueError as e:
        print(f"Erreur lors de la lecture de {fichier} : {e}")

# Fusionner les DataFrames
df_concatene = pd.concat(dataframes)

# Mélanger les lignes sans réinitialiser l'index
df_melange = df_concatene.sample(frac=1)

# Sauvegarder le résultat
df_melange.to_json('recipes_data.json', orient='records', lines=True)

print("Fusion et mélange effectués : 'recipes_data.json'")