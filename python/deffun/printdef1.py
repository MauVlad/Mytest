def f(a, L=[]):
    L.append(a)
    return L

x = int(input("numero : ", ))
y = int(input("numero2 : ", ))
z = int(input("numero3 : ", ))

print f(x)
print f(y)
print f(z)

