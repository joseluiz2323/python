import os
import random


simp_path = r'config\\legendas.txt'
abs_path = os.path.abspath(simp_path)
lista = []
with open(abs_path, encoding='utf8') as infile:
    for i in infile.read().splitlines():
        lista.append(i)
bio = random.choice(lista)
print(str(bio))
