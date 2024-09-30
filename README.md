# Scraping d'offres d'emploi Python

Ce script permet de scraper des offres d'emploi spécifiques à Python à partir du site web [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/). Le programme extrait les informations sur les emplois comme le titre, l'entreprise, le lieu et les liens pour postuler. 

## Prérequis

Assurez-vous d'avoir Python 3.x installé ainsi que les bibliothèques nécessaires.

### Installation des dépendances

Les modules suivants sont nécessaires pour exécuter ce script :

- `requests` : pour faire des requêtes HTTP.
- `beautifulsoup4` : pour analyser le HTML.

Vous pouvez installer ces dépendances en exécutant :

```bash
pip install requests beautifulsoup4
```

## Package


beautifulsoup4     4.12.3
certifi            2024.8.30
charset-normalizer 3.3.2
distlib            0.3.8
filelock           3.16.1
idna               3.10
lxml               5.3.0
numpy              2.1.1
pandas             2.2.3
pip                24.2
platformdirs       4.3.6
python-dateutil    2.9.0.post0
pytz               2024.2
requests           2.32.3
six                1.16.0
soupsieve          2.6
tzdata             2024.2
urllib3            2.2.3
virtualenv         20.26.6



## Fonctionnement

Le script effectue les actions suivantes :

1. **Requête HTTP** : Il envoie une requête GET à l'URL `https://realpython.github.io/fake-jobs/` pour obtenir le contenu de la page.
2. **Analyse du HTML** : Il utilise BeautifulSoup pour analyser la page HTML récupérée.
3. **Recherche des offres d'emploi Python** :
   - Le script cherche l'élément HTML contenant les offres d'emploi via l'ID `ResultsContainer`.
   - Il recherche ensuite tous les éléments <h2> dont le texte contient le mot "python" (insensible à la casse).
4. **Extraction des informations** :
   - Pour chaque emploi Python trouvé, le script extrait :
     - Le **titre de l'emploi**.
     - Le **nom de l'entreprise**.
     - Le **lieu**.
     - Les **liens** associés pour postuler.
5. **Affichage des résultats** : Les informations extraites sont affichées dans la console.

## Exemples de sortie

Voici un exemple de la sortie que vous pouvez obtenir :

```
Il y a 10 jobs en Python

Emploi: Senior Python Developer
Entreprise: Acme Corp
Ville: San Francisco, CA
Apply here: https://realpython.github.io/fake-jobs/python-developer

Emploi: Python Engineer
Entreprise: Widgets Inc
Ville: New York, NY
Apply here: https://realpython.github.io/fake-jobs/python-engineer


## Avertissements

- Ce script est à des fins d'exemple et fonctionne sur une page statique fictive. Si vous voulez l'utiliser sur un site réel, assurez-vous de respecter les [conditions d'utilisation](https://realpython.com/legal/) du site en question, en particulier celles concernant le scraping.


```<img width="1512" alt="Capture d’écran 2024-09-30 à 16 13 35" src="https://github.com/user-attachments/assets/a3a4de60-336c-4cb8-9cf2-e4407e3e9dd7">
