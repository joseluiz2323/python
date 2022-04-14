import os

# deletar um arquivo text


def deletar_arquivo_text():
    try:
        simp_path = r'config\\config.txt'
        abs_path = os.path.abspath(simp_path)
        nome_arquivo = abs_path
        arquivo = open(nome_arquivo, 'r+')
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
    arquivo.close()
    os.remove(nome_arquivo)


# emailfake = 1
# anonimo = 1
# navsemimages = 1
# navocultos = 0
# senha = gen1122
