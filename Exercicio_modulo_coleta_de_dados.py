import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

#Requisitando dados do site https://books.toscrape.com/
url = 'https://books.toscrape.com/'
requisicao = requests.get(url)


extracao = BeautifulSoup(requisicao.text, 'html.parser')

print(extracao.prettify()[:2000])