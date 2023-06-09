from bs4 import BeautifulSoup
import requests
import pandas as pd


paginas= [
'https://n1g.cl/Home/computacion/1567-intel-celeron-g4930-coffee-lake-dual-cor-32-ghz-lga-1151-300-series-54w-bx80684g4930-desktop-processor-intel-uhd-graphics-610.html',
'https://n1g.cl/Home/computacion/1014-intel-core-i5-10400f-comet-lake-6-core-29-ghz-lga-1200-65w-bx8070110400f-desktop-processor.html',
'https://n1g.cl/Home/computacion/1821-intel-core-i3-12100-33-ghz-4-cores-8-threads-12-mb-cache-lga1700-socket-box.html',
'https://n1g.cl/Home/computacion/2292-intel-core-i3-13100-desktop-processor-4-cores-4-p-cores-0-e-cores-12mb-cache-up-to-45-ghz-box.html',
'https://n1g.cl/Home/computacion/1166-intel-core-i5-11500-46ghz-turbo-lga-1200-rocket-lake-6-core-65w-intel-uhd-graphics-750.html',
'https://n1g.cl/Home/computacion/1238-intel-core-i7-10700f-29ghz-16mb-lga1200.html',
'https://n1g.cl/Home/computacion/1485-intel-core-i5-12600k-core-i5-12th-gen-alder-lake-10-core-6p4e-37-ghz-lga-1700-125w-intel-uhd-graphics-770-bx8071512600k.html',
'https://n1g.cl/Home/computacion/605-intel-core-i7-10700-comet-lake-8-core-29-ghz-lga-1200-65w-bx8070110700-procesador-intel-uhd-graphics-630.html',
'https://n1g.cl/Home/computacion/1160-intel-core-i5-11600-lga-1200-48-ghz-turbo-6-nucleos12-thead-rocket-lake-s.html',
'https://n1g.cl/Home/computacion/610-intel-core-i7-10700k-51ghz-turbo-8-core-16-theads-comet-lake-lga-1200-125w-procesador-uhd-graphics-630.html',
'https://n1g.cl/Home/computacion/1484-intel-core-i7-11700k-core-i7-11th-gen-rocket-lake-8-core-36-ghz-lga-1200-125w-intel-uhd-graphics-750-bx8070811700k.html'
        ]

i = 0
def scrap(paginas):
    for i in range(0, 11,+1):
        url = paginas[i]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        name = soup.find('h1', class_='product_name')
        valor = soup.find('span', itemprop='price')
        stock = soup.find('div', class_='si-items')
        data = list()
        data.append(name.text)
        data.append(stock.text)
        data.append(valor.text)
        print(data)
        
    return data


scrap(paginas)

    