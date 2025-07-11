import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)


# Escreve seu código abaixo
extracao = BeautifulSoup(requisicao.text, 'html.parser')

print(extracao.prettify()[:2000])