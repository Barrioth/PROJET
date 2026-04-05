import sqlite3
import os

DB_PATH = os.path.join("/app/data", "pasta.db")

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pastas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pasta_nom TEXT NOT NULL,
            ingredient TEXT NOT NULL,
            quantite INTEGER NOT NULL,
            FOREIGN KEY (pasta_nom) REFERENCES pastas(nom)
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM pastas")
    if cursor.fetchone()[0] == 0:
        pastas_initiales = {
            "Spaghetti à la Carbonara": {"Spaghetti": 100, "Œufs": 1, "Pancetta": 50, "Parmesan": 20, "Poivre Noir": 1},
            "Penne à l'Arrabbiata": {"Penne": 100, "Sauce Tomate": 100, "Ail": 1, "Piments Rouges": 1, "Persil": 5},
            "Lasagnes": {"Pâtes à Lasagne": 100, "Bœuf Haché": 100, "Sauce Tomate": 100, "Ricotta": 50, "Mozzarella": 50},
            "Fettuccine Alfredo": {"Fettuccine": 100, "Beurre": 50, "Crème Épaisse": 50, "Parmesan": 20, "Ail": 1},
            "Raviolis": {"Pâtes à Ravioli": 100, "Ricotta": 50, "Épinards": 50, "Parmesan": 20, "Sauce Tomate": 100},
            "Pâtes au Pesto": {"Pâtes": 100, "Pesto au Basilic": 50, "Pignons de Pin": 10, "Parmesan": 20, "Ail": 1},
            "Macaroni au Fromage": {"Macaroni": 100, "Fromage Cheddar": 50, "Lait": 50, "Beurre": 20, "Farine": 10},
            "Pâtes Primavera": {"Pâtes": 100, "Légumes Mixtes": 100, "Huile d'Olive": 20, "Ail": 1, "Parmesan": 20},
            "Ziti au Four": {"Ziti": 100, "Sauce Tomate": 100, "Ricotta": 50, "Mozzarella": 50, "Parmesan": 20},
            "Gnocchis": {"Gnocchi de Pomme de Terre": 100, "Sauce Tomate": 100, "Parmesan": 20, "Basilic": 5, "Huile d'Olive": 20},
            "Tortellinis": {"Pâtes Tortellini": 100, "Ricotta": 50, "Parmesan": 20, "Sauce Tomate": 100, "Basilic": 5},
            "Linguine aux Palourdes": {"Linguine": 100, "Palourdes": 100, "Vin Blanc": 50, "Ail": 1, "Persil": 5},
            "Pâtes Puttanesca": {"Pâtes": 100, "Sauce Tomate": 100, "Anchois": 5, "Câpres": 10, "Olives": 10},
            "Cacio e Pepe": {"Spaghetti": 100, "Pecorino Romano": 20, "Poivre Noir": 1, "Beurre": 20, "Sel": 1},
            "Pâtes et Haricots": {"Pâtes": 100, "Haricots Cannellini": 50, "Sauce Tomate": 100, "Ail": 1, "Romarin": 5},
            "Tagliatelles au Ragu": {"Tagliatelle": 100, "Bœuf Haché": 100, "Sauce Tomate": 100, "Carottes": 50, "Céleri": 50},
            "Orecchiette aux Brocolis Rabe": {"Orecchiette": 100, "Brocoli Rabe": 100, "Ail": 1, "Flocons de Piment Rouge": 1, "Huile d'Olive": 20},
            "Pâtes à la Norma": {"Pâtes": 100, "Aubergine": 100, "Sauce Tomate": 100, "Ricotta Salata": 20, "Basilic": 5},
            "Pappardelle aux Champignons": {"Pappardelle": 100, "Champignons Mixtes": 100, "Ail": 1, "Persil": 5, "Huile d'Olive": 20},
            "Farfalle au Saumon": {"Farfalle": 100, "Saumon Fumé": 50, "Crème": 50, "Aneth": 5, "Citron": 1},
        }

        for nom, ingrs in pastas_initiales.items():
            cursor.execute("INSERT INTO pastas (nom) VALUES (?)", (nom,))
            for ingredient, quantite in ingrs.items():
                cursor.execute(
                    "INSERT INTO ingredients (pasta_nom, ingredient, quantite) VALUES (?, ?, ?)",
                    (nom, ingredient, quantite)
                )

    conn.commit()
    conn.close()

def get_all_pastas():
    conn = get_connection()
    pastas = conn.execute("SELECT nom FROM pastas ORDER BY nom").fetchall()
    conn.close()
    return [row["nom"] for row in pastas]

def get_ingredients(pasta_nom):
    conn = get_connection()
    rows = conn.execute(
        "SELECT ingredient, quantite FROM ingredients WHERE pasta_nom = ?",
        (pasta_nom,)
    ).fetchall()
    conn.close()
    return {row["ingredient"]: row["quantite"] for row in rows}