#Series de Finonacci:
# la suma de dos elementso 

a,b = int(input("A= ")),int(input("B= "))
c = int(input("C= "))

while b<c:
    print b,
    a, b = b, a+b
