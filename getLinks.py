from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
import time
import getDataProducto
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi


SCROLL_PAUSE_TIME = 0.5

datos =  [{'web': 'https://n1g.cl/Home/71-amd-cpu', 'cantidad': 19},  
         {'web': 'https://n1g.cl/Home/50-placa-madre-amd', 'cantidad': 32}, 
         {'web': 'https://n1g.cl/Home/39-tarjetas-graficas', 'cantidad': 45}, 
         {'web': 'https://n1g.cl/Home/98-teclados', 'cantidad': 15}]


item = 1
maximo = 100

def links(datos):
    for i in range(0, len(datos), +1):
        url = datos[i]["web"]
        cantidad = datos[i]["cantidad"]

        if 64 > cantidad > 32:
            service = Service()
            options = Options()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument('--headless')
            #options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Firefox(service=service, options=options)

            driver.get(url)
            time.sleep(4)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
            clickdata = driver.find_element(By.CLASS_NAME, "vss-down-icon").click()
            time.sleep(4)
            page_source = driver.page_source
            time.sleep(4)

            #respuesta = requests.get(base_url + graficas)
            data = BeautifulSoup(page_source, 'html.parser')
            buscar_resultados = data.find_all('article', class_='product-miniature js-product-miniature')

            #buscar_resultados = data.find_all('h1', class_='product_name')
            data = []
            time.sleep(5)

            for resultado in buscar_resultados:
                link = resultado.find('h3', class_='h3 product-title')
                url = link.find('a', href=True)
                data.append(url['href'])
            
            
            #print(data)
            datosProducto = getDataProducto.scrapProducto(data)
            
            #print(datosProducto)
            #Insert base de datos
            conn = MongoClient("mongodb+srv://modingeroliver:Olivercolopa1@clustertst.cb6tmee.mongodb.net/", tlsCAFile=certifi.where())
            db = conn["productospc"]
            coll = db["cantidadporweb"]
            guarda = coll.insert_many(datosProducto)
            print(guarda.inserted_ids)
            conn.close()
        
        if cantidad < 32:
            service = Service()
            options = Options()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument('--headless')
            #options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Firefox(service=service, options=options)

            driver.get(url)
            time.sleep(4)
            page_source = driver.page_source
            time.sleep(4)

            #respuesta = requests.get(base_url + graficas)
            data = BeautifulSoup(page_source, 'html.parser')
            buscar_resultados = data.find_all('article', class_='product-miniature js-product-miniature')

            #buscar_resultados = data.find_all('h1', class_='product_name')
            data = []
            time.sleep(5)

            for resultado in buscar_resultados:
                link = resultado.find('h3', class_='h3 product-title')
                url = link.find('a', href=True)
                data.append(url['href'])
            

            #print(data)
            datosProducto = getDataProducto.scrapProducto(data)

            conn = MongoClient("mongodb+srv://modingeroliver:Olivercolopa1@clustertst.cb6tmee.mongodb.net/", tlsCAFile=certifi.where())
            db = conn["productospc"]
            coll = db["DatosProductos"]
            guarda = coll.insert_many(datosProducto)
            print(guarda.inserted_ids)
            conn.close()

    return datosProducto

#SegundoPaso = links(datos)

#for resultado in buscar_resultados:
#    link = resultado.find('h3', class_='h3 product-title')
#    #nombre = link.find('a', class_='product-name')
#    url = link.find('a', href=True)
#    #print(f"nombre: {link.text.strip()}")
#    data.append(url['href'])
#    #print("'"+ url['href'] +"',")
#    #item += 1
#    #print(buscar_resultados)
#
#        print(data)