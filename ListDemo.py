fruits=["Apple","Banana","watermelon","Dragon","Berry"]
#Modification
fruits[2]="Litchi"
print(fruits)
fruits.append("Guava")    #adds element in the list
print(fruits)
fruits.remove("Berry")   #removes elements in the list
print(fruits)
print(len(fruits))# calculate length using len function
for f in fruits:    #printing the items list wise
    print(f)
    
count=0
for f in fruits:
    count+=1
    print(count, f)
    
numbers=[34,23,56,78,67,57,89,34]
print("Maximum number=", max(numbers))
roll=(23,25,35,67)
print(roll)
roll=list(roll)
print(roll)
print(numbers[::-1])

print(numbers.count(34))
numbers.extend(roll)
print(numbers)
print(numbers.pop(0))
numbers.insert(3,100)
print(numbers)

age=numbers.copy()   #copy the list into another name

print(age)


