import numpy as np
data_type=np.dtype([('subject', 'S10'),('marks',int)])
arr= np.array([('Maths',70),('English',60),('Python',80),('Nepali',55)],dtype=data_type)
print("Sorting data ordered by subject and marks") 
print(np.sort(arr, order='marks')) 
print(np.sort(arr, order='subject')) 