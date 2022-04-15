from distutils import extension
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
import random
import requests
from subprocess import CREATE_NO_WINDOW
from criador import selecionarlistadefotos
from open_json import ler_config_json

simp_path = r'config\\config.json'
abs_path = os.path.abspath(simp_path)
config = ler_config_json(abs_path)

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get(
    'https://www.instagram.com/accounts/login')
driver.implicitly_wait(20)
driver.find_element_by_name(
    'username').send_keys("marcosviniciusdacunha49")
driver.find_element_by_name(
    'password').send_keys("gen1122")
driver.find_element_by_name('password').click()
driver.find_element_by_name(
    'password').send_keys(Keys.ENTER)
sleep(8)


bio = 1
driver.get('https://www.instagram.com/accounts/edit/')
driver.implicitly_wait(10)
fotos, pasta = selecionarlistadefotos()
try:
    driver.find_element_by_class_name('tb_sK').send_keys(
        f'{pasta}\\{random.choice(fotos)}')
    sleep(2)
    driver.find_element_by_class_name('UP43G').click()
except:
    pass
# selecionar bio
if config['montagem']['alterar_foto_de_perfil']:
    simp_path = r'config\\biografias.txt'
    with open(simp_path) as f:
        bios = [line.strip() for line in f if line.strip()]
    bios = random.choice(bio)
    if bio == 0:
        driver.get('https://www.instagram.com/accounts/edit/')
        driver.implicitly_wait(10)
    sleep(2)
    driver.find_element_by_class_name('p7vTm').send_keys(bios)
    buttons = driver.find_elements_by_xpath(
        "//*[contains(text(), 'Enviar')]")
    for btn in buttons:
        btn.click()
