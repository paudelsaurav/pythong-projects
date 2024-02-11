from collections import defaultdict as dd
def notfound():
    return "Not found"
d1=dd(notfound)  #dictionary
d1["name"]="saurav"
d1["age"]=19
d1["gender"]="male"

print(d1["name"])
print(d1["age"])
print(d1["gender"])


#Without Using defaultdict
from collections import defaultdict as default
quote="nothing is permanent in life besides non living things"
d=default(int) #default value is 0 -default (lambda:2) to change the default value
for i in quote:
    if i in quote:
        d[i]+=1
print(d)


    

    
