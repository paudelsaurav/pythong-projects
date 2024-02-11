dictionary1={1:"Python",2:"Javascript",3:"Java"}
print("First Language nowadays is",dictionary1
      [1])
dictionary2=dict({"Apple":"Most Loved fruit","Mango0": "King of fruits"})
print("Apple is:",dictionary2["Apple"])

student = {"name": "Saurav", "age": 19, "bloodgroup": "AB+"}
print ("Before update:", student)
print ("\nChange age to 19:\nAdding gender key:value pair")
#updating
student["age"] = 36
student["gender"] = "Male"
print ("\nAfter update:", student)
#Deleting
print("Delete bloodgroup entry:")
del student["bloodgroup"]
print("After deleting bloodgroup:", student)



dict1 = {"name": "saurav", "age": 19, "gender": "male"}
dict2 = {"name": "saurav", "age": 20, "gender": "male"}
if (dict1 == dict2):
   print("both dictionaries are equal")
else:
   print("both dictionaries are not equal")
print("The length of dict1=", len(dict1))
# print("The dict2 is: "+dict2) #error because dict2 is dictionary not string
#converting dict2 into string as follows
print("The dict2 is: "+str(dict2))
print("the type of age key is:",type(dict2.get('age')))
print("the type of name key is:",type(dict2.get('name')))
#7
dict2 = {"name": "harendra", "age": 36, "gender": "male"}
dict2.clear() # removes all the contents of dictionary
print(dict2)
dict2 = dict1.copy() # copy one dictionary to another (whole content)
print(dict2)
# fromkeys(x,y) method
x = ("key1", "key2", "key3")
y = 1
dict4 = dict.fromkeys(x, y) # dict is a keyword used for dictionaries
print(dict4)
print("key1" in dict4) # return true because key1 is in dict4

print(dict2.items())
print(dict2.keys())
print(dict2.values())
dict4.update(dict2)
print(dict4)

#setdefault() in Dictionary
person={"name": "Aaiya","age":100,"gender":"female"}
person.setdefault("email","paudelsaurav37@gmail.com")
print(person)
dict2.setdefault("email","paudelsau37@gmail.com")   #gender is removed with value-last inserted
print(dict2)

#removal using pop and popitem
dict4.pop("key1")  #key1 is removed with value
print(dict4)
dict4.popitem()
print(dict4)
