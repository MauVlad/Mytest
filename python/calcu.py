a = float(input("A = "))
b = float(input("B = "))

x = raw_input("Escriba la operacion, suma, resta, mutiplica, divide : ")

if x == 'suma':
	x = a + b
	print "La suma es: ", x

elif x == 'resta':
	x = a - b
	print "La resta es: ", x

elif x == 'multiplica':
	x = a * b
	print "La multiplicacion es: ", x

elif x == 'divide':
	x = a / b
	print "La division es: ", x

elif x == 'todo':
	x = a + b
	print "suma : ", a, '+', b, "=", x
	x = a - b
	print "resta : ", a, "-", b,'=', x
	x = a * b
	print "multiplicacion : ", a, '*', b, '=', x
	x = a / b
	print "division : ", a, "/", b, "=", x
else:
	print "operacion no encontrada"
