def filtro(elem):
	return (elem > 0)

s = [1, 2, 3, -4, 0, -3, -12, -23]

lr = filter(filtro,s)

print s
print lr
print type(lr)

def filtro(elem):
	return (elem == "o")

s = "hola mundo,hola a todos"

lr = filter(filtro, s)

print s
print lr
print type(lr)

