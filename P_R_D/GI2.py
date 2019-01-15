from PIL import Image
from random import randrange
from numpy import random

lista = ['imagenes/placa0.jpg', 'imagenes/placa1.jpg', 'imagenes/placa2.jpg']
lista2 = ['imagenes/comp.png', 'imagenes/comp0.png', 'imagenes/comp1.png', 'imagenes/comp2.png']
lista3 = ['imagenes/comp.jpg', 'imagenes/comp0.jpg', 'imagenes/comp1.jpg', 'imagenes/comp2.jpg']
x = 0

num_generar = 80
for i in range(num_generar):
    #imagen de fondo
    fondo = Image.open(random.choice(lista))

    #imagen tipo .png para colocar sobre el fondo
    objeto = Image.open(random.choice(lista2)).convert("RGBA") 
    objeto = objeto.resize((objeto.width//3,objeto.height//3))
    objeto = objeto.rotate(randrange(180))

    #posicion random dentro de la imagen
    pos = ((fondo.width - randrange(fondo.width-objeto.width)), (fondo.height - randrange(fondo.height-objeto.height)))

    img_nueva = fondo.copy()
    img_nueva.paste(objeto, pos, objeto)
    name = ('Imagenes_generadas/' + str(i) + '.jpg')
    img_nueva.save(name)

print('Generadas ' + str(i + 1) + ' imagenes')

for i in lista3:

    imag = Image.open(i)
    imag_rotada = imag.rotate(randrange(180))
    x = x + 1
    imag_rotada.save('Imagenes_generadas/mcc_rotada' + str(x) + '.jpg')

print('Rotadas ' + str(x) + ' imagenes')
