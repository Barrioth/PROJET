import os
from flask import Flask, render_template, request
from database import init_db, get_all_pastas, get_ingredients

app = Flask(__name__)

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    pasta_dishes = get_all_pastas()
    result = ""

    if request.method == "POST":
        selected_dishes = request.form.getlist("dishes")
        try:
            num_people = int(request.form.get("num_people", 1))
        except ValueError:
            num_people = 1

        result_lines = []
        for dish in selected_dishes:
            ingrs = get_ingredients(dish)
            if not ingrs:
                result_lines.append(f"<strong>{dish} :</strong> Ingrédients non disponibles<br><br>")
                continue
            result_lines.append(f"<strong>{dish} pour {num_people} personne(s):</strong><br>")
            for ingredient, qty in ingrs.items():
                result_lines.append(f"{ingredient}: {qty * num_people}g<br>")
            result_lines.append("<br>")
        result = "".join(result_lines)

    return render_template("index.html", dishes=pasta_dishes, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)