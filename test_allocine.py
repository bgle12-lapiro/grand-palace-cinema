import re
import requests
from bs4 import BeautifulSoup

url = "https://www.allocine.fr/film/fichefilm_gen_cfilm=1000031247.html"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
texte = soup.get_text(" ", strip=True)

for rubrique in ["Presse", "Spectateurs"]:
    print(f"\n--- {rubrique} ---")

    for match in list(re.finditer(
        re.escape(rubrique), texte, re.IGNORECASE
    ))[:5]:
        debut = max(0, match.start() - 80)
        fin = min(len(texte), match.end() + 160)
        print(texte[debut:fin])
