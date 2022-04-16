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
from credentialss import getvalueFirebase, setvalorFirebase
from gravar_logs import criacao_de_logo, logs
from limpar_historico import limparlogins
from open_json import ler_config_json


chrome_service = ChromeService('./chromedriver.exe')
chrome_service.creationflags = CREATE_NO_WINDOW
######


def capCodEmail(email, num, criacao_de_logo):
    ######
    criacao_de_logo(num, 'esperando codigo')
    count = 0
    while True:
        count += 1
        try:
            sleep(4)
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


def selecionarlistadefotos(config):
    fotos = []
    pastas = []

    simp_path = r'fotos'
    abs_path = os.path.abspath(simp_path)
    if config['criacao']['genero'] == 'F':
        count = 0
        abs_path = abs_path+"\\femenino"
        for diretorio, subpastas, arquivos in os.walk(abs_path):
            count += 1
            pastas.append(subpastas)
        pasta = f'{abs_path}\\{pastas[0][random.randint(0, len(pastas[0])-1)]}'
        for arquivo in os.walk(pasta):
            if arquivo[-4:] == '.jpg' or '.png' or '.jpeg':
                fotos.append(arquivo)
    else:
        count = 0
        abs_path = abs_path+"\\masculino"
        for diretorio, subpastas, arquivos in os.walk(abs_path):
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
            driver.implicitly_wait(10)
            print(driver.title)
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


def montador(config, user, senh):
    very = 0
    try:
        options = webdriver.ChromeOptions()
        if config["navegador"]["ocultar_navegador"]:
            options.add_argument("--headless")
        if config['navegador']['user_agent_aleatorio_mobile']:
            simp_path = r'config\\useragents_mobile.txt'
            abs_path = os.path.abspath(simp_path)
            with open(abs_path) as f:
                usermobi = [line.strip() for line in f if line.strip()]
            useragents = random.choice(usermobi)
            mobile_emulation = {"deviceMetrics": {
                "pixelRatio": 4.0}, "userAgent": useragents}
            options.add_experimental_option(
                "mobileEmulation", mobile_emulation)
        else:
            options.add_argument(
                f'user-agent={config["navegador"]["user_agent_fixo_mobile"]}')
        if config['navegador']['navegador_anonimo']:
            options.add_argument('--incognito')
        options.add_argument("--window-size=640,920")
        options.creationflags = CREATE_NO_WINDOW
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
        # foto de perfil
        bio = 0
        if config['montagem']['alterar_foto_de_perfil']:
            bio = 1
            driver.get('https://www.instagram.com/accounts/edit/')
            driver.implicitly_wait(10)
            fotos, pasta = selecionarlistadefotos(config)

            try:
                driver.find_element_by_class_name('tb_sK').send_keys(
                    f'{pasta}\\{random.choice(fotos)}')
                sleep(2)
                driver.find_element_by_class_name('UP43G').click()
            except:
                pass
            sleep(3)
        # selecionar bio
        if config['montagem']['bioaleatoria']:
            ###########
            simp_path = r'config\\bio.txt'
            abs_path = os.path.abspath(simp_path)
            lista = []
            with open(abs_path, encoding='utf8') as infile:
                for i in infile.read().splitlines():
                    lista.append(i)
            bio = str(random.choice(lista))

            driver.get('https://www.instagram.com/accounts/edit/')
            driver.implicitly_wait(10)
            sleep(1)
            driver.find_element_by_class_name('p7vTm').send_keys(bio)
            sleep(2)
            try:
                buttons = driver.find_elements_by_xpath(
                    "//*[contains(text(), 'Enviar')]")
                for btn in buttons:
                    btn.click()
            except:
                try:
                    button = driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/article/form/div[10]/div/div/button')
                    driver.execute_script("arguments[0].click();", button)
                except:
                    try:
                        button = driver.find_element_by_xpath(
                            '/html/body/div[1]/section/main/div/article/form/div[10]/div/div/button')
                        driver.execute_script("arguments[0].click();", button)
                    except:
                        pass
        sleep(2)
        c = 0
        simp_path = r'config\\legendas.txt'
        abs_path = os.path.abspath(simp_path)
        lista = []
        with open(abs_path, encoding='utf8') as infile:
            for i in infile.read().splitlines():
                lista.append(i)
        while True:
            c += 1
            try:
                if c == config['montagem']['qauntidade_de_fotos']:
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
                fotoss = random.choice(fotos)
                fotos.remove(fotoss)
                driver.find_element_by_class_name('tb_sK').send_keys(
                    f'{pasta}\\{fotoss}')
                sleep(5)
                driver.find_element_by_class_name('UP43G').click()
                sleep(2)
                if config['montagem']['legenda']:
                    legenda =str( random.choice(lista))
                    try:
                            driver.find_element_by_class_name(
                            '_472V_').send_keys(legenda)
                            sleep(2)
                    except:
                        driver.find_element_by_class_name(
                            '_472V_').send_keys(' ')
                driver.find_element_by_class_name('UP43G').click()
            except:
                very += 1
                if very == 4:
                    break
            
                try:
                    driver.find_element_by_class_name('cB_4K  ').click()
                except:
                    pass
                # escolher um tempo aleatorio
            sleep(random.randint(
                config['montagem']['tempo_entre_postagem']['inicial'], config['montagem']['tempo_entre_postagem']['final']))
        # limpeza de login
        if config['montagem']['verificar_postagens']:
            json_code = driver.execute_script("return window._sharedData")
            qtd_post = json_code['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']
            if config['montagem']['qauntidade_de_fotos'] == qtd_post:
                try:
                    simp_path = r'relatorio_de_contas\\contas-ativas-completas.txt'
                    abs_path = os.path.abspath(simp_path)
                    nome_arquivo = abs_path
                    arquivo = open(nome_arquivo, 'r+')
                except FileNotFoundError:
                    arquivo = open(nome_arquivo, 'w+')
                arquivo.close()
                f = open(abs_path, 'r')
                conteudo = f.readlines()
                conteudo.append(f'\n{user} {senh}')
                f2 = open(abs_path, 'w')
                f2.writelines(conteudo)
                f2 = open(abs_path)
                arquivo.close()
            else:
                try:
                    simp_path = r'relatorio_de_contas\\contas-ativas-incompletas.txt'
                    abs_path = os.path.abspath(simp_path)
                    nome_arquivo = abs_path
                    arquivo = open(nome_arquivo, 'r+')
                except FileNotFoundError:
                    arquivo = open(nome_arquivo, 'w+')
                arquivo.close()
                f = open(abs_path, 'r')
                conteudo = f.readlines()
                conteudo.append(f'\n{user} {senh}')
                f2 = open(abs_path, 'w')
                f2.writelines(conteudo)
                f2 = open(abs_path)
                arquivo.close()
        if config['montagem']['limpar_login']:
            limparlogins(driver)
        driver.quit()
    except:
        driver.quit()
    try:
        simp_path = r'relatorio_de_contas\\contas-ativas-incompletas.txt'
        abs_path = os.path.abspath(simp_path)
        nome_arquivo = abs_path
        arquivo = open(nome_arquivo, 'r+')
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
    arquivo.close()
    f = open(abs_path, 'r')
    conteudo = f.readlines()
    conteudo.append(f'\n{user} {senh}')
    f2 = open(abs_path, 'w')
    f2.writelines(conteudo)
    f2 = open(abs_path)
    arquivo.close()


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
        # try:

        options = webdriver.ChromeOptions()
        ################################
        #   congifuração do navgador   #
        ################################

        options.add_argument(
            "--disable-blink-features=AutomationControlled")
        options.add_argument('--no-sandbox')
        if config["navegador"]["navegador_anonimo"]:
            options.add_argument('--incognito')
        options.add_argument('--disable-extensions')
        if config["navegador"]["ocultar_navegador"]:
            options.add_argument("--headless")
        options.add_argument('--profile-directory=Default')
        options.add_argument('--window-size=540,920')
        if config["navegador"]["desativar_imagens"]:
            prefs = {"profile.managed_default_content_settings.images": 2}
        if config["navegador"]["user_agent_aleatorio_desktop"]:
            simp_path = r'config\\useragents_desktop.txt'
            abs_path = os.path.abspath(simp_path)
            with open(abs_path) as f:
                usermobi = [line.strip() for line in f if line.strip()]
            useragents = random.choice(usermobi)
            options.add_argument(
                f"user-agent={useragents}")
        else:
            options.add_argument(
                f"user-agent={config['navegador']['user_agent_fixo_desktop']}")
        #############################################
        options.add_argument("--lang=pt-br")
        options.add_experimental_option("prefs", prefs)
        options.creationflags = CREATE_NO_WINDOW
        chrome_service = ChromeService(r'./chromedriver.exe')
        chrome_service.creationflags = CREATE_NO_WINDOW
        driver = webdriver.Chrome(
            options=options, service=chrome_service)
        daley = driver.implicitly_wait(15)
        driver.get('https://www.instagram.com/accounts/emailsignup/')
        if driver.title == 'Página não encontrada • Instagram':
            driver.quit()
            criacao_de_logo(numero_do_log, 'Instagram Bloqueou a pagina')
            sleep(2)
            criacao_de_logo(numero_do_log, 'Esperando 10 segundos')
            sleep(8)
        else:
            daley
            ##############
            # verificando se entrou no site
            ##############

            try:
                driver.find_element_by_xpath(
                    '/html/body/div[4]/div/div/button[1]').click()
                sleep(0.5)
            except Exception as e:
                pass
            ######
            # selecionando nome para o usuario
            pastanomes = r'config'
            abs_path = os.path.abspath(pastanomes)
            if config['criacao']['genero'] == 'F':
                with open(abs_path+"\\nomes_f.txt") as f:
                    nome = [line.strip() for line in f if line.strip()]
                nome = random.choice(nome)
                with open(abs_path+"\\sobrenomes.txt") as f:
                    sobrenome = [line.strip() for line in f if line.strip()]
                sobrenome = random.choice(sobrenome)
            criacao_de_logo(numero_do_log, f'Nome gerado {nome} {sobrenome}')
            if config['criacao']['genero'] == 'M':
                with open(abs_path+"\\nomes_m.txt") as f:
                    nome = [line.strip() for line in f if line.strip()]
                nome = random.choice(nome)
                with open(abs_path+"\\sobrenomes.txt") as f:
                    sobrenome = [line.strip() for line in f if line.strip()]
                sobrenome = random.choice(sobrenome)
            nome = nome + ' ' + sobrenome
            #######
            # selecionando email
            if config["email"]["layonsemail"]:
                emailroba = '@lyonsbot.com.br'
                criacao_de_logo(numero_do_log, 'Gerando email')
                email = f"{random.randint(10, 99)}{nome.replace(' ', '')[0:9]}{random.randint(100, 999)}"
                email2 = email+emailroba
            elif config["email"]["fakemail"]:
                email2 = capCodEmailfake(driver, 1)
            driver.find_element_by_name(
                'emailOrPhone').send_keys(email2)
            driver.find_element_by_name(
                'fullName').send_keys(nome)
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
                daley
                senha = config["criacao"]["senha"]
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
                if config["email"]["layonsemail"]:
                    codigoEmail = capCodEmail(
                        email, numero_do_log, criacao_de_logo)
                    if codigoEmail == '':
                        sleep(5)
                        codigoEmail = (
                            email, numero_do_log, criacao_de_logo)
                    driver.implicitly_wait(10)
                    sleep(2)
                    if codigoEmail == 0:
                        driver.quit()
                elif config["email"]["fakemail"]:
                    codigoEmail = capCodEmailfake(driver, 20)
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
                    try:
                        driver.find_element_by_xpath(
                            '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button').click()
                    except:
                        try:
                            driver.find_element_by_xpath(
                                '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]').click()
                        except:
                            pass
                sleep(10)
                try:
                    button.click()
                except:
                    pass
                if driver.title == 'Entrar • Instagram':
                    try:
                        driver.get(
                            'https://www.instagram.com/accounts/login')
                        driver.implicitly_wait(10)
                        driver.find_element_by_name(
                            'username').send_keys(email2)
                        driver.find_element_by_name(
                            'password').send_keys(senha)
                        driver.find_element_by_name('password').click()
                        driver.find_element_by_name(
                            'password').send_keys(Keys.ENTER)
                        sleep(5)
                    except:
                        pass
                driver.get('https://www.instagram.com/accounts/edit/')
                driver.implicitly_wait(10)
                sleep(1)
                nomeUser = ''
                json_code = driver.execute_script("return window._sharedData")
                # pegar usernome json_code
                nomeUser = json_code['config']['viewer']['username']
                if nomeUser == '':
                    try:
                        nomeUser = driver.find_element_by_xpath(
                            '//*[@id="react-root"]/section/main/div/article/div/div[2]/h1').text
                    except:
                        pass
                if taxa == 5:
                    driver.quit()
                    setvalorFirebase(nomeUser + ' ' + senha)
                    taxa = 0
                    if config["montagem"]["mont"]:
                        montador(config, nomeUser, senha)
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
                    if config["montagem"]["mont"]:
                        montador(config, nomeUser, senha)

            else:
                driver.quit()
            # except:
            #     driver.quit()


simp_path = r'config\\config.json'
abs_path = os.path.abspath(simp_path)
config = ler_config_json(abs_path)

criacao(config)
