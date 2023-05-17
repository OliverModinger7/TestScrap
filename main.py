from bs4 import BeautifulSoup
import requests
import pandas as pd


paginas= [
    'https://n1g.cl/Home/computacion/1640-procesador-amd-ryzen-3-pro-4350g-3800-mhz-4-core-radeon-graphics-sam4-oem-sin-caja-incluye-ventilador-aparte-pn-100-100000148mp.html',
    'https://n1g.cl/Home/computacion/1807-procesador-amd-ryzen-5-5500-42ghz-turbo-6core12thread-am4-box-100-100000457box.html',
    'https://n1g.cl/Home/computacion/1647-oem-amd-ryzen-5-pro-4650g-graficos-rx-vega-7-procesador-am4-.html',
    'https://n1g.cl/Home/computacion/1310-amd-ryzen-5-5600g-graficos-vega-6-core-12-hilos-39ghz-socket-am4-100-100000252box-cpu-retail.html',
    'https://n1g.cl/Home/computacion/1673-amd-ryzen-5-5600-6-core-socket-am4-65w-100-100000927box.html',
    'https://n1g.cl/Home/computacion/831-amd-ryzen-5-5600x-6-core-37-ghz-socket-am4-65w-100-100000065box-desktop-processor.html',
    'https://n1g.cl/Home/computacion/1672-amd-ryzen-7-5700x-ryzen-7-5000-series-8-core-socket-am4-65w-desktop-processor-100-100000926wof.html',
    'https://n1g.cl/Home/computacion/1311-amd-ryzen-7-5700g-radeon-vega-8-core-38ghz-max-boost-46ghz-socket-am4-graphics.html',
    'https://n1g.cl/Home/computacion/805-amd-ryzen-7-5800x-47ghz-turbo-8core-16-hilos-105w-tdp-pci-e-40.html',
    'https://n1g.cl/Home/computacion/1927-amd-ryzen-5-7600x-socket-am5-6-core-12-hilos-max-53ghz-.html',
    'https://n1g.cl/Home/computacion/1928-amd-ryzen-7-7700x-socket-am5-8-core-16-hilos-max-54ghz-video-int.html',
    'https://n1g.cl/Home/computacion/1778-amd-ryzen-7-5800x3d-8-core-34-ghz-socket-am4-105w-100-100000651wof.html',
    'https://n1g.cl/Home/computacion/2274-amd-ryzen-9-7800x3d-8-core-42-ghz-7000-series-am5-120w-amd-radeon-graphics-desktop-100-100000910wof.html',
    'https://n1g.cl/Home/computacion/806-amd-ryzen-9-5950x-49ghz-turbo-16core-32-hilos-105w-tdp-pci-e-40.html',
    'https://n1g.cl/Home/computacion/2248-amd-ryzen-9-7900x3d-12-core-44-ghz-socket-am5-120w-amd-radeon-graphics-desktop-processor-100-100000909wof.html',
    'https://n1g.cl/Home/computacion/1930-amd-ryzen-9-7950x-socket-am5-16-core-32-hilos-max-57ghz-video-int.html',
    'https://n1g.cl/Home/computacion/2221-amd-ryzen-9-7950x3d-16-core-42-ghz-7000-series-am5-120w-amd-radeon-graphics-desktop-processor-100-100000908wof.html',
    'https://n1g.cl/Home/computacion/2236-amd-ryzen-threadripper-pro-5955wx-16-core-40-ghz-chagall-pro-socket-swrx8-280w-100-100000447wof.html',
    'https://n1g.cl/Home/computacion/2009-amd-ryzen-threadripper-pro-5965wx-48-hilos-24-core-38-ghz-socket-swrx8-280w-100-100000446wof.html',
    'https://n1g.cl/Home/computacion/1917-amd-ryzen-threadripper-pro-5975wx-zen-3-64-hilos-32-core-36-ghz-socket-swrx8-280w-desktop-processor-100-100000445wof.html',
    'https://n1g.cl/Home/computacion/2008-amd-ryzen-threadripper-pro-5995wx-128-hilos-64-core-27-ghz-socket-swrx8-280w-100-100000444wof.html'
        ]

i = 0
def scrap(paginas):
    for i in range(0, 21,+1):
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

    