x = raw_input('escribe una palabra: ')

def creaciontxt():
	archi=open('datos.txt','w')
	archi.close()

def grabartxt():
	archi=open('datos.txt','a')
	archi.write('Linea 1\n')
	archi.write('Linea 2\n')
	archi.write('Linea 3\n')
	archi.write('Hola')
	archi.write('Adios \n')
	archi.write(x)
	archi.close()

creaciontxt()
grabartxt()
