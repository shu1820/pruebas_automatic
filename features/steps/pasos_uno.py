from behave import *
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains



@given(u'Cargando la pagina')
def step_impl(context):
    global driver
    context.driver = webdriver.Chrome('./chromedriver')
    context.driver.get('https://demoqa.com/text-box')
    context.driver.maximize_window()
    time.sleep(2)


@when(u'Ingresar datos de usurario')
def step_impl(context):
    nom = context.driver.find_element(By.ID, 'userName').send_keys('jesus')
    mail = context.driver.find_element(By.ID, 'userEmail').send_keys('jesus@gmail.com')
    direx = context.driver.find_element(By.ID, 'currentAddress').send_keys('bolivar 1224')
    dire1 = context.driver.find_element(By.ID, 'permanentAddress').send_keys('venezuela')
    time.sleep(2)


@then(u'Clik submit finalizar')
def step_impl(context):
    val = WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located((By.ID, 'submit')))
    val = context.driver.execute_script("arguments[0].scrollIntoView();", val)
    val = context.driver.find_element(By.ID, 'submit').click()
    time.sleep(2)
    context.driver.close()
