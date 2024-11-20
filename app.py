from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from flask import request, jsonify

app = Flask(__name__)

# Chargement des données
data = pd.read_csv("economic_data.csv")
data["Date"] = pd.to_datetime(data["Date"])

@app.route("/")
def index():
    return render_template("index.html")
    # Génération du graphique à chaque chargement de la page
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data["Exchange_Rate"], label="Taux de change", color="blue", linewidth=2)
    plt.xlabel("Date")
    plt.ylabel("Taux de change")
    plt.title("Taux de change sur un an")
    plt.legend()
    plt.grid(visible=True, linestyle="--", alpha=0.5)
    plt.savefig("static/plot.png")
    plt.close()
    return render_template("index.html")


@app.route("/predict", methods=["GET"])
def predict():
    month = int(request.args.get("month", 1))
    # Exemple de prédiction simple (statique pour l'instant)
    prediction = data[data["Date"].dt.month == month]["Exchange_Rate"].mean()
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(debug=True)
