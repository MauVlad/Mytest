canasta = ['24', 'hola', 'adios', 'hola', '23', '23', '24']

df = set(canasta)

print df

x = raw_input("caracter a buscar: ")
print x in df

y = raw_input("Escribir un caracter: ")
a = set(y)
print a
z = raw_input("Escribir un caracter: ")
b = set(z)
print b

print "Letras en a pero no en b ", a - b
print "letras en a o en b", a | b
print "letras en a y en b", a & b
print "letras en a o b pero no en ambas", a ^ b
