import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


'''entrar a la pagina de Mercado libre, buscar "Camisetas" 
y guardar en un archivo csv el nombre y el precio del primer 1 items 
del resultado de la busqueda'''

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.mercadolibre.com.ar/')
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID, 'cb1-edit').send_keys('Camisetas')
driver.find_element(By.XPATH, '/html/body/header/div/form/button/div').click()

camiseta_a = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol/li[1]/div/div/div[2]/div[1]').click()
camiseta_a1 = driver.find_element(By.ID, 'header')
camiseta_a2 = driver.find_element(By.ID, 'price')

archivo = open('archivo.csv', 'w')
archivo.write(camiseta_a1.text + '' '' + camiseta_a2.text )
driver.close()
