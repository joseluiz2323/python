from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def abrirNavegador():
    options = selenium.webdriver.ChromeOptions()
    options.add_argument(
        "--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    driver = selenium.webdriver.Chrome(
        executable_path=r'./chromedriver.exe', options=options)
    driver.get('https://www.mohmal.com/pt/inbox')
    sleep(1)
    codigo = driver.find_element_by_xpath(
        '//*[@id="email_content"]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody')
    print(codigo.text)


abrirNavegador()
