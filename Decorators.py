def devision(a,b):
    return a/b

def deco(func):  # func=division 
    def inner(a, b):  # inner function used for swapping the numbers 
        if a < b: 
            a, b = b, a  # swapping values of a and b 
        return func(a, b)  # it calls the division function 
    return inner

@deco
def division(a,b):
    return a/b

@deco
def swap(a,b):
    return(a,b)

value=devision(4,8)
print(value)

#numerator must be greater than denominator



#WAP to find the square root of a number and make the number entered positive if the number is negative
import math
def sqr(a):
    result= math.sqrt (a)
    print(result)

def deco(func):
    def inner(a):
        if a<0:
            return -a
        
print(sqr(4))  


import math as mt
def absdeco(method):
    def inner(a):
        a=abs(a)
        return method(a)
    
print()
        



def fibo(func):
    def inner(n):
        n>0
    return inner
@fibo
def fibo1(n):
    result = [] 
    a, b = 0, 1 
    while a < n: 
        a, b = b, a+b 
    return result 
 
print (fibo1(100)) 


