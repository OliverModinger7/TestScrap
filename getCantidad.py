from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
import getLinks
import getDataProducto

### Parte 1 
webs = [
'https://n1g.cl/Home/71-amd-cpu',
#'https://n1g.cl/Home/72-intel-cpu',
#'https://n1g.cl/Home/50-placa-madre-amd'
#'https://n1g.cl/Home/51-placa-madre-intel',
#'https://n1g.cl/Home/67-pendrive-flash',
#'https://n1g.cl/Home/69-ddr4-pc',
#'https://n1g.cl/Home/74-memoria-notebook',
#'https://n1g.cl/Home/77-ddr5-pc',
#'https://n1g.cl/Home/54-discos-ssd',
#'https://n1g.cl/Home/55-discos-hdd',
#'https://n1g.cl/Home/56-discos-25',
#'https://n1g.cl/Home/60-discos-duros-accesorios',
#'https://n1g.cl/Home/57-fuentes-certificadas-modular',
#'https://n1g.cl/Home/58-fuentes-certificadas-no-modular',
#'https://n1g.cl/Home/59-accesorios-de-fuentes-de-poder',
#'https://n1g.cl/Home/39-tarjetas-graficas',
#'https://n1g.cl/Home/24-gabinetes',
#'https://n1g.cl/Home/61-disipador-por-aire',
#'https://n1g.cl/Home/62-watercooling',
#'https://n1g.cl/Home/63-ventiladores',
#'https://n1g.cl/Home/64-pasta-disipadora',
#'https://n1g.cl/Home/28-monitores',
#'https://n1g.cl/Home/92-mouse',
#'https://n1g.cl/Home/93-mousepad',
#'https://n1g.cl/Home/98-teclados'
]

w = len(webs)
i = 0
data = []
datos = {}

def ping():
    try:
        conn = MongoClient('mongodb+srv://modingeroliver:Olivercolopa1@clustertst.cb6tmee.mongodb.net/', tlsCAFile=certifi.where())
        print("Connected successfully!!!")
    except:  
        print("Could not connect to MongoDB")



def scrap(webs):
    for i in range(0, w,+1):
        url = webs[i]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        cantidad = soup.find('div', class_='row products-selection')
        datos = cantidad.find('p').text
        datos = datos.replace("Hay ", "")
        datos = datos.replace(" productos.", "")
        numeros = int(datos)
        datosWeb = {
            "web" : webs[i],
            "cantidad" : numeros
        }
        data.append(datosWeb)
        #print(datosWeb)

        #insert(datosWeb)
        
    return data

#scrap(webs)
#print(data)
PrimerPaso = scrap(webs)
SegundoPaso = getLinks.links(PrimerPaso)
#getDataProducto.scrapProducto(SegundoPaso)


#conn = MongoClient("mongodb+srv://modingeroliver:Olivercolopa1@clustertst.cb6tmee.mongodb.net/", tlsCAFile=certifi.where())
#db = conn["productospc"]
#coll = db["cantidadporweb"]
#guarda = coll.insert_many(data)
#print(guarda.inserted_ids)
#conn.close()
#'''

### Parte 2


### Parte 3
#paginas= [
#'https://n1g.cl/Home/computacion/2374-amd-ryzen-3-4100-ryzen-3-4000-series-quad-core-socket-am4-65w-none-integrated-graphics-desktop-processor-100-100000510box.html',
#'https://n1g.cl/Home/computacion/1876-amd-ryzen-5-4500-oem-6-core-12-hilos-socket-am4-65w-desktop-processor-.html',
#'https://n1g.cl/Home/computacion/1640-procesador-amd-ryzen-3-pro-4350g-3800-mhz-4-core-radeon-graphics-sam4-oem-sin-caja-incluye-ventilador-aparte-pn-100-100000148mp.html',
#'https://n1g.cl/Home/computacion/1807-procesador-amd-ryzen-5-5500-42ghz-turbo-6core12thread-am4-box-100-100000457box.html',
#'https://n1g.cl/Home/computacion/1647-oem-amd-ryzen-5-pro-4650g-graficos-rx-vega-7-procesador-am4-.html',
#'https://n1g.cl/Home/computacion/831-amd-ryzen-5-5600x-6-core-37-ghz-socket-am4-65w-100-100000065box-desktop-processor.html',
#'https://n1g.cl/Home/computacion/1311-amd-ryzen-7-5700g-radeon-vega-8-core-38ghz-max-boost-46ghz-socket-am4-graphics.html',
#'https://n1g.cl/Home/computacion/2274-amd-ryzen-9-7800x3d-8-core-42-ghz-7000-series-am5-120w-amd-radeon-graphics-desktop-100-100000910wof.html',
#'https://n1g.cl/Home/computacion/2248-amd-ryzen-9-7900x3d-12-core-44-ghz-socket-am5-120w-amd-radeon-graphics-desktop-processor-100-100000909wof.html',
#'https://n1g.cl/Home/computacion/1917-amd-ryzen-threadripper-pro-5975wx-zen-3-64-hilos-32-core-36-ghz-socket-swrx8-280w-desktop-processor-100-100000445wof.html'
#        ]

#getDataProducto.scrapProducto(paginas)