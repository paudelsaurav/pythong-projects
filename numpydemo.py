


import numpy as npy
A = [n*n for n in range(20)] 
print("List is:") 
print(A) 
B =npy.array(A)     
print("Numpy array is:") 
print(B) 
print("The type of B is:", type(B)) 