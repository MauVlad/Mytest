def seleccion(operacion):
	def suma(n,m):
		return n+m

	def resta(n,m):
		return n-m

	def multiplicacion(n,m):
		return n*m

	def division(n,m):
		return n/m

	if operacion == "suma":
		return suma
	elif operacion == "resta":
		return resta
	elif operacion == "multi":
		return multiplicacion
	elif operacion == "divide":
		return division
	else:
		print "No es operacion"

x = raw_input("seleccione suma, resta, multi, divide: ")

f = seleccion(x)

y = float(input("Escribe un numero para 'n': "))
z = float(input("Escribe un numero para 'm': "))

if x == 'suma':
	print y,'+',z,'=',f(y,z)
elif x == 'resta':
	print y,'-',z,'=',f(y,z)
elif x == 'multi':
	print y,'*',z,'=',f(y,z)
elif x == 'divide':
	print y,'/',z,'=',f(y,z)
else:
	print "Nada que hacer a",y,'y a',z, "sin 'seleccion de operacion'"

