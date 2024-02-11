word = 'Saurav' 
# creates a set-where duplicate elements are discarded 
letters1 = set(c for c in word) 
letters2 = {c for c in word}  # another way of creating a set 
print(letters1)  # prints: {'l', 'o', 'H', 'e'} 
print(letters1 == letters2)  # prints: True 


#############.......Genereator.........###############
#>...........generator function........<#
def get_squares_gen(n):  # generator approach 
    for x in range(n): 
        yield x ** 2  # we yield, we don't return 
gen=get_squares_gen(10) 
print(type(gen)) 
 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen))
