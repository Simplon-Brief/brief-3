import requests
from bs4 import BeautifulSoup  # Importation des modules : requests pour faire des requêtes HTTP et BeautifulSoup pour analyser le HTML

# L'URL cible que tu veux scraper
URL = "https://realpython.github.io/fake-jobs/"

# Envoi d'une requête GET à l'URL pour obtenir le contenu de la page
page = requests.get(URL)

# Analyse le contenu HTML de la page récupérée avec BeautifulSoup en utilisant le parseur HTML
soup = BeautifulSoup(page.content, "html.parser")

# Recherche de l'élément HTML avec l'ID "ResultsContainer" qui contient les offres d'emploi
results = soup.find(id="ResultsContainer")

# Recherche tous les éléments <h2> dont le texte contient le mot "python" (peu importe la casse, grâce à .lower())
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# Pour chaque élément <h2> trouvé, on récupère son parent à trois niveaux au-dessus, 
# qui correspond à la structure HTML contenant toutes les informations relatives au job (titre, entreprise, lieu, etc.)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Affiche combien de jobs Python ont été trouvés
print(f"Il y a {len(python_jobs)} jobs en Python")
print()# Ajoute une ligne vide pour espacer

# Boucle sur chaque job Python trouvé
for job_element in python_job_elements:
    
    # Recherche du titre de l'emploi dans la balise <h2> ayant la classe "title"
    title_element = job_element.find("h2", class_="title")
    
    # Recherche du nom de l'entreprise dans la balise <h3> ayant la classe "company"
    company_element = job_element.find("h3", class_="company")
    
    # Recherche du lieu du job dans la balise <p> ayant la classe "location"
    location_element = job_element.find("p", class_="location")
    
    print(f"Emploi: {title_element.text.strip()}")   # Affiche le titre du job
    print(f"Entreprise: {company_element.text.strip()}")  # Affiche le nom de l'entreprise
    print(f"Ville: {location_element.text.strip()}")  # Affiche le lieu du job
    print()  # Ajoute une ligne vide pour espacer les différentes offres

    # Recherche tous les liens (<a>) à l'intérieur de cet élément de job (cela peut inclure le lien pour postuler)
    links = job_element.find_all("a")
    
    # Boucle sur chaque lien trouvé
    for link in links:
        # Récupère l'URL du lien à partir de l'attribut "href" de la balise <a>
        link_url = link["href"]
        
        # Affiche l'URL pour postuler au job
        print(f"Apply here: {link_url}\n")
