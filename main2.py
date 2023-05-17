from bs4 import BeautifulSoup
import requests
import pandas as pd


paginas= []


url = 'https://n1g.cl/Home/71-amd-cpu'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


#extract = soup.find_all('a', )
extract = soup.find_all('a', href=True)

data = list()

count = 0
for a_href in extract:
    print(a_href['href'])


