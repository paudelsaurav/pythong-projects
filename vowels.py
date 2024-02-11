def check(letter): 
    list_of_vowels = ['a', 'e', 'i', 'o', 'u'] 
    if letter in list_of_vowels: 
        return True 
    else: 
        return False 
letters="Saurav chapagain"
fil_obj=list(filter(check,letters))
print("The type of returned object is: ", type(fil_obj)) 
filtered_list = fil_obj
print("My name contains", len(filtered_list), " vowel letters.") 
print("The list of vowels is: ", filtered_list) 

########################################################
#using for anf if conditions
employee=['ananda','anoop','akshay','bibek','amrit','ram','shyam','anjit']
newlist=[]
for emp in employee:
    if 'a' in emp:
        newlist.append(emp)
print("without list Comprehension", newlist)

#using comprehension


###>............Nested list comprehension..............<###
items ='ABCDE'
pairs =[]
for a in range(len(items)):
    for b in range(a,len(items)):
        pairs.append((items[a],items[b]))
    print(pairs)
    
    
list1=[(items[a],items[b]) for a in range(len(items)) for b in range (a,len(items)) if items
       [a]!=items[b]]
       
print(list1)


#>.................Filtered comprehension............<#
from math import sqrt
mx=10
legs=[(a,b,sqrt(a**2 + b**2)) for a in range(1,mx)]

