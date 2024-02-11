name='saurav paudel'
address="kalanki"
about="""My name I dont know
I love Ms Dhoni the most and I
wanna meet him"""
#print(name)
#print(address)
#name[3]='a'   #cannot do this cause it is immutable syntax
print(name[4])    #indexing
print(name[9:12])     #slicing
print(name,address,about)
teststr=name*3
print(teststr)
print("Saurav" in about)
s=r'\t dsahdj \n SJkbs'    #gives the raw data i.e same as the input
print(s)
print("My name is %s and I am %d years old!" %("saurav",19))
print("My name is {}, his name is {} ans her name is {}".format("saurav","mukss","Abhi"))



#split function in string
stringval="Nepal is a beautiful country."
print(stringval.split())  #split
print(stringval.upper())
country=["Nepal","India","Pakistan"]
he="Hello"
print(he.join(country))
print(stringval.replace("Nepal","India"))
print(stringval.find("beautiful"))  #gives the index of the word

list=[1,2,3,4,256]  #cannot do this as bytes must have range between (0-255)
b=bytes(list)

