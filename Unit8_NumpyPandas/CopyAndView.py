#copy -> change value of only one i.e a1
import numpy as np
a1= np.array([2,3,4,5])
a2=a1.copy()
a1[1]=40
print(a2) # copy only copies the recent list
print(a1)

#view()  -> change value in both
import numpy as np
a1= np.array([2,3,4,5])
a2=a1.view()
a1[1]=40
print(a2)# view cahnges the value
print(a1)# view changes the value

#linspace
import numpy as np
x=np. linspace(10 ,20, 15, True, False, dtype=int)
y=np. linspace(10 ,20, 5, True, True, dtype=float)

print("x=",x)
print("Y=",y)# second true gives common difference between items

#logspace
import numpy as np
a=np.logspace(2,10, num=10,base=2,dtype=float)
print(a)

#description
#2 start, 10 end, 10 - no of terms

#array broadcasting
import numpy as np  # this is a wromg code
a= np.array([1,2,3,4],
            [2,4,6,8])
b=np.arary([10,20,30,40])
c=a*b
print(c)

#multiplying the array
import numpy as np 
a= np.array([1,2,3,4],
            [2,4,6,8])
b=np.arary([10,20,30,40])
#############.............assignment...........################# in 3*3 matrices

# nditer
# -> reduces the use of for loop 
import numpy as np
arr= np.array([[[1,2],[3,4],[5,6],[7,8]]])
for x in np.nditer(arr):
    print(x)
    
# sorting and searching
# # quick sort ,,,,  merge sort ,,,, Heap sort

import numpy as np
a=np.array([[12,6],[10,11],[16,14]])
arr1=np.sort(a,kind="mergesort", axis=-10)  #it sorts items in three arrays, ascending order
arr2=np.sort(a,kind="headsort",axis=0)   #it sorts items in three arrays, descending order

arr3=np.sort(a,kind="quicksort", axis=1)  # it sorts items in three arrays , ascending 
arr4 = np.sort(a, kind="quicksort", axis=None)  # it sorts all items and return in a single array 

print("arr1 : \n", arr1) 
print("arr2 : \n", arr2) 
print("arr3 : \n", arr3) 
print("arr4 : \n", arr4)
