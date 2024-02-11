mytuple=("Nepal","India","China")
myit= iter(mytuple)  #it makes tuple iterator , by default it is  iterable and  
#we can use for loop to access the values
print("I have visited following countries so far:") 
print(next(myit)) 
print(next(myit)) 
print(next(myit))

