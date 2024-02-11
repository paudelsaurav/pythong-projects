import collections
employee=collections.namedtuple("employee",("name","age","gender"))
emp=employee("saurav",19,"male")
print(emp.age)
print(emp[1])
print(emp)
print(type(emp))


import collections as col
employee=col.namedtuple("employee",["name","age","gender"])
emp=employee("saurav",19,"male")
print(emp.name)
print(emp)
print(emp[0])

#deque
from collections import deque
q=deque([10,20,30,40])
q.appendleft(0)
print(q)
q.append(50)
print(q)
q.pop()
print(q)
q.popleft()
print(q)
######
from collections import deque
numbers=deque([],maxlen=6)   #creates empty deque of max capacity 6 
for i in range(10):          #for loop iterates for 10 iterations 
    numbers.append(i)
    print(numbers)
    
    
#counter
from collections import Counter
c=Counter()
list=[1,2,3,4,5,6,7,8,4,7,5,6,7,10]
print(Counter(list))   #gives dictionary with key numbers and frequency values
c=Counter(list)
print(c[1])    #gives frequency of 5 in list (mode in statistics)