from time import sleep

def funcion(palabra, numero):
	contenido = palabra, numero
	print contenido, "\n"

funcion('hola', 23)
sleep(2)

def saludar(nom, men='hola'):
	print men, nom, "\n"

saludar('mau')
sleep(2)

def nsalu(nom, men='Hola'):
	print men, nom, "\n"

nsalu(men="Buen dia", nom="a mi")
sleep(2)

def parametro_arbita(para_fijo, *arbitrario):
	print para_fijo, "\n"
	sleep(2)

	for argu in arbitrario:
		print argu, "\n"
		sleep(2)

parametro_arbita("1","arbitra 0", "arbitra 1", "arbitra 2", "arbitra 3")

def parametro_arbi(p_fijo, *arbitrarios, **kwords):
	print p_fijo, "\n"
	sleep(2)
	for argumen in arbitrarios:
		print argumen, "\n"
		sleep(2)

	for clave in kwords:
		print "El valor de", clave, "es", kwords[clave], "\n"
		sleep(2)

parametro_arbi("Fixed", "arbitrario 1", "arbitrario 2", "arbitrario 3", clave1="valor uno", clave2="valor dos")
