import os

from regex import P

from func.open_json import ler_config_json


simp_path = r'config\\config.json'
abs_path = os.path.abspath(simp_path)
config = ler_config_json(abs_path)

if config['montagem']['postagen_de_story']['quantidade_fotos'] > 0:
    print('Postando story')
    pass
