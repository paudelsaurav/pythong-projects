dict1 = {"name": "harendra", "age": 33, "gender": "male"}
dict2 = {"name": "harendra", "age": 36, "gender": "male"} 
dict2.clear()  # removes all the contents of dictionary 
print(dict2) 
dict2 = dict1.copy()  # copy one dictionary to another (whole content) 
print(dict2)

x = ("key1", "key2", "key3") 
y = (1,2,3)
dict4 = dict.fromkeys(x, y) # dict is a keyword used for dictionaries 
print(dict4) 
print("key1" in dict4)


print(dict2.items())  # returns all items 
print(dict2.keys())  # returns all keys 
print(dict2.values())  # returns all values 
dict4.update(dict2)  # append or update the dict4 with dict2 elements 
print(dict4)

dict2.setdefault("email", "harendra@gmail.com") 
print(dict2) 
dict2.setdefault("email", "haren@gmail.com")  # email key is already exists 
print(dict2)  

dict2.pop("name")  # key1 is removed with value 
print(dict2) 
dict2.popitem()  # gender is removed with value-last inserted key-value item 
print(dict2)    