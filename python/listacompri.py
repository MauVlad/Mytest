
l = [1,2,3,-1,-2,4,0]
s = ["H","O","L","A"]
l2 = [c * num for c in s
		for num in l
			if num > 0]
print "comprension de listas"
print l
print l2


l2 = (c * num for c in s
		for num in l
			if num > 0)
####################################
print "Generadores"
print l

for letra in l2:
	print letra
##################################
def factorial(n):
	i = 1;
	while n > 1:
		i = n*i
		yield i	
		n -= 1

print "factorial"

for e in factorial(5):
	print e
