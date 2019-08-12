    ############ ROTINA DO REPORT - PickingAll

def picking_All_Report(centro):

    # Selecionar iframe lateral

    browser.get(URL)
    time.sleep(5)
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.ID, 'sidebar'))
        WebDriverWait(browser, timeout).until(element_present)
        time.sleep(1)
    except TimeoutException:
        print("Timed out waiting for page to load")

    time.sleep(3)
    _ = browser.switch_to.default_content()
    time.sleep(3)

    _ = browser.switch_to.frame('sidebar')
    elem4 = browser.find_element_by_id('Link4')
    elem4.click()
    time.sleep(3)
    elem5 = browser.find_element_by_id('Link4_7')
    elem5.click()

    # Selecionar iframe principal
    time.sleep(10)



    _ = browser.switch_to.default_content()
    time.sleep(3)
    _ = browser.switch_to.frame('mainBody')

    _ = browser.find_elements_by_xpath('//a[contains(@href, "PICKING_ALL")]')[0].click()
    time.sleep(10)
    # inicio picking all 

    _ = browser.switch_to.default_content()
    time.sleep(3)
    _ = browser.switch_to.frame('mainBody')

    fecha = datetime.today().strftime('%Y-%m-%d')
    elem7 = browser.find_element_by_id('P_START_DATE::content')
    elem7.send_keys(fecha)

    elem8 = browser.find_element_by_id('P_CENTRO')
    elem8.send_keys(centro)

    elem9 = browser.find_element_by_name('submit_report')
    path = 'C:\\Users\\fabricio.passos\\Downloads\\Reports'
    deleta_arquivos(path)

    elem9.click()

    Download_Completed() # Verifica que download terminou
    Move_Download(centro) # Move arquivo dos downloads para pasta correta com nome ok

# Deleta arquivos da pasta

def deleta_arquivos(folder):
    import os
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path) #Deletaria pastas tbm
        except Exception as e:
            print(e)

# Função para verificar Download

def Download_Completed():
    import shutil
    import os
    from glob import glob

    path = 'C:\\Users\\fabricio.passos\\Downloads\\Reports'
    tempo=0
    
    # GARANTE QUE A PASTA ESTA VAZIA

    #deleta_arquivos(path)

    
    while os.listdir(path) == [] or glob('C:/Users/fabricio.passos/Downloads/Reports/*.crdownload'):
        time.sleep(1)
        tempo=tempo+1

    
    print('Download terminou em (s): ' + str(tempo))

# Função para mover arquivos

def Move_Download(novo_nome):
    import shutil
    import os
    path = 'C:\\Users\\fabricio.passos\\Downloads\\Reports\\'
    destino = 'C:\\Users\\fabricio.passos\\Downloads\\Arquivos_TOTA\\'

    time.sleep(1)
    shpfiles = []
    for dirpath, _, files in os.walk(path):
        for x in files:
            shpfiles.append(os.path.join(dirpath, x))

    novo_lugar = destino + novo_nome + '.xls'
    os.unlink(novo_lugar)
    shutil.move(str(shpfiles[0]) , novo_lugar)
    deleta_arquivos(path)


###

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import shutil
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime





#Ajusta local de download
options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": r"C:\Users\fabricio.passos\Downloads\Reports",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}

options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(options=options)

browser.get(URL)

elem1 = browser.find_element_by_name('username')  # Find the search box

elem2 = browser.find_element_by_name('userpassword')  # Find the search box

time.sleep(3)
elem3 = browser.find_element_by_name('submitbutton')
elem3.click()
time.sleep(3)


picking_All_Report('3006')
picking_All_Report('5002')
picking_All_Report('3002')
picking_All_Report('3007')
picking_All_Report('3004')
picking_All_Report('5011')

browser.close()