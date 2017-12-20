a = ['rojo','verde','azul','violeta']

for x in a:
    print x, len(x)

for x in a[:]:
    if len(x) > 6: a.insert(0,x)
print (a)

for x in a[:]:
    if len(x) > 5: a.insert(0,x)
print(a)

for x in a[:]:
    if len(x) > 4: a.insert(0,x)
print(a)

for x in a[:]:
    if len(x) > 3: a.insert(0,x)
print(a)

