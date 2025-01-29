from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# URL de votre API
API_URL = "http://3.215.16.52"  # Remplacez par l'URL de votre API FastAPI

@app.route("/")
def index():
    """Page d'index affichant la liste des étudiants."""
    try:
        response = requests.get(f"{API_URL}/etudiants")
        response.raise_for_status()
        etudiants = response.json()  # Récupère les données de l'API
    except requests.exceptions.RequestException as e:
        etudiants = []
        print(f"Erreur lors de la récupération des étudiants : {e}")
    return render_template("index.html", etudiants=etudiants)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
