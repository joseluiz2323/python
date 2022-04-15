import json
import os

# ler o arquivo json config\\config.json


def ler_config_json(arquviro):
    with open(arquviro, "r", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    return dados


def alterar_genero():
    dados = ler_config_json()
    dados['criacao']['genero'] = 'F'
    with open("config\\config.json", "w", encoding='utf-8') as meu_json:
        json.dump(dados, meu_json, indent=4)
