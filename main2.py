from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import pandas as pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

SCROLL_PAUSE_TIME = 0.5
base_url = 'https://n1g.cl/Home'
graficas = '/39-tarjetas-graficas'

item = 1
maximo = 100

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#service = Service
#while graficas and item <= maximo:
#url = base_url + graficas + '?page=' + str(item)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(base_url + graficas)
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
clickdata = driver.find_element(By.CLASS_NAME, "vss-down-icon").click()
time.sleep(2)
page_source = driver.page_source
time.sleep(2)

#respuesta = requests.get(base_url + graficas)
data = BeautifulSoup(page_source, 'html.parser')
buscar_resultados = data.find_all('article', class_='product-miniature js-product-miniature')

#buscar_resultados = data.find_all('h1', class_='product_name')

time.sleep(5)
for resultado in buscar_resultados:
    link = resultado.find('h3', class_='h3 product-title')
    #nombre = link.find('a', class_='product-name')
    url = link.find('a', href=True)
    #print(f"nombre: {link.text.strip()}")
    print(f"url: {url['href']}")
    #item += 1
    #print(buscar_resultados)

