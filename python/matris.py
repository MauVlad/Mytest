x = int(raw_input("primer fila : ", ))
y = int(raw_input("segunda fila : ", ))
z = int(raw_input("tercera fila : ", ))

mat = [
	[x, y, z],
	[x, y, z],
	[x, y, z],
       ]
print mat

print [[fila[i] for fila in mat] for i in [0, 1, 2]]
######################################################
for i in [0, 1, 2]:
	for fila in mat:
		print fila[i],
	print
#######################################################
print zip(*mat)
