file = raw_input ("Borrar datos (b) o anexar datos (a) : ")

k = raw_input ("Escribe: ")

if file == 'b':
	def creartxt():
		archi=open('b/edad2.txt','w')
		archi.close()
	creartxt()

if file == 'a':
	def creartxt():
		archi=open('b/edad2.txt','a')
		archi.close()

	edad = input ("Edad = ")
	n = input("N = ")

	while edad <= n:
		print "tienes: " + str(edad)
		edad = edad + 1
	
		def grabartxt():
			archi=open('b/edad2.txt','a')
			archi.write("tienes: " + str(edad - 1 ))
			archi.write(' \n')
			archi.write(k)
			archi.write(' \n')
			archi.close()
 
		creartxt()
		grabartxt()
