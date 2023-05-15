from bs4 import BeautifulSoup
import requests
import pandas as pd


paginas= [
    'https://n1g.cl/Home/computacion/2178-lian-li-gpu-bracket-kit-upright-black-for-lian-li-o11-dynamic-evo.html',
    'https://n1g.cl/Home/computacion/2096-fantech-cg74-gabinete-atx-rgb-black-edition-vidrio-templado-sin-fan.html',
    'https://n1g.cl/Home/computacion/243-gabinete-fantech-strike-cg72-rgb-atx-vidrio-templado-sin-fuente-negro.html',
    'https://n1g.cl/Home/computacion/543-gabinete-black-5915-atx-micro-atx-mini-itx-fuente-300w-2x-usb-20-audio.html',
    'https://n1g.cl/Home/computacion/428-gabinete-slim-clio-cl-s605-500w-micro-atx-itx-fuente-de-poder.html',
    'https://n1g.cl/Home/computacion/2186-gabinete-black-hole-2x-200mm-argb-gamemax-atx-sin-fuente.html',
    'https://n1g.cl/Home/computacion/893-inwin-gabinete-atx-101-tuf-gaming.html',
    'https://n1g.cl/Home/computacion/2185-gabinete-gamer-gamemax-white-diamond-rgb-atx-m-atx.html',
    'https://n1g.cl/Home/computacion/2187-gamemax-brufen-c3-whitepink.html',
    'https://n1g.cl/Home/computacion/546-gabinete-itx-stratos-vidrio-templado-argb-2x-fan-120mm-high-end-vga-fuente-sfx.html',
    'https://n1g.cl/Home/computacion/2188-gabinete-precision-white-120mm-fan-argb-e-atx-atx-matx-gamer-gamemax-controladora-sin-fuente.html',
    'https://n1g.cl/Home/computacion/2302-gabinete-mini-itx-cougar-qbx-black-psu-atx-ultra-compact-pro-gaming-case.html',
    'https://n1g.cl/Home/computacion/1293-msi-mpg-sekira-100r-4x-120mm-argb-gabinete-atx-e-atx-micro-atx-mini-itx.html',
    'https://n1g.cl/Home/computacion/687-inwin-development-bp655fh300tb3-haswell-miniitx-chasis-bp655-casos-bp655fh300tb3.html',
    'https://n1g.cl/Home/computacion/2087-lian-li-tu150-itx-silver-gabinete-de-aluminio-y-vidrio-templado-tu150wa.html',
    'https://n1g.cl/Home/computacion/2088-lian-li-tu150-itx-black-gabinete-de-aluminio-y-vidrio-templado-tu150xa.html',
    'https://n1g.cl/Home/computacion/544-gabinete-rackeable-4u-para-server-atx-e-atx-rackmount-incluye-rieles-y-manillas.html',
    'https://n1g.cl/Home/computacion/1294-msi-mpg-sekira-500p-black-steel-4x-120mm-argb-gabinete-atx-e-atx-micro-atx-mini-itx.html',
    'https://n1g.cl/Home/computacion/2303-gabinete-in-win-explorer-iw-cs-explorer-tempered-glass-abs-mini-itx.html',
    'https://n1g.cl/Home/computacion/2082-lian-li-o11-dynamic-mini-white-atx-micro-atx-mini-itx-mini-o11d-mini-s-sfx-sfx-l-.html',
    'https://n1g.cl/Home/computacion/2208-asus-tuf-gaming-gt502-black-atx-mid-tower-panel-rgb-button-usb-32-type-c-and-2x-usb-30-360mm-280mm-radiator.html',
    'https://n1g.cl/Home/computacion/1399-chenbro-gabinete-rackeable-4u-server-rm42300-f-12-mm-sgcc-3-bahias-de-525-externas-dvd-opcion.html',
    'https://n1g.cl/Home/computacion/1614-inwin-a1-plus-pink-mini-itx-tower-con-argb-650w-gold-psu-qi-wireless-charger-case.html',
    'https://n1g.cl/Home/computacion/2198-lian-li-o11-dynamic-evo-grey-o11deg-aluminum-steel-tempered-glass-atx-mid-tower.html',
    'https://n1g.cl/Home/computacion/2085-lian-li-o11-dynamic-evo-o11dex-white-aluminum-steel-tempered-glass-atx-mid-tower.html',
    'https://n1g.cl/Home/computacion/2200-lian-li-o11-dynamic-xl-rog-silver-o11dxl-a-tempered-glass-e-atx-atx-full-tower.html',
    'https://n1g.cl/Home/computacion/1397--lian-li-o11-dynamic-xl-rog-certificado-white-color-temp.html',
    'https://n1g.cl/Home/computacion/2199-lian-li-o11-dynamic-xl-rog-black-o11dxl-x-tempered-glass-e-atx-atx-full-tower.html',
    'https://n1g.cl/Home/computacion/1607-asus-rog-z11-mini-itxdtx-mid-tower-pc-gaming-case-3-slot-graphics-gen-2-type-c-two-usb-32.html',
    'https://n1g.cl/Home/computacion/2086-nzxt-h510i-all-might-edicion-limitada-tower-pc-gaming-case-front-io-usb-type-c-port.html',
    'https://n1g.cl/Home/computacion/1439-gabinete-asus-strix-helios-rgb-gx601-negro-fan-incluidos-4x-140mm-eatx-atx-matx-itx-vidrio-templado-aluminio.html',
    'https://n1g.cl/Home/computacion/2006-asus-rog-strix-helios-eva-edition-aluminio-y-vidrio-templado-90dc0020-b30010-atx.html'
        ]

i = 0
data2 = []
def scrap(paginas):
    for i in range(0, 32,+1):
        url = paginas[i]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        name = soup.find('h1', class_='product_name')
        valor = soup.find('span', itemprop='price')
        stock = soup.find('div', class_='si-items')
        data = list()
        data.append(name.text)
        data.append(valor.text)
        data.append(stock.text)
        print(data)
        
    return data


scrap(paginas)

    