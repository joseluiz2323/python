from distutils import extension
import os
from this import s
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
import random

from open_json import ler_config_json

simp_path = r'config\\config.json'
abs_path = os.path.abspath(simp_path)
config = ler_config_json(abs_path)
ptions = webdriver.ChromeOptions()
ptions.add_argument(
    f'user-agent={config["navegador"]["user_agent_fixo_mobile"]}')
driver = webdriver.Chrome(
    executable_path=r'./chromedriver.exe', options=ptions)
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
driver.get('https://www.instagram.com/srpedrolucasdaconceicao67/')
json_code = driver.execute_script("return window._sharedData")
