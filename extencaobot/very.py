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


lista = """"olliver.shaul1 gen1122
gabriellydacruz881 gen1122
theodasneves781 gen1122
mariaclaracostela201 gen1122
draalicemelo83 gen1122
kermit.adeel1 gen1122
marinavieira475 gen1122
isadorarezende5755 gen1122
kaiquebarbosa1688 gen1122
luizacampos7825 gen1122
camilasouza4993 gen1122
joaopedroalves573 gen1122
pedrohenriquecarvalho549 gen1122
eduardamonteiro8044 gen1122
srtaamandabarros43 gen1122
anabeatrizviana174 gen1122
anajuliacavalcanti177 gen1122
samueldias8689 gen1122
srpedrolucasdaconceicao67 gen1122
davimoreira1805 gen1122
drfernandocunha36 gen1122
isabelgomes8472 gen1122
srtaemanuellydaluz88 gen1122
estherviana3026 gen1122
caiofogaca81 gen1122
luizacampos7817 gen1122
mariaceciliaporto582 gen1122
anaclarasilva3284 gen1122
marcosviniciusnascimento3190 gen1122
srcaiodaconceicao992 gen1122
mariaclaracostela96 gen1122
anabeatrizduarte1671 gen1122
isabellysantos9945 gen1122
estherviana2588 gen1122
isadorafarias9211 gen1122
mariaalicesouza707 gen1122
mariafernandapinto615 gen1122
pedrohenriquedapaz926 gen1122
isabellysantos9919 gen1122
guilhermedasneves21 gen1122
anabeatrizviana22 gen1122
mariaalicesouza8308 gen1122
srdanilopinto18 gen1122
sabrinadasneves808 gen1122
drfernandocunha87 gen1122
mariaceciliaporto537 gen1122
anabeatrizduarte4186 gen1122
luizgustavolopes158 gen1122
julianacostela478 gen1122
joaolucasfarias246 gen1122
srheitorrodrigues23 gen1122
mariaceciliaporto934 gen1122
juliaviana7860 gen1122
luizgustavolopes698 gen1122
theodasneves999 gen1122
mariaalicesouza1186 gen1122
marcosviniciusnascimento29 gen1122
brenoalmeida8194 gen1122
pietrafogaca3456 gen1122
marcosviniciusdacunha47 gen1122
obsa.kaedin2 gen1122
joaquimsouza803 gen1122
marinavieira6225 gen1122
sryuriramos3 gen1122
isaacvieira4123 gen1122
drlucasfernandes35 gen1122
analuizamelo375 gen1122
marcosviniciusnascimento311 gen1122
julianacostela93 gen1122
benjaminlopes520 gen1122
analuizacunha8674 gen1122
brenoalmeida9921 gen1122
rafaelporto9940 gen1122
ross.lajuan1 gen1122
anajuliacavalcanti4350 gen1122
drfernandocunha25 gen1122
luizgustavolopes414 gen1122
srtaamandabarros30 gen1122
anabeatrizduarte930 gen1122
drgustavomendes158 gen1122
luizgustavolopes151 gen1122
anajuliamendes7919 gen1122
yagoduarte1542 gen1122
luanacosta9089 gen1122
alexiamonteiro8969 gen1122
marcosviniciusdacunha6463 gen1122
anacarolinaribeiro8113 gen1122
marcelodias9810 gen1122
analuizacunha18 gen1122
joaofelipesilva231 gen1122
nataliadasneves35 gen1122
emanuellaferreira6565 gen1122
eduardamonteiro5482 gen1122
sryuriramos44 gen1122
leyland.kelly1 gen1122
raquelporto7695 gen1122
anabeatrizduarte9000 gen1122
cauaferreira4421 gen1122
sabrinadasneves993 gen1122
pietrocampos9878 gen1122
srpedrolucasdaconceicao938 gen1122
joaovitorporto121 gen1122
cauaferreira2345 gen1122
oliviarezende5747 gen1122
srheitorrodrigues827 gen1122
cauaferreira2360 gen1122
bryanaraujo782 gen1122
estherviana62 gen1122
pietrocampos9754 gen1122
elisasilva518 gen1122
estherviana741 gen1122
pedrohenriquecarvalho938 gen1122
kaiquemartins1135 gen1122
anabeatrizviana4543 gen1122
juliabarbosa3754 gen1122
theodasneves247 gen1122
paulovieira133 gen1122
enzogabrieldacosta97 gen1122
drgustavomendes517 gen1122
isabelgomes7050 gen1122
elisasilva3819 gen1122
giovannamendes1381 gen1122
joaopedroalves5189 gen1122
eduardamonteiro6151 gen1122
samueldias159 gen1122
elisasilva792 gen1122
amandaramos7505 gen1122
caiofogaca482 gen1122
jakub.halid6 gen1122
julianacostela52 gen1122
sheffield.kanaloa5 gen1122
guilhermedasneves629 gen1122
joaovitorporto76 gen1122
analuizamelo5617 gen1122
caiodaconceicao95 gen1122
juliaviana8034 gen1122
srfernandoalmeida25 gen1122
isadorafarias1575 gen1122
anajuliacavalcanti944 gen1122
juliabarbosa5592 gen1122
luanacosta6488 gen1122
srrodrigopires85 gen1122
joaopedroalves5938 gen1122
sabrinadasneves329 gen1122
pedrohenriquemoraes225 gen1122
anajuliacavalcanti179 gen1122
drgustavomendes126 gen1122
isadorafarias389 gen1122
pietrafarias3553 gen1122
srtaamandabarros98 gen1122
elisasilva8218 gen1122
isaacvieira289 gen1122
paulovieira8606 gen1122
oliviarezende555 gen1122
elisasilva9565 gen1122
analuizacunha162 gen1122
joaopedroalves647 gen1122
luizacampos294 gen1122
pietrarodrigues6185 gen1122
mariaalicesouza4320 gen1122
benjaminlopes2110 gen1122
isaacvieira6965 gen1122
joaomiguelbarros829 gen1122
draalicemelo55 gen1122
juliaviana9863 gen1122
benjaminlopes5185 gen1122
srrodrigopires11 gen1122
rafaelporto5970 gen1122
isadorafarias8954 gen1122
luizfelipedias3254 gen1122
emanuellaferreira399 gen1122
isabellysantos2287 gen1122
elisasilva6984 gen1122
drpedrolucasfogaca88 gen1122
drlucasfernandes267 gen1122
kaiquemartins8303 gen1122
kamronbek.micha8 gen1122
erasmo.darek1 gen1122
kaiquebarbosa5967 gen1122
guilhermedasneves8720 gen1122
joaquimsouza1346 gen1122
drgustavomendes31 gen1122
mariaclaracostela737 gen1122
marcelodias9356 gen1122
joaquimsouza4600 gen1122
mariafernandapinto365 gen1122
giovannamendes258 gen1122
marcelodias2821 gen1122
analuizacunha864 gen1122
camiladarosa995 gen1122
marcosviniciusnascimento515 gen1122
isabellysantos730 gen1122
noahsantos4095 gen1122
samueldias3137 gen1122
salvador.blayz7 gen1122
marcosviniciusnascimento4903 gen1122
yamen.jamil26 gen1122
pietrafogaca640 gen1122
joaofelipesilva2923 gen1122
rafaelporto7833 gen1122
kaiquemartins6753 gen1122
isaacvieira5674 gen1122
pedrohenriquecarvalho172 gen1122
drgustavomendes386 gen1122
isabellysantos2542 gen1122
eloahferreira9946 gen1122
isabelgomes7428 gen1122
joaovitorporto5176 gen1122
anabeatrizviana424 gen1122
drpedrolucasfogaca212 gen1122
analuizamelo7978 gen1122
marcosviniciusnascimento226 gen1122
luizacampos1625 gen1122
drlucasfernandes370 gen1122
caiofogaca547 gen1122
drpedrolucasfogaca520 gen1122
mariaalicesouza404 gen1122
joaovitorporto96 gen1122
juliabarbosa759 gen1122
luizacampos8246 gen1122
anabeatrizduarte281 gen1122
srheitorrodrigues865 gen1122
pedrohenriquedapaz50 gen1122
isadorafarias501 gen1122
brenoalmeida278 gen1122
noahsantos115 gen1122
luizacampos6941 gen1122
sabrinadasneves240 gen1122
marcelodias763 gen1122
caiodaconceicao647 gen1122
joaovitorporto75 gen1122
yasminrodrigues7320 gen1122
theodasneves30 gen1122
mariaceciliaporto164 gen1122
pedrohenriquedapaz826 gen1122
socorroleocadio2538 gen1122
angelicasanders8010 gen1122
romanabateman22 gen1122
adelaidedouglas104 gen1122
maysezaganelli37 gen1122
ranyadunn5 gen1122
geruzafraser9 gen1122
ierefreitas701 gen1122
luizabruzaca973 gen1122
mirellasalgado465 gen1122
rosacullen23 gen1122
rhone.hrehaan gen1122
isannasouta41 gen1122
cleidesimao9265 gen1122
isabelalgarves1446 gen1122
iranicantrell6 gen1122
isannachoairy73 gen1122
afroditedempsey6 gen1122
karenamorim7893 gen1122
pandoradepinho175 gen1122
anadionemaewing9 gen1122
mclaughlincarter71 gen1122
thamirishuffman9 gen1122
teolindamendes229 gen1122
mariahdomonte149 gen1122
angelasaraiva195 gen1122
kassiarocha172 gen1122
margaridaporto756 gen1122
irisprohmann555 gen1122
gardeniagila616 gen1122
dianaalegria728 gen1122
angelinagraham465 gen1122
willacarey601 gen1122
murphybernal8 gen1122
maisamacau1941 gen1122
giovannaewerton96 gen1122
melissacoutinho235 gen1122
kincaidhensley6 gen1122
marairamercedes48 gen1122
zarasantos807 gen1122
palomaaleixo465 gen1122
inezdriscoll65 gen1122
mariettaayers29 gen1122
lunabittencourt510 gen1122
oneideviana993 gen1122
iracemaallen5 gen1122
francinexavie953 gen1122
murdockballard76 gen1122
drgustavomendes95 gen1122
joaofelipesilva5514 gen1122
pietrafogaca94 gen1122
anabeatrizduarte8035 gen1122
mariaceciliaporto60 gen1122
mariaceciliaporto3432 gen1122
luizfernandopinto7296 gen1122
marcelodias5031 gen1122
marcosviniciusdacunha2221 gen1122
otaviosales885 gen1122
noahsantos9132 gen1122
vitorhugodamata6684 gen1122
anaclarasilva9543 gen1122
kaiquebarbosa6813 gen1122
pedrohenriquemoraes713 gen1122
anajuliacavalcanti160 gen1122
paulovieira2829 gen1122
caiofogaca963 gen1122
joaolucasfarias658 gen1122
pedrohenriquecarvalho7719 gen1122
raquelporto774 gen1122
drgustavomendes23 gen1122
marcosviniciusdacunha89 gen1122
srcaiodaconceicao272 gen1122
vitorhugodamata82 gen1122
sabrinadasneves989 gen1122
samueldias7802 gen1122
isadorafarias6548 gen1122
julianacostela376 gen1122
rafaeladacosta9508 gen1122
isadorarezende1391 gen1122
juliabarbosa485 gen1122
brenoalmeida3511 gen1122
luizfelipedias5927 gen1122
pedrohenriquedapaz74 gen1122
pedrohenriquecarvalho5860 gen1122
joaolucasfarias26 gen1122
joaopedroalves9351 gen1122
pietrocampos490 gen1122
joaquimsouza4139 gen1122
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
