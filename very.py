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


lista = """"eloahferreira5989 gen1122
srcaiodaconceicao95 gen1122
marcelodias763 gen1122
caiodaconceicao647 gen1122
joaovitorporto75 gen1122
yasminrodrigues7320 gen1122
theodasneves30 gen1122
mariaceciliaporto164 gen1122
pietrafarias1952 gen1122
drgustavomendes739 gen1122
isaacvieira994 gen1122
marcosviniciusdacunha74 gen1122
samueldias800 gen1122
joaolucasfarias631 gen1122
laviniasouza118 gen1122
juliaviana5178 gen1122
caiofogaca63 gen1122
yasminrodrigues2989 gen1122
luizfelipedias7463 gen1122
analuizamelo701 gen1122
paulovieira143 gen1122
draalicemelo965 gen1122
analuizacunha677 gen1122
analuizacunha28 gen1122
srrodrigopires251 gen1122
srfernandoalmeida11 gen1122
mariafernandapinto5947 gen1122
drfernandocunha180 gen1122
caiodaconceicao801 gen1122
oliviarezende174 gen1122
yasminrodrigues220 gen1122
enzogabrieldacosta63 gen1122
yagoduarte9067 gen1122
anabeatrizduarte139 gen1122
elisasilva5164 gen1122
oliviarezende7520 gen1122
elisasilva1336 gen1122
samueldias617 gen1122
srdanilopinto820 gen1122
anacarolinaribeiro7489 gen1122
camiladarosa118 gen1122
raquelporto629 gen1122
pedrohenriquedapaz248 gen1122
srtaamandabarros96 gen1122
camilasouza4147 gen1122
andrez.ezrael2 gen1122
srdanilopinto8922 gen1122
gabriellydacruz932 gen1122
luizgustavolopes72 gen1122
draalicemelo95 gen1122
rafaelamoura7749 gen1122
mariaalicefarias468 gen1122
noahsantos8076 gen1122
anacarolinaribeiro8824 gen1122
anabeatrizduarte944 gen1122
joaomiguelbarros309 gen1122
joaolucasfarias22 gen1122
marcosviniciusnascimento724 gen1122
yagoduarte301 gen1122
draalicemelo1060 gen1122
pedrohenriquemoraes7534 gen1122
tavares.naheem1 gen1122
benjaminlopes7487 gen1122
oliviarezende854 gen1122
luizacampos1636 gen1122
mariaalicefarias126 gen1122
drfernandocunha63 gen1122
srheitorrodrigues90 gen1122
joaofelipesilva679 gen1122
enzogabrieldacosta52 gen1122
joaovitorporto47 gen1122
alexiamonteiro3074 gen1122
drmarcelopires54 gen1122
isabellysantos7677 gen1122
srcaiodaconceicao20 gen1122
isabelgomes5540 gen1122
camilasouza9667 gen1122
rafaelamoura8284 gen1122
yasminrodrigues579 gen1122
anabeatrizduarte4521 gen1122
elisasilva5431 gen1122
anabeatrizduarte647 gen1122
marinavieira8177 gen1122
marcelodias1779 gen1122
drmarcelopires88 gen1122
julianacostela913 gen1122
srrodrigopires23 gen1122
luanacosta1642 gen1122
yagoduarte927 gen1122
benjaminlopes717 gen1122
mariaalicesouza498 gen1122
migueldacruz706 gen1122
marcosviniciusdacunha83 gen1122
pietrocampos9754 gen1122
benjaminlopes555 gen1122
luizgustavolopes877 gen1122
alexiamonteiro8145 gen1122
yasminrodrigues5002 gen1122
mariafernandapinto3835 gen1122
caiofogaca405 gen1122
paulovieira9460 gen1122
olliver.shaul1 gen1122
gabriellydacruz881 gen1122
srheitorrodrigues67 gen1122
marcosviniciusdacunha34 gen1122
theodasneves781 gen1122
mariaclaracostela201 gen1122
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
