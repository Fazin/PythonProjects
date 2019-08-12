#       Bibliotecas

from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time



#       Variaveis



# Função de preços Dalben

def precos_dalben(produto):

    URL = 'https://www.dalbendelivery.com.br/produtos/buscas?q=' + produto.replace(' ', '%2B')
    driver.get(URL)
    time.sleep(1)
    innerHTML = driver.execute_script("return document.body.innerHTML")

    time.sleep(1)
    root=soup(innerHTML,"lxml")
    viewcount=root.find_all("div",attrs={'class':'col-xs-6 col-sm-3 col-md-3 col-lg-3 product'})

    # lista de produtos encontrados
    for span in viewcount:
        # print(span)
        nome = span.find("p",attrs={'class':'text-success description center-block text-center hidden-xs'})
        price = span.find("div",attrs={'class':'info-price'})
        lista_produtos = nome.text.strip()
        lista_precos = float(price.text.split()[1].replace(",", "."))
        # print(nome.text.strip() + ': ' + price.text)
        print(nome.text.strip() + ': ' + price.text.split()[1].replace(",", "."))
        print()



def lista_completa_dalben(produto_2):

    precos_dalben(produto_2)
    for page_site in range(2,5):
        precos_dalben(produto_2 + '&page=' + str(page_site))
            
    driver.quit()
    

# Main

#chrome sem cabeçalho
options = webdriver.ChromeOptions()
options.add_argument('headless') 
driver = webdriver.Chrome(options=options)

produto='vinho'
lista_completa_dalben(produto)


