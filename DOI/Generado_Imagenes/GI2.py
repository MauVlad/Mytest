from PIL import Image
from random import randrange
from numpy import random

lista = ['imagenes/playita.jpg', 'imagenes/playa.jpg', 'imagenes/ciudad.jpg', 'imagenes/calle.jpg', 'imagenes/rancho.jpg']
lista2 = ['imagenes/bud.png', 'imagenes/caguama.png']

num_generar = 50
for i in range(num_generar):
    #imagen de fondo
    fondo = Image.open(random.choice(lista))

    #imagen tipo .png para colocar sobre el fondo
    objeto = Image.open(random.choice(lista2))
    objeto = objeto.resize((objeto.width//5,objeto.height//5))
    objeto = objeto.rotate(randrange(180))

    #posicion random dentro de la imagen
    pos = ((fondo.width - randrange(fondo.width-objeto.width)), (fondo.height - randrange(fondo.height-objeto.height)))

    img_nueva = fondo.copy()
    img_nueva.paste(objeto, pos, objeto)
    name = ('Imagenes_generadas/' + str(i) + '.jpg')
    img_nueva.save(name)

imag = Image.open('imagenes/mcc.jpg')

imag_rotada = imag.rotate(randrange(180))

imag_rotada.save('Imagenes_generadas/mcc_rotada.jpg')
