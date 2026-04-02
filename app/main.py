from flask import Flask, render_template, request

app = Flask(__name__)

# Liste complète des plats
pasta_dishes = [
    "Spaghetti à la Carbonara", "Penne à l'Arrabbiata", "Lasagnes", "Fettuccine Alfredo", "Raviolis",
    "Pâtes au Pesto", "Macaroni au Fromage", "Pâtes Primavera", "Ziti au Four", "Gnocchis",
    "Tortellinis", "Linguine aux Palourdes", "Pâtes Puttanesca", "Cacio e Pepe", "Pâtes et Haricots",
    "Tagliatelles au Ragu", "Orecchiette aux Brocolis Rabe", "Pâtes à la Norma", "Pappardelle aux Champignons", "Farfalle au Saumon"
]

# Dictionnaire complet des ingrédients
ingredients = {
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
    "Farfalle au Saumon": {"Farfalle": 100, "Saumon Fumé": 50, "Crème": 50, "Aneth": 5, "Citron": 1}
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        selected_dishes = request.form.getlist("dishes")
        try:
            num_people = int(request.form.get("num_people", 1))
        except ValueError:
            num_people = 1

        result_lines = []
        for dish in selected_dishes:
            if dish not in ingredients:
                result_lines.append(f"<strong>{dish} :</strong> Ingrédients non disponibles<br><br>")
                continue
            result_lines.append(f"<strong>{dish} pour {num_people} personne(s):</strong><br>")
            for ingredient, qty in ingredients[dish].items():
                result_lines.append(f"{ingredient}: {qty * num_people}g<br>")
            result_lines.append("<br>")
        result = "".join(result_lines)
    return render_template("index.html", dishes=pasta_dishes, result=result)

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8000)
