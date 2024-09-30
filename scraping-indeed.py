import requests
from bs4 import BeautifulSoup  # Importation des modules : requests pour faire des requêtes HTTP et BeautifulSoup pour analyser le HTML

# L'URL cible que tu veux scraper
URL = "https://finance.yahoo.com/markets/stocks/most-active/?guccounter=1"

# Envoi d'une requête GET à l'URL pour obtenir le contenu de la page
page = requests.get(URL)

# Analyse le contenu HTML de la page récupérée avec BeautifulSoup en utilisant le parseur HTML
soup = BeautifulSoup(page.content, "html.parser")


tableauEntier = soup.find_all("span", class_="longName")

for table in tableauEntier:
    print(table.prettify())



