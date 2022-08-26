from LIBRAIRIES.utils import Utils
from LIBRAIRIES.csv import CsvFactory
from LIBRAIRIES.json import JsonFactory
from LIBRAIRIES.html import HtmlFactory
from LIBRAIRIES.Bceao import CurrencyScrapper





def concatener(data1, data2, data3):
    data = data1+data2+data3
    return data 


if __name__ == '__main__':
    print(Utils.divider())
    print(HtmlFactory.main())
    print(Utils.divider())
    DATA_total= concatener(HtmlFactory.main(),CsvFactory.main(), JsonFactory.main())
    print(DATA_total) 
  



    
