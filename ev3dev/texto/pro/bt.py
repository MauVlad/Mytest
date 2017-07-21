#_*_coding: utf_8_*_
#!/usr/bin/python

import time

edad = input ("Edad = ")
n = input("N = ")

def creartxt():
	archi=open('a/edad.txt','a')
##	archi.write('Fecha: '+time.strftime("%x "))
##	archi.write('Hora: '+time.strftime("%X "))
	archi.write('Fecha y Hora: '+ time.strftime("%x ")+ time.strftime("%X"))
	archi.close()

while edad <= n:
	print "tienes: " + str(edad)
	edad = edad + 1
	
	def grabartxt():
		archi=open('a/edad.txt','a')
		archi.write(" tienes: " + str(edad - 1 ))
		archi.write(' \n')
		archi.close()
 
	creartxt()
	grabartxt()
