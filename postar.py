import os
from time import sleep
from tkinter.tix import Tree
from pyparsing import autoname_elements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import random
import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW
from fake_useragent import UserAgent
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random


def selecionarlistadefotos():
    fotos = []
    pastas = []

    simp_path = r'fotos'
    abs_path = os.path.abspath(simp_path)

    count = 0
    print(abs_path)
    for diretorio, subpastas, arquivos in os.walk(''+abs_path+''):
        count += 1
        pastas.append(subpastas)
    pasta = f'{abs_path}\\{pastas[0][random.randint(0, len(pastas[0])-1)]}'
    for arquivo in os.walk(pasta):
        if arquivo[-4:] == '.jpg' or '.png' or '.jpeg':
            fotos.append(arquivo)
    return fotos[0][2], pasta


def montador(user, senh):
    try:
        options = webdriver.ChromeOptions()
        with open(r'useragents_mobile.txt') as f:
            usermobi = [line.strip() for line in f if line.strip()]
        useragents = random.choice(usermobi)
        mobile_emulation = {"deviceMetrics": {
            "pixelRatio": 4.0}, "userAgent": useragents}
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument('--incognito')
        options.add_argument("--window-size=640,920")
        driver = webdriver.Chrome(
            executable_path=r'chromedriver.exe', options=options
        )
        driver.get('https://www.instagram.com/accounts/login/?next=/login/')
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_class_name(
                'cB_4K  ').click()
            sleep(4)
        except:
            pass
        driver.find_element_by_name('username').send_keys(user)
        sleep(0.1)
        driver.find_element_by_name('password').send_keys(senh)
        sleep(0.1)
        driver.find_element_by_name('password').click()
        driver.find_element_by_name('password').send_keys(Keys.ENTER)
        sleep(10)
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
        sleep(2)
        c = 0
        while True:
            c += 1
            try:
                if c == 12:
                    break
                driver.get(f'https://www.instagram.com/{user}/')
                driver.implicitly_wait(10)
                driver.execute_script(
                    "HTMLInputElement.prototype.click = function() {                     " +
                    "  if(this.type !== 'file') HTMLElement.prototype.click.call(this);  " +
                    "};                                                                  ")
                try:
                    driver.find_element_by_xpath(
                        '//div[@data-testid="new-post-button"]').click()
                except:
                    driver.find_element_by_xpath(
                        "//div[@data-testid='new-post-button']/*[name()='svg']").click()

                driver.execute_script(
                    "delete HTMLInputElement.prototype.click")
                driver.implicitly_wait(10)
                driver.find_element_by_class_name('tb_sK').send_keys(
                    f'{pasta}\\{random.choice(fotos)}')
                sleep(5)
                driver.find_element_by_class_name('UP43G').click()
                sleep(5)
                driver.find_element_by_class_name('UP43G').click()
            except:
                print('erro')
                try:
                    driver.find_element_by_class_name('cB_4K  ').click()
                except:
                    pass
            sleep(5)
        dados = driver.find_element_by_class_name(
            '_7UhW9   xLCgt      MMzan    _0PwGv         uL8Hv     l4b0S   T0kll ').text
        print(dados)
        driver.quit()
    except:
        driver.quit()


contas = '''anaclaranascimento5679 gen1122
gustavomartins4131 gen1122
nicoleteixeira519 gen1122
vitornascimento8370 gen1122
valentinadaconceicao987 gen1122
srmatheuscampos7 gen1122
srtaisabelmelo4 gen1122
viniciuspinto278 gen1122
sryuridacunha7 gen1122
clarasantos4662 gen1122'''

# percorrer uma string contas
for conta in contas.split('\n'):
    usuario = conta.split(' ')[0]
    senha = conta.split(' ')[1]
    print(f'{usuario} - {senha}')
    montador(usuario, senha)
