def is_multiple_of_five(n):
    return not n%5
def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five,range(n)))
print(get_multiples_of_five(50))

#iterative collection

def get_multiple_of_five(n):
    return list(filter(lambda k:not k%5,range(n)))
print(get_multiple_of_five(50))


#Random number generator/pseudo-random numbers.

from random import random, seed, randint, uniform, choice, randrange
#random function
print(random()) #generate random number, different at different 
print(seed(1))  #repeat the same random number every time
print(random())
print(random())
#choice function
print(choice("abcdefghijklmnopqrstuvwxyz"))
print(choice(range(100)))
print(choice([10,20,30,40,50]))
#uniform function
print(uniform(1,10))  #return random number     