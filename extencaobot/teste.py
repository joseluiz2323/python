# import os
# import psutil as ps
# from datetime import datetime

# print(datetime.today().strftime('%H:%M:%S'))

# # import requests

# # ip_publico = requests.get('https://api.ipify.org/').text
# # print(f'IP Publico: {ip_publico}')


# def criacao_de_logo(numbers, logs):
#     data = datetime.today().strftime('%H:%M:%S')
#     try:
#         simp_path = r'logs\\log_de_criacao.txt'
#         abs_path = os.path.abspath(simp_path)
#         nome_arquivo = abs_path
#         arquivo = open(nome_arquivo, 'r+')
#     except FileNotFoundError:
#         arquivo = open(nome_arquivo, 'w+')
#     arquivo.close()
#     f = open(abs_path, 'r')
#     conteudo = f.readlines()
#     conteudo.append(f'\n{numbers}-{data}-{logs}')
#     f2 = open(abs_path, 'w')
#     f2.writelines(conteudo)
#     f2 = open(abs_path, 'r')
#     arquivo.close()


# criacao_de_logo(1, 'Criado')


# def ler_arquivo_log():
#     try:
#         simp_path = r'logs\\log_de_criacao.txt'
#         abs_path = os.path.abspath(simp_path)
#         nome_arquivo = abs_path
#         arquivo = open(nome_arquivo, 'r+')
#     except FileNotFoundError:
#         arquivo = open(nome_arquivo, 'w+')
#     arquivo.close()
#     f = open(abs_path, 'r')
#     conteudo = f.readlines()
#     print(len(conteudo))
#     f.close()
#     return conteudo


# conteudo = ler_arquivo_log()

# # deletar dados do arquivo de log/log_de_criacao.txt


# def deletar_arquivo_log():
#     try:
#         simp_path = r'logs\\log_de_criacao.txt'
#         abs_path = os.path.abspath(simp_path)
#         nome_arquivo = abs_path
#         arquivo = open(nome_arquivo, 'r+')
#     except FileNotFoundError:
#         arquivo = open(nome_arquivo, 'w+')
#     arquivo.close()
#     f = open(abs_path, 'w')
#     f.close()


# if len(conteudo) > 10000:
#     deletar_arquivo_log()
