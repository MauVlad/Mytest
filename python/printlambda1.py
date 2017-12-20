def hacer_incrementador(n):
	return lambda x: x + n

y = float(input("Numero para incremento : ", ))

f = hacer_incrementador(y)

a = float(input("primer incremento : ", ))
print (f(a))
b = float(input("segundo incremento : ", ))
print (f(b))
c = float(input("tercer incremento : ", ))
print (f(c))

d = raw_input("palabra : ", )
print y, a, f(a), b, f(b), c, f(c), d

print type(f)
print type(d)
