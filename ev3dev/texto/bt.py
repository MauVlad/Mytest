import time

edad = input ("Edad = ")
n = input("N = ")

def creartxt():
	archi=open('edad.txt','a')
	archi.write('Fecha: '+time.strftime("%x "))
	archi.write('Hora: '+time.strftime("%X "))
	archi.close()

while edad <= n:
	print "tienes: " + str(edad)
	edad = edad + 1
	
	def grabartxt():
		archi=open('edad.txt','a')
		archi.write(" tienes: " + str(edad - 1 ))
		archi.write(' \n')
		archi.close()
 
	creartxt()
	grabartxt()
