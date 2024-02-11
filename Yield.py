def yieldFunc(a, b): 
    while b > 0: 
        b += 1 
        yield a**b #desired number of sequences can be achieved using yield 
gen = yieldFunc(2, 3) 
print("Output by yield") 
print(next(gen)) 
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))