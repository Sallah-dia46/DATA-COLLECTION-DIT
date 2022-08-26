from LIBRAIRIES.utils import Utils
from LIBRAIRIES.csv import CsvFactory
from LIBRAIRIES.json import JsonFactory
from LIBRAIRIES.html import HtmlFactory
from LIBRAIRIES.Bceao import CurrencyScrapper

################### Tous les fichiers.py ou modules importés dans cet exercices sont ajoutés dans ce répertoires avec des modification adaptés à ce programme.########
###Les questions 1, 2, 3 sont au niveau du fichier ou module html.py que j'ai mis dans le répertoire.

#4 Implémentation d'une méthode qui concatène tous les trois datas. C'est à dire:
	- Celui de CsvFactory
	- Celui de JsonFactory
	- Celui de HtmlFactory
    
    
def concatener(data1, data2, data3):
    data = data1+data2+data3
    return data 

#5 Utiliser le lien de la BCEAO concernant les devises:
	- Ajouter une nouvelle entrée dans la donnée globale
	- Puis cette entrée doit contenir (Euro, Dollar, Yen)
	- Attribuer de manière aléatoire ces Devises
	- Grace aux données collecter via Scrapping du site de la BCEAO concernant les devises
	- Ajouter une nouvelle entrée qui donnera la conversion en XOF
		- Ainsi on aura une entrée contenant la devise attribuée
		- Puis une entrée dant la conversion en XOF via les données de la BCEAO
###5 comme j'ai importé la méthode CurrencyScrapper de module Bceao.py, les codes sont dans ce fichier Bceao.py

###6 Utiliser l'API FREE de countries
    - Chercher l'API countries sur le NET
	- Pour ajouter des pays de manière aléatoire dans une nouvelle entrée (Colonne)
	- Puis y joindre les flags de ces pays dans une nouvelle entrée


if __name__ == '__main__':
    print(Utils.divider())
    print(HtmlFactory.main())
    print(Utils.divider())
    DATA_total= concatener(HtmlFactory.main(),CsvFactory.main(), JsonFactory.main())
    print(DATA_total) 
    print(
  



    
