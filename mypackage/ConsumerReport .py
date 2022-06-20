## importing bs4, requests modules
import bs4
import requests

## initialiser  url
url = "https://www.consumerreports.org/cro/a-to-z-index/products/index.htm"

## obtenir la réponse de la page en utilisant la méthode get du module requests
page = requests.get(url)

## stocker le contenu de la page dans une variable
html = page.content

## création d'un objet BeautifulSoup
soup = bs4.BeautifulSoup(html, "lxml")

## voir la classe ou l'id de la balise qui contient les noms et les liens
div_class = "crux-body-copy"

## récupérer tous les divs en utilisant la méthode find_all
div_tags = soup.find_all("div", class_=div_class)## trouver les divs qui ont la classe mentionnée

## nous verrons toutes les balises avec une balise qui a un nom et un lien à l'intérieur de la div.
for tag in div_tags:
    print(tag)