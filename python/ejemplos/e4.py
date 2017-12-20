def fib(n):

    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

print (fib(2000))

print (fib)

f = fib
print (f(100))

print (fib(0))
