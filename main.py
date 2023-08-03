from bs4 import BeautifulSoup
import requests
import pandas as pd


paginas= [
'https://n1g.cl/Home/computacion/2374-amd-ryzen-3-4100-ryzen-3-4000-series-quad-core-socket-am4-65w-none-integrated-graphics-desktop-processor-100-100000510box.html',
'https://n1g.cl/Home/computacion/1876-amd-ryzen-5-4500-oem-6-core-12-hilos-socket-am4-65w-desktop-processor-.html',
'https://n1g.cl/Home/computacion/1640-procesador-amd-ryzen-3-pro-4350g-3800-mhz-4-core-radeon-graphics-sam4-oem-sin-caja-incluye-ventilador-aparte-pn-100-100000148mp.html',
'https://n1g.cl/Home/computacion/1807-procesador-amd-ryzen-5-5500-42ghz-turbo-6core12thread-am4-box-100-100000457box.html',
'https://n1g.cl/Home/computacion/1647-oem-amd-ryzen-5-pro-4650g-graficos-rx-vega-7-procesador-am4-.html',
'https://n1g.cl/Home/computacion/831-amd-ryzen-5-5600x-6-core-37-ghz-socket-am4-65w-100-100000065box-desktop-processor.html',
'https://n1g.cl/Home/computacion/1311-amd-ryzen-7-5700g-radeon-vega-8-core-38ghz-max-boost-46ghz-socket-am4-graphics.html',
'https://n1g.cl/Home/computacion/2274-amd-ryzen-9-7800x3d-8-core-42-ghz-7000-series-am5-120w-amd-radeon-graphics-desktop-100-100000910wof.html',
'https://n1g.cl/Home/computacion/2248-amd-ryzen-9-7900x3d-12-core-44-ghz-socket-am5-120w-amd-radeon-graphics-desktop-processor-100-100000909wof.html',
'https://n1g.cl/Home/computacion/1917-amd-ryzen-threadripper-pro-5975wx-zen-3-64-hilos-32-core-36-ghz-socket-swrx8-280w-desktop-processor-100-100000445wof.html'
        ]

i = 0
def scrap(paginas):
    for i in range(0, 10,+1):
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

    