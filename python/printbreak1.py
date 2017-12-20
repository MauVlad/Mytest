z = int(input("rango de inicio : ", ))
y = int(input("rango de fin : "))

for n in range(z, y):
    for x in range(z, n):
        if n % x == 0:
           print n, 'es igual a ', x, '*', n/x
           break
    else:
         print n,'es un numero primo'
