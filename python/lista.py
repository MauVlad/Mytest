lista = [1, "Dos", 3, "cuatro", 5, "seis"]
print lista

z = float(input("Escribir un numero: "))
lista.append(z)
print lista

x = raw_input("Buscar palabra: ")
y = float(input("Buscar numero: "))

lista.reverse()
print lista

buscar = x
if buscar in lista:
	
	print buscar in lista
	print lista.index(buscar)
else:
	print "No esta el elemento"

buscar = y
if buscar in lista:

	print buscar in lista
	print lista.index(buscar)
else:
	print "No esta el elemento"

