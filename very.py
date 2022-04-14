from calendar import c
from cgitb import handler, text
import random
import re
from time import sleep
import requests
from datetime import datetime
from fake_useragent import UserAgent

XInstagramAJAX = csrftoken = ds_user_id = sessionid = ig_did = mid = ig_nrcb = shbid = shbts = rur = XIGWWWClaim = False


def sessionData(lista, user_agent):
    contas = lista.splitlines()
    conta = random.choice(contas)
    conta = conta.split()
    print(conta)
    global XIGWWWClaim
    link = 'https://www.instagram.com/'
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    localtime = int(datetime.now().timestamp())
    payload = {
        'username': f'{conta[0]}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{localtime}:{conta[1]}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    with requests.Session() as s:
        r = s.get(link, headers={
            "User-Agent": f"{user_agent}",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/"})
        csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
        globals()['XInstagramAJAX'] = re.findall(
            r"rollout_hash\":\"(.*?)\"", r.text)[0]

        r = s.post(login_url, data=payload, headers={
            "User-Agent": f"{user_agent}",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "X-IG-WWW-Claim": '0',
            "x-csrftoken": csrf
        })
        global XIGWWWClaim
        XIGWWWClaim = r.headers['x-ig-set-www-claim']
        cookies = dict(r.cookies)
        res = [(k, v) for k, v in cookies.items()]
        for i in res:
            globals()[i[0]] = i[1]
        print(sessionid)
        return csrftoken, ds_user_id, sessionid, ig_did, mid, ig_nrcb, rur


def verificar(conta, csrftoken, ds_user_id, sessionid, ig_did, mid, ig_nrcb, rur, user_agent):

    url = f'https://www.instagram.com/{conta}/'

    handler = {
        'authority': 'www.instagram.com',
        'method': 'GET',
        'path': f'/{conta}/',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': f'mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb}; csrftoken={csrftoken}; ds_user_id={ds_user_id}; sessionid={sessionid}; rur={rur}',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': f"{user_agent}"
    }
    response = requests.get(url, headers=handler)

    return response

# funcao para retornar a data e hora atural


def very(lista, csrftoken, ds_user_id, sessionid,
         ig_did, mid, ig_nrcb, rur, user_agent):
    contas = lista.splitlines()
    contas.insert(0, '1 2')
    cont = 0
    sms = 0
    ativas = 0
    completas = 0
    incompletas = 0
    lins = []
    print(len(contas))
    for conta in contas:
        conta = conta.split()
        cont += 1
        # if cont == 1:
        #     conta[0] = 'data da verificacao'
        #     data = datetime.today().strftime('%H:%M:%S')
        #     conta[1] = f"{data}"
        #     try:
        #         nome_arquivo = 'contas-ativas-completas.txt'
        #         arquivo = open(nome_arquivo, 'r+')
        #     except FileNotFoundError:
        #         arquivo = open(nome_arquivo, 'w+')
        #     arquivo.close()
        #     f = open('contas-ativas-completas.txt', 'r')
        #     conteudo = f.readlines()
        #     conteudo.append(f'\n{conta[0]} {conta[1]}')
        #     f2 = open('contas-ativas-completas.txt', 'w')
        #     f2.writelines(conteudo)
        #     f2 = open('contas-ativas-completas.txt', 'r')
        #     f2.close()
        #     try:
        #         nome_arquivo = 'contas-ativas-incompletas.txt'
        #         arquivo = open(nome_arquivo, 'r+')
        #     except FileNotFoundError:
        #         arquivo = open(nome_arquivo, 'w+')
        #     arquivo.close()
        #     f = open('contas-ativas-incompletas.txt', 'r')
        #     conteudo = f.readlines()
        #     conteudo.append(f'\n{conta[0]} {conta[1]}')
        #     f2 = open('contas-ativas-incompletas.txt', 'w')
        #     f2.writelines(conteudo)
        #     f2 = open('contas-ativas-incompletas.txt', 'r')
        #     f2.close()

        sleep(random.randint(0, 1))
        try:
            dados = verificar(conta[0], csrftoken, ds_user_id, sessionid,
                              ig_did, mid, ig_nrcb, rur, user_agent)
            for j in dados.text.splitlines():
                lins.append(j)
            index = lins.index('<meta property="og:type" content="profile"/>')
            dados_final = lins[index+3].replace(
                '<meta property="og:description" content="', '').split()
            print(f'{cont} -- {conta[0]} publicações {dados_final[4]}')
            if (int(dados_final[4])) >= 5:
                completas += 1
                try:
                    nome_arquivo = 'contas-ativas-completas.txt'
                    arquivo = open(nome_arquivo, 'r+')
                except FileNotFoundError:
                    arquivo = open(nome_arquivo, 'w+')
                arquivo.close()
                f = open('contas-ativas-completas.txt', 'r')
                conteudo = f.readlines()
                conteudo.append(f'\n{conta[0]} {conta[1]}')
                f2 = open('contas-ativas-completas.txt', 'w')
                f2.writelines(conteudo)
                f2 = open('contas-ativas-completas.txt', 'r')
                f2.close()
            else:
                incompletas += 1
                try:
                    nome_arquivo = 'contas-ativas-incompletas.txt'
                    arquivo = open(nome_arquivo, 'r+')
                except FileNotFoundError:
                    arquivo = open(nome_arquivo, 'w+')
                arquivo.close()
                f = open('contas-ativas-incompletas.txt', 'r')
                conteudo = f.readlines()
                conteudo.append(f'\n{conta[0]} {conta[1]}')
                f2 = open('contas-ativas-incompletas.txt', 'w')
                f2.writelines(conteudo)
                f2 = open('contas-ativas-incompletas.txt', 'r')
                f2.close()
        except:
            if cont == 1:
                print(f'{cont-1} {conta[0]} {conta[1]} ')
            else:
                print(f'{cont} {conta[0]} conta com verificacao')
            sms += 1
            pass
        lins.clear()
    return completas, incompletas, cont, sms


lista = """"
"""
ua = UserAgent()
user_agent = ua.random

while True:
    csrftoken, ds_user_id, sessionid, ig_did, mid, ig_nrcb, rur = sessionData(
        lista, user_agent)
    if sessionid != False:
        pass
        break

if sessionid != False:
    print('logado com sucesso')
    completas, incompletas, cont, sms = very(
        lista, csrftoken, ds_user_id, sessionid, ig_did, mid, ig_nrcb, rur, user_agent)
try:
    print('contas verificadas')
    print(cont)
    print('contas completas')
    print(completas)
    print('contas incompletas')
    print(incompletas)
    print('contas com verificacao')
    print(sms)
except:
    print('conta com verificacao')
