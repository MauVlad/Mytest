######
def muchos_pcn():
	i = input("cunatos numeros: ")
	for j in range(0,i):
		x = input("numero: ")
		if x > 0:
			print "numero poitivo"
		elif x == 0:
			print "es cero"
		else:
			print "numero negativo"
print "def muchos_pcn : ", muchos_pcn()
#####
def pcn_loop():
	hayMasDatos = "Si"
	while hayMasDatos == "Si":
		x = input("ingrese numero: ")
		if x > 0:
			print "numero positivo"
		elif x == 0:
			print "Es cero"
		else:
			print "Numero negativo"
		hayMasDatos = raw_input("Hay mas datos <Si-No>: ")

print "pcn_loop : ", pcn_loop()
#####
def pcn_loop2():
	x = input("Ingrese un numero ('*' para terminar): ")
	while x <> "*":
		if x > 0:
			print "numero positivo"
		elif x == 0:
			print "Es cero"
		else:
			print "numero negativo"
		x = input("Ingrese un numero ('*' para terminar): ")

print "pcn_loop2 : ",pcn_loop2()
#####
def pcn_loop3():
	while True:
		x = input("Ingresa un numero('*' para terminar): ")
		if x == '*':
			break
		elif x > 0:
			print "numero positivo"
		elif x == 0:
			print "Es cero"
		else:
			print "Numero negativo"
print "pcn_loop3 : ", pcn_loop3()
