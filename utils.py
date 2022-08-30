import random
import requests
from bs4 import BeautifulSoup
import pandas as pd



class Utils(object):
    @classmethod
    def divider(cls, n=54):
        return '-' * n

    @classmethod
    def randomize(cls,
                  start,
                  final):
        return random \
            .randint(start, final)

    @classmethod
    def x(cls, x):
        x = x.split(' ')
        last_name = x[-1].upper()
        first_name = x[0].capitalize()
        x = ' '.join([first_name, last_name])
        return x
    class DataSouperShop(object):
    @classmethod
    def fetcher(cls, URL):
        assert len(URL) > 0, f"URL expected a non-empty string, got {URL}"
        with requests.Session() as session:
            result = session.get(URL)
            result = result.text
            return result
    @classmethod
    def MakeSoupe(cls, URL):
        assert len(URL) > 0, f"URL expected a non-empty string, got {URL}"
        result = cls.fetcher(URL)
        return BeautifulSoup(
            result.encode('utf-8'),
            'html.parser')

    @classmethod
    def getCards(cls, URL):
        assert len(URL) > 0, f"URL expected a non-empty string, got {URL}"
        soupe = cls.MakeSoupe(URL)
        soupe = soupe \
            .find_all(attrs={
                'class': 'product-small'})
        return soupe

    @classmethod
    def structureDatas(cls, URL):
        pathUrl =['','page/2','page/3','page/4']
        assert len(URL) > 0, f"URL expected a non-empty string, got {URL}"
        tab=[]
        for i in pathUrl:
            cards = cls.getCards(f'{URL}{i}')
            for card in cards:
                price=card.find('bdi').text
                title=card.find(attrs={
                    'class': 'product-title'})
                tab.append({
                    'title': title.text,
                    'prix': price.replace('\xa0CFA',"").replace('.',""),
                    'quantity': 1,
                    'currency': 'XOF/CFA'

                })
        return tab

    @classmethod
    def combineDatas(cls, tab, URL):
        data=DataSouperDevise.structureDatas(URL)
        data=data.head(6)
        for i in tab:
            for j in range(len(data)):
                i.update({
                        data['Devise'][j]: int(i['prix'])*float(data['value'][j])
                    })
        return pd.DataFrame(tab)

class DataSouperDevise(object):
    @classmethod
    def MakeSoupe(cls, URL):
        assert len(URL) > 0, f"URL expected a non-empty string, got {URL}"
        result = DataSouperShop.fetcher(URL)
        return BeautifulSoup(
            result.encode('utf-8'),
            'html.parser')

    @classmethod
    def getCard(cls, URL):
        assert len(URL) > 0, f"URL expected a non-empty string, got {URL}"
        soupe = cls.MakeSoupe(URL)
        soupe = soupe \
            .find('channel')
        return soupe
    
    @classmethod
    def structureDatas(cls, URL):
        assert len(URL) > 0, f"URL expected a non-empty string, got {URL}"
        tab=[]
        card = cls.getCard(URL)
        card=card.find_all('item')
        for item in card[1:]:
            currency=item.find('targetcurrency')
            value=item.find('exchangerate')
            basecurrency = item.find('basecurrency')
            tab.append({
                'Devise': currency.text,
                'value': value.text,
                "basecurrency": basecurrency.text

            })
        return pd.DataFrame(tab)

