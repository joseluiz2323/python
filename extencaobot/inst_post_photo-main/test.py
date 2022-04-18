from time import sleep
from instagram import Instagram

login = 'srpedrolucasdaconceicao64'
password = 'xxxxx123'

if __name__ == "__main__":
    inst = Instagram()
    inst.login(username=login, password=password)
    sleep(10)
    with open('C:\\Users\\lui_z\\Desktop\\python\\extencaobot\\fotos\\femenino\\Pasta 2\\1 (102).jpg', 'rb') as image:
        print(inst.post(image, caption='status'))
    sleep(10)
    with open('C:\\Users\\lui_z\\Desktop\\python\\extencaobot\\fotos\\femenino\\Pasta 2\\1 (102).jpg', 'rb') as image:
        print(inst.post(image, caption='status'))
    with open('C:\\Users\\lui_z\\Desktop\\python\\extencaobot\\fotos\\femenino\\Pasta 2\\1 (102).jpg', 'rb') as image:
        print(inst.post(image, caption='status'))
    sleep(11)
    with open('C:\\Users\\lui_z\\Desktop\\python\\extencaobot\\fotos\\femenino\\Pasta 2\\1 (102).jpg', 'rb') as image:
        print(inst.post(image, caption='status'))
    sleep(12)
    with open('C:\\Users\\lui_z\\Desktop\\python\\extencaobot\\fotos\\femenino\\Pasta 2\\1 (102).jpg', 'rb') as image:
        print(inst.post(image, caption='status'))
