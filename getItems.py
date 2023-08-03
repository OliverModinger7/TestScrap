from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

webs = [
'https://n1g.cl/Home/71-amd-cpu',
'https://n1g.cl/Home/72-intel-cpu',
'https://n1g.cl/Home/50-placa-madre-amd',
'https://n1g.cl/Home/51-placa-madre-intel',
'https://n1g.cl/Home/67-pendrive-flash',
'https://n1g.cl/Home/69-ddr4-pc',
'https://n1g.cl/Home/74-memoria-notebook',
'https://n1g.cl/Home/77-ddr5-pc',
'https://n1g.cl/Home/54-discos-ssd',
'https://n1g.cl/Home/55-discos-hdd',
'https://n1g.cl/Home/56-discos-25',
'https://n1g.cl/Home/60-discos-duros-accesorios',
'https://n1g.cl/Home/57-fuentes-certificadas-modular',
'https://n1g.cl/Home/58-fuentes-certificadas-no-modular',
'https://n1g.cl/Home/59-accesorios-de-fuentes-de-poder',
'https://n1g.cl/Home/39-tarjetas-graficas',
'https://n1g.cl/Home/24-gabinetes',
'https://n1g.cl/Home/61-disipador-por-aire',
'https://n1g.cl/Home/62-watercooling',
'https://n1g.cl/Home/63-ventiladores',
'https://n1g.cl/Home/64-pasta-disipadora',
'https://n1g.cl/Home/28-monitores',
'https://n1g.cl/Home/92-mouse',
'https://n1g.cl/Home/93-mousepad',
'https://n1g.cl/Home/98-teclados'
]

w = len(webs)
i = 0
lista = []

def scrap():
    for i in range(0, w,+1):
        url = webs[i]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        cantidad = soup.find('div', class_='row products-selection')
        datos = cantidad.find('p').text
        datos = datos.replace("Hay ", "")
        datos = datos.replace(" productos.", "")
        numeros = int(datos)
        lista.append(numeros)
        lista.append(webs[i])
        
    return lista

scrap()
print(lista)