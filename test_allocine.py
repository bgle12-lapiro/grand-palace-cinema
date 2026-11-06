
import requests
from bs4 import BeautifulSoup

url = "https://www.allocine.fr/film/fichefilm_gen_cfilm=1000031247.html"

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=20
    )
    print("Code de réponse :", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    texte = soup.get_text(" ", strip=True)

    print("Titre trouvé :", "La Maison de nos rêves" in texte)
    print("Mention Presse :", "Presse" in texte)
    print("Mention Spectateurs :", "Spectateurs" in texte)

except requests.RequestException as erreur:
    print("Erreur :", erreur)
