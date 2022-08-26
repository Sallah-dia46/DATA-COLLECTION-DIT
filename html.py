import json
from LIBRAIRIES.utils import Utils
from bs4 import BeautifulSoup


BASE_URL = 'DATA-COLLECTION-DIT\COURSE\DATABASES\data-zIybdmYZoV4QSwgZkFtaB.html'



class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data

    @classmethod
    def main(cls):
        data=cls.openFile() 
        return data   
        
    @classmethod
    def getBoxData(cls):
        soupering=cls.openFile()
        table=[]
        soupering= soupering\
         .find_all('tr')
        for i in soupering[1:]:
            td= i.find_all('td')
            soupering=td[0].text.split(' ')

            table.append({
            'name':f'{soupering[0]} {soupering[-1].upper()}',
            'phone':td[1].text,
            'email':td[2].text,
            'Adress':'',
            'latlng':td[3].text,
            'salary':td[4].text,
            'age':td[5].text
        
                     })
        return table
    
    @classmethod
    def main(cls):
        #1 completer le code de htmlFactory,afin de recuperer les données
        data=cls.openFile()
            #Questions 2 et 3
        data =cls.getBoxData()
        return data
        

