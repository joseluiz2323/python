from calendar import c
from cgitb import handler, text
import random
import re
from time import sleep
import requests
from datetime import datetime
from fake_useragent import UserAgent

XInstagramAJAX = csrftoken = ds_user_id = sessionid = ig_did = mid = ig_nrcb = shbid = shbts = rur = XIGWWWClaim = False

#jose
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


def very(lista, csrftoken, ds_user_id, sessionid,
         ig_did, mid, ig_nrcb, rur, user_agent):
    contas = lista.splitlines()
    cont = 0
    sms = 0
    ativas = 0
    completas = 0
    incompletas = 0
    lins = []
    print(len(contas))
    for conta in contas:
        cont += 1
        sleep(random.randint(0, 1))
        try:
            conta = conta.split()
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
            print(f'{cont} {conta[0]} conta com verificacao')
            sms += 1
            pass
        lins.clear()
    return completas, incompletas, cont, sms


lista = """"mariaalicesouza9867 gen1122
luizfelipedias782 gen1122
mariaclaracostela670 gen1122
sabrinadasneves401 gen1122
srtaemanuellydaluz91 gen1122
pietrafarias928 gen1122
brenoalmeida6076 gen1122
emanuellaferreira198 gen1122
anajuliamendes9203 gen1122
rafaeladacosta464 gen1122
neilan.froylan9 gen1122
srcaiodaconceicao769 gen1122
marcosviniciusdacunha78 gen1122
cauaferreira6082 gen1122
julianacostela12 gen1122
joaolucasfarias838 gen1122
mariaceciliaporto54 gen1122
isadorarezende9232 gen1122
marcosviniciusnascimento410 gen1122
srdanilopinto43 gen1122
luizfelipedias720 gen1122
amandaramos7488 gen1122
srheitorrodrigues74 gen1122
isadorarezende3686 gen1122
mariaalicefarias311 gen1122
srheitorrodrigues56 gen1122
anajuliacavalcanti5316 gen1122
joaomiguelbarros9718 gen1122
juliabarbosa1364 gen1122
noahsantos2974 gen1122
franciscoribeiro240 gen1122
srheitorrodrigues47 gen1122
pietrocampos667 gen1122
theodasneves44 gen1122
marcosviniciusnascimento9015 gen1122
pedrohenriquedapaz95 gen1122
samueldias2719 gen1122
drmarcelopires98 gen1122
pietrafarias659 gen1122
sryuriramos56 gen1122
otaviosales315 gen1122
drfernandocunha97 gen1122
brenoalmeida930 gen1122
anabeatrizduarte5959 gen1122
benjaminlopes139 gen1122
emanuellaferreira385 gen1122
anajuliacavalcanti915 gen1122
analuizacunha694 gen1122
pietrafarias922 gen1122
analuizacunha532 gen1122
drlucasfernandes596 gen1122
isabellysantos428 gen1122
yasminrodrigues8061 gen1122
rafaelamoura9078 gen1122
mariaclaracostela49 gen1122
kaiquemartins9185 gen1122
joaomiguelbarros95 gen1122
luizfernandopinto809 gen1122
paulovieira3878 gen1122
gustavocarvalho572 gen1122
laviniasouza974 gen1122
eero.zidaan5 gen1122
gabriellydacruz14 gen1122
eloahferreira5989 gen1122
migueldacruz393 gen1122
srcaiodaconceicao95 gen1122
juliaviana7250 gen1122
marcelodias763 gen1122
gustavocarvalho224 gen1122
caiodaconceicao647 gen1122
juliabarbosa7522 gen1122
joaovitorporto75 gen1122
yasminrodrigues7320 gen1122
camiladarosa75 gen1122
theodasneves30 gen1122
srtaamandabarros16 gen1122
mariaceciliaporto164 gen1122
srrodrigopires16 gen1122
rafaeladacosta206 gen1122
pietrafarias1952 gen1122
drgustavomendes739 gen1122
isaacvieira994 gen1122
yasminrodrigues7816 gen1122
marcosviniciusdacunha74 gen1122
drfernandocunha74 gen1122
samueldias800 gen1122
joaolucasfarias631 gen1122
sabrinadasneves159 gen1122
laviniasouza118 gen1122
juliaviana5178 gen1122
bryanaraujo1027 gen1122
caiofogaca63 gen1122
srpedrolucasdaconceicao17 gen1122
yasminrodrigues2989 gen1122
luizfelipedias7463 gen1122
analuizamelo701 gen1122
paulovieira143 gen1122
yasminrodrigues8338 gen1122
anabeatrizviana7437 gen1122
srheitorrodrigues42 gen1122
draalicemelo965 gen1122
alexiamonteiro2990 gen1122
"""
ua = UserAgent()
user_agent = ua.random

while True:
    csrftoken, ds_user_id, sessionid, ig_did, mid, ig_nrcb, rur = sessionData(
        lista, user_agent)
    if sessionid != False:
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
