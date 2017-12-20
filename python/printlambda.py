def hacer_incrementador(n):
	return lambda x: x + n

y = float(input("Numero para incremento : ", ))

f = hacer_incrementador(y)

a = float(input("primer incremento : ", ))
print (f(a))
b = float(input("segundo incremento : ", ))
print (f(b))
c = float(input("tercer incremento : ", ))
print ((f(a)*f(b))/f(c))

print type(f)

