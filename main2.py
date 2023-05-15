from bs4 import BeautifulSoup
import requests
import pandas as pd


paginas= []

{'https://n1g.cl/Home/computacion/1683-gigabyte-gt-1030-low-profile-2gb-pci-express-16x-30-gv-n1030d5-2gl-.html',
        'https://n1g.cl/Home/computacion/1007-evga-xr1-capturadora-certificada-obs-usb-30-4k-pass-argb-mesclador-de-audio-pc-ps5-xbox-nintendo.html',
        'https://n1g.cl/Home/computacion/942-asus-tuf-gtx-1650-4gb-128-bit-gddr6-geforce-tuf-gtx1650-o4gd6-p-gaming-pci-express-30.html',
        'https://n1g.cl/Home/computacion/2099-asrock-amd-radeon-rx-6600-challenger-d-8gb-3x-displayport.html'
}

url = 'https://n1g.cl/Home/computacion/1683-gigabyte-gt-1030-low-profile-2gb-pci-express-16x-30-gv-n1030d5-2gl-.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Data

extract = soup.find_all('h1', class_='product_name')

data = list()

count = 0
for i in extract:
    if count < 20:
        data.append(i.text)
    else:
        break
    count += 1

print(data)