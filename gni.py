from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# atualizacao efetuada
# atualizacao efetuada


def veryGni():
    click = 0
    firefox_options = webdriver.EdgeOptions()
    firefox_options.add_argument(
        "--disable-blink-features=AutomationControlled")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument('--disable-extensions')
    firefox_options.add_argument('--profile-directory=Default')
    prefs = {"profile.managed_default_content_settings.images": 2}
    firefox_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Edge(
        executable_path=r'./msedgedriver.exe', options=firefox_options)
    driver.get('https://www.ganharnoinsta.com/painel/?pagina=logout')
    awit = driver.implicitly_wait(15)
    awit
    sleep(2)
    while True:
        print('logue e entre no gerenciador de contas')
        sleep(5)
        if driver.current_url == 'https://www.ganharnoinsta.com/painel/?pagina=gerenciar_contas':
            break
    print('verificando contas')
    sleep(1)
    very = ''
    while True:
        try:
            driver.get(
                'https://www.ganharnoinsta.com/painel/?pagina=gerenciar_contas')
            awit
            very = driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div/div[3]/div[2]/div/table/tbody/tr[1]/td[4]/a[1]').text
            if very == 'Arquivar Conta':
                print(very)
                driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div/div[3]/div[2]/div/table/tbody/tr[1]/td[4]/a[1]').click()
                click = 1
                driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div/div[3]/table/tbody/tr/td[4]/a').click()
                click = 1
                driver.get(
                    'https://www.ganharnoinsta.com/painel/?pagina=gerenciar_contas')
                driver.implicitly_wait(10)
            elif very == 'Histórico de Descontos':
                print(very)
                if click == 0:
                    try:
                        driver.find_element_by_xpath(
                            '//*[@id="tableGerenciarContasInstagram"]/tbody/tr[1]/td[4]/a[3]').click()
                        click = 1
                    except:
                        pass

                elif click == 1:
                    driver.find_element_by_xpath(
                        '//*[@id="tableGerenciarContasInstagram"]/tbody/tr[1]/td[4]/a[3]').click()
                elif click == 2:
                    driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div/div/div[3]/div[2]/div/table/tbody/tr[1]/td[4]/a[3]').click()

                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                buttons = driver.find_elements_by_xpath(
                    "//*[contains(text(), 'Confirmar Exclusão')]")
                for btn in buttons:
                    btn.click()
                driver.find_element_by_xpath(
                    '//*[@id="main-wrapper"]/div/div/div/div/ul/form/input[1]').click()
                driver.find_element_by_xpath(
                    '//*[@id="main-wrapper"]/div/div/div/div/ul/form/input[2]').click()
                driver.find_element_by_xpath(
                    '//*[@id="main-wrapper"]/div/div/div/div/ul/form/button').click()
                driver.close()
                window_after = driver.window_handles[0]
                driver.switch_to.window(window_after)
            else:
                driver.close()
                break
        except:
            driver.refresh()
            click = 0


veryGni()
