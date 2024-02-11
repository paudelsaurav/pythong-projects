def geometric_progression(a, q): 
    k = 0 
    while True: 
        result = a * q**k 
        yield result 
        k += 1 
gp = geometric_progression(2, 5) 
print(next(gp)) 
print(next(gp)) 
print(next(gp)) 
print(next(gp)) 
print(next(gp)) 
print(next(gp)) 
print(next(gp)) 
print(next(gp)) 
print(next(gp)) 
print(next(gp)) 
print(next(gp)) 
print(next(gp)) 
print(next(gp))


#fibonacci series
def fib(n): 
    a, b = 0, 1 
    while a <= n: 
        yield a 
        a, b = b, a + b 
fib1=fib(100) 
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))