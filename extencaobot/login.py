from instagrapi import Client


class Client_verificador:
    def __init__(self):
        self.username = ""
        self. password = ""
        self.clint = Client()

    def login(self, username, password):
        self.username = username
        self.password = password
        self.clint.login(username=self.username, password=self.password)
        return self.clint.user_id

    def verificar_seguidores(self, conta):
        try:
            dados = self.clint.user_info_by_username(conta)
            idconta = self.clint.user_id_from_username(conta)
            return dados.biography, dados.follower_count, dados.following_count, dados.media_count, len(dados.profile_pic_url)
        except:
            print("Erro ao verificar seguidores")


cl = Client_verificador()
id = cl.login(username="rebecabrown617", password="gen1122")
contas = ['__rayannefarias', 'neymarjr', 'amandapaiiva__', 'jemimeharris7', 'lindon.keiron', 'erciliabaima77', 'blendahunt8',
          'rafaelamoura6788', 'noahsantos4390', 'pietrocampos277', 'pedrolucasfernandes489', 'srdanilopinto259', 'benjaminlopes821', ]
dados_retorn = []
for conta in contas:
    dados_retorn.append(cl.verificar_seguidores(conta))

print(dados_retorn)
