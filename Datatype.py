x=7
print(x, "is of type",type(x))
x=7.0
print(x, "is of type",type(x))
x=22/7
print(x, "is of type", type(x))
x=2+33j
print(x, "is of type", type(x))

x=True
print(x, "is of type", type(x))
print("Is x type of bool?", isinstance(x,bool))

#typecasting
numerator=input("Enter numerator")
denominator=input("Enter denominator")
print(repr(numerator))   #real data representation
result=int(numerator)/int(denominator)    #type conversion
print("Result=",result)

a,b,c,d=2,3.5,2+3j,True
x=str(a)
print(repr(x))
