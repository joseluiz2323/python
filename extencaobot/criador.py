from distutils import extension
import os
from time import sleep
from tkinter.tix import Tree
from pyparsing import autoname_elements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import random
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW

from credentialss import getvalueFirebase, setvalorFirebase
from gravar_logs import criacao_de_logo, logs


chrome_service = ChromeService('./chromedriver.exe')
chrome_service.creationflags = CREATE_NO_WINDOW


def capCodEmail(email, num, criacao_de_logo):
    ######
    criacao_de_logo(num, 'esperando codigo')
    count = 0
    while True:
        count += 1
        try:
            sleep(4)
            print(count)
            if count == 10:
                return 0
            response = requests.get(
                f'https://lyonsbot.com.br/api/messages/{email}/yvEW5xKHliptoAeY3LZw')
            codigodados = response.json()
            try:
                if codigodados[0]['sender_name'] == 'Instagram':
                    criacao_de_logo(num, 'codigo recebido')
                    criacao_de_logo(num, codigodados[0]['subject'].split()[0])
                    return codigodados[0]['subject'].split()[0]
            except:
                pass
        except:
            pass


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


def capCodEmailfake(driver, temp):
    try:
        email = ''
        codigoinsta = 0
        if temp == 1:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get('https://www.fakemail.net/')
            email = driver.find_element_by_class_name('animace').text
            driver.switch_to.window(driver.window_handles[0])
        else:
            driver.switch_to.window(driver.window_handles[1])
            count = 0
            while True:
                count += 1
                if count == temp:
                    break
                sleep(1.5)
                codigo = driver.find_element_by_id('schranka').text
                codigo = codigo.split()
                if codigo[0] == '"Instagram"':
                    codigoinsta = codigo[1]
                if codigoinsta != 0:
                    driver.close()
                    break
                driver.refresh()
            driver.switch_to.window(driver.window_handles[0])

        if codigoinsta != 0:
            return codigoinsta
        elif email != '':
            return email
    except:
        return 0


def montador(user, senh):
    try:
        options = webdriver.ChromeOptions()
        simp_path = r'config\\useragents_mobile.txt'
        abs_path = os.path.abspath(simp_path)
        with open(abs_path) as f:
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


def criacao(config):
    numero_do_log = logs()
    bre = 0
    taxa = 0
    while True:
        criacao_de_logo(numero_do_log, 'Criacao iniciada')
        bre += 1
        if bre == 500:
            if getvalueFirebase() != 1:
                break
        try:
            senha = config[5].split('=')[1].replace(' ', '')
            firefox_options = webdriver.ChromeOptions()
            firefox_options.add_argument(
                "--disable-blink-features=AutomationControlled")
            firefox_options.add_argument('--no-sandbox')
            if config[2] == 'anonimo = 1':
                firefox_options.add_argument('--incognito')
            firefox_options.add_argument('--disable-extensions')
            firefox_options.add_argument('--profile-directory=Default')
            firefox_options.add_argument('--window-size=540,920')
            if config[3] == 'navsemimages = 1':
                prefs = {"profile.managed_default_content_settings.images": 2}
            simp_path = r'config\\useragents_desktop.txt'
            abs_path = os.path.abspath(simp_path)
            with open(abs_path) as f:
                usermobi = [line.strip() for line in f if line.strip()]
            useragents = random.choice(usermobi)
            firefox_options.add_argument(
                f"user-agent={useragents}")
            firefox_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(
                options=firefox_options)
            temp_page = driver.implicitly_wait(15)
            driver.get('https://www.instagram.com/accounts/emailsignup/')
            print(driver.title)
            temp_page
            ##############
            # verificando se entrou no site
            if driver.title == 'Página não encontrada • Instagram':
                driver.get('https://www.instagram.com/accou')
                print(driver.title)
                temp_page
                driver.get(
                    'https://www.instagram.com/accounts/emailsignup/')
                temp_page
            # clicando em cku
            try:
                driver.find_element_by_xpath(
                    '/html/body/div[4]/div/div/button[1]').click()
                sleep(0.5)
            except Exception as e:
                print(e)
            try:
                driver.find_element_by_class_name(
                    'cB_4K  ').click()
                sleep(4)
            except Exception as e:
                print(e)
            ######
            # selecionando nome para o usuario
            simp_path = r'config\\nomes.txt'
            abs_path = os.path.abspath(simp_path)
            criacao_de_logo(numero_do_log, 'Gerando nome')
            with open(abs_path) as f:
                nomess = [line.strip() for line in f if line.strip()]
            nomeSobrenome = random.choice(nomess)
            criacao_de_logo(numero_do_log, f'Nome gerado {nomeSobrenome}')
            #######
            # selecionando email
            if config[1] == 'email = 0':
                emailroba = '@lyonsbot.com.br'
                criacao_de_logo(numero_do_log, 'Gerando email')
                email = f"{random.randint(10, 99)}{nomeSobrenome.replace(' ', '')[0:9]}{random.randint(100, 999)}"
                email2 = email+emailroba

            elif config[0] == 'email = 0':
                email2 = capCodEmailfake(driver, 1)
            driver.find_element_by_name(
                'emailOrPhone').send_keys(email2)
            driver.find_element_by_name(
                'fullName').send_keys(nomeSobrenome)
            driver.find_element_by_name('username').send_keys()
            verycount = 0
            sleep(1)
            pont = 0
            while True:
                sleep(1)
                verycount += 1
                if verycount == 4:
                    break
                try:
                    driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button/span').click()
                    driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button/span').click()
                    pont = 1
                    break
                except:
                    try:
                        driver.find_element_by_xpath(
                            '//*[@id="react-root"]/div/div/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button/span').click()
                        driver.find_element_by_xpath(
                            '//*[@id="react-root"]/div/div/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button/span').click()
                        pont = 1
                        break
                    except:
                        pass
            try:
                driver.find_element_by_class_name('Szr5J').click()
                pont = 1
            except:
                pass
            if pont == 1:
                temp_page
                driver.find_element_by_name('password').send_keys(senha)
                sleep(1)
                driver.find_element_by_name('password').click()
                driver.find_element_by_name(
                    'password').send_keys(Keys.ENTER)
                sleep(4)

                try:
                    buttons = driver.find_elements_by_xpath(
                        f"//*[contains(text(), '{random.randint(1990, 2000)}')]")
                    for btn in buttons:
                        btn.click()
                except:
                    pass
                button = driver.find_elements_by_class_name(
                    'y3zKF')[1]
                button.click()
                criacao_de_logo(numero_do_log, 'Selecionado data de usuario')
                ################ ##############
                # verifica o email para confirmar o confirmacao do codigo de cadastro
                if config[1] == 'email = 0':
                    codigoEmail = capCodEmail(
                        email, numero_do_log, criacao_de_logo)
                    print(codigoEmail)
                    if codigoEmail == '':
                        sleep(5)
                        codigoEmail = (
                            email, numero_do_log, criacao_de_logo)
                    driver.implicitly_wait(10)
                    sleep(2)
                    if codigoEmail == 0:
                        driver.quit()
                elif config[0] == 'email = 1':
                    codigoEmail = capCodEmailfake(driver, 20)
                    print(codigoEmail)
                    if codigoEmail == 0:
                        sleep(5)
                        codigoEmail = capCodEmailfake(driver, 5)
                    driver.implicitly_wait(10)
                    sleep(2)
                    if codigoEmail == 0:
                        driver.quit()

                driver.implicitly_wait(10)
                sleep(2)
                driver.find_element_by_name(
                    'email_confirmation_code').click()
                driver.find_element_by_name(
                    'email_confirmation_code').send_keys(codigoEmail)
                sleep(0.2)
                button = driver.find_elements_by_class_name(
                    'y3zKF')[1]
                try:
                    button.click()
                except:
                    pass
                try:
                    driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button').click()
                except:
                    try:
                        driver.find_element_by_xpath(
                            '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]').click()
                    except:
                        pass
                sleep(17)
                try:
                    driver.get(
                        'https://www.instagram.com/accounts/login')
                    driver.implicitly_wait(20)
                    try:
                        driver.find_element_by_xpath(
                            '/html/body/div[4]/div/div/button[1]').click()
                    except:
                        pass
                    try:
                        driver.find_element_by_class_name(
                            'cB_4K  ').click()
                        sleep(4)
                    except:
                        pass
                    try:
                        driver.find_element_by_name(
                            'username').send_keys(email2)
                        driver.find_element_by_name(
                            'password').send_keys(senha)
                        driver.find_element_by_name('password').click()
                        driver.find_element_by_name(
                            'password').send_keys(Keys.ENTER)
                        sleep(8)
                    except:
                        pass
                except:
                    pass
                driver.get('https://www.instagram.com/accounts/edit/')
                driver.implicitly_wait(10)
                nomeUser = ''
                nomeUser = driver.find_element_by_class_name('kHYQv ').text
                if nomeUser == '':
                    try:
                        nomeUser = driver.find_element_by_xpath(
                            '//*[@id="react-root"]/section/main/div/article/div/div[2]/h1').text
                    except:
                        pass
                print('##############################')
                print('##############################')
                print('==============================')
                print(f'     {nomeUser}      ')
                print('==============================')
                print('##############################')
                print('##############################')
                if taxa == 5:
                    setvalorFirebase(nomeUser + ' ' + senha)
                    taxa = 0
                    montador(nomeUser, senha)
                else:
                    taxa += 1
                    try:
                        simp_path = r'relatorio_de_contas\\contas.txt'
                        abs_path = os.path.abspath(simp_path)
                        nome_arquivo = abs_path
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                    arquivo.close()
                    f = open(abs_path, 'r')
                    conteudo = f.readlines()
                    conteudo.append(f'\n{nomeUser} {senha}')
                    f2 = open(abs_path, 'w')
                    f2.writelines(conteudo)
                    f2 = open(abs_path, 'r')
                    arquivo.close()
                    try:
                        driver.quit()
                    except:
                        pass
                    montador(nomeUser, senha)
            else:
                driver.quit()
        except:
            driver.quit()


simp_path = r'config\\config.txt'
abs_path = os.path.abspath(simp_path)
with open(abs_path) as f:
    config = [line.strip() for line in f if line.strip()]


criacao(config)
