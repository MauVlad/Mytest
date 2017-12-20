from time import sleep
#t = [2,2*3,"adios"]
#print t
#print type(t)

x =float(input("x = "))
t1= (x, 1500,350,-350)
print t1
print type(t1)

x1 =float(input("x1 = "))
t2 = (x1,750,350,-350)
print t2
print type(t2)

y1 =float(input("y1 = "))
t3 = (y1,750,-350,350)
print t3
print type(t3) 

y =float(input("y = "))
t4 = (y,1500,-350,350)
print t4
print type(t4) 

sleep(2)
t5 = (t1,t2,t3,t4)
print t5
print type(t4)

sleep(2)
#x = input("N = ")
an = max(t5)

z,a,b,c = an

print z
print a,b,c
