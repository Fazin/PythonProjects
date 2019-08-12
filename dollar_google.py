#       Bibliotecas

from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time



#       Variaveis

moeda='dolar'


# Função de valor dollar Google

def valor_google(moeda):

    URL = 'https://www.google.com/search?q=' + moeda + '+hoje'
    driver.get(URL)
    time.sleep(1)
    
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")

    # time.sleep(1)
    
    # print(source_code)
    root=soup(source_code, 'lxml')
    # print(root)
    valor=root.find_all("span",attrs={'class':'DFlfde SwHCTb'}) 
    valor_real = float(valor[0]['data-value'])
    print(moeda +' GOOGLE: ' + str(valor_real))
    
    # driver.quit()


def valor_transferwise():

    

    URL = 'https://transferwise.com/tools/exchange-rate-alerts/?fromCurrency=USD&toCurrency=BRL'
    driver.get(URL)
    time.sleep(3)

    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")


    root=soup(source_code, 'lxml')
    
    valor=root.find_all("span",attrs={'class':'text-success'}) 

    valor_real = float(valor[0].text.split()[0])
    
    print(moeda +' TRANSFERWISE: ' + str(valor_real))

    # driver.quit()
    

# Main

#chrome sem cabeçalho
options = webdriver.ChromeOptions()
options.add_argument('headless') 
driver = webdriver.Chrome(options=options)

valor_google(moeda)
valor_transferwise()
driver.quit()
