radius=float(input("Enter the radius: "))
from math import pi
def area(r):
    return pi*r**2
a=area(radius)
print(f"The area of a circle is {a:.2f}")
#Write a Python program that accepts the user's first and last name and prints them in 
#reverse order with a space between them.

name=input("Enter your first and last name: ")
def reversee(n):
    rev_name=n[::-1]
    return rev_name
print("Your name reversed is: ",reversee(name))
#Write a Python program that accepts a sequence of comma-separated numbers from the 
#user and generates a list and a tuple of those numbers

num=(input("Enter a sequence of comma seperated numbers: "))
num_list=list(num.split(','))
num_tuple=tuple(num.split(','))
print("List=",num_list)
print("Tuple=",num_tuple)
#Write a Python program to calculate the number of days between two dates.

date1=input("Enter first date(yyyy-mm-dd):")
date2=input("Enter second date(yyyy-mm-dd):")

y1=int(date1[0:4])
m1=int(date1[5:7])
d1=int(date1[8:])
y2=int(date2[0:4])
m2=int(date2[5:7])
d2=int(date2[8:])

year=y2-y1
month=m2-m1
day=d2-d1

monthh=month+year*12
days=day+monthh*32
print(days)
 #Write a Python program to calculate the difference between a given number and 32. If the 
#number is greater than 32, return twice the absolute difference

n=int(input("enter a number: "))
diff=32-n
if n<=32:
    print(diff)
else:
    print(abs(diff*2))
 #Write a Python program that determines whether a given number (accepted from the 
#user) is even or odd, and prints an appropriate message to the user

n=int(input("Enter a number: "))
if n%2==0:
    print(n,"is an even number.")
else:
    print(n,"is an odd number.")
 #Write a Python program to test whether a passed letter is a vowel or not

vowel=['a','e','i','o','u','A','E','I','O','U']
letter=input("enter a letter: ")
if letter==vowel:
    print("The provided letter '",letter,"' is a vowel.")
else:
    print("The provided letter '",letter,"' is not a vowel.")
 #Write a Python program that prints out all colors from color_list_1 that are not present in 
#color_list_2.

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
diff=color_list_1-color_list_2
print(diff)
 #Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2)

from math import sqrt
a=input("enter the first point(x1,y1): ")
b=input("enter the second point(x2,y2): ")

x1=int(a[0])
y1=int(a[2])
x2=int(b[0])
y2=int(b[2])
distance=sqrt((x2-x1)**2+(y2-y1)**2)
print(f"The distance between the two points ({a}) and ({b}) is: {distance:.2f}")
#Write a Python program to sum the first n positive integers

n=int(input("enter the number of terms: "))
sum=0
for i in range(n+1):
    sum=sum+i
    i+=1
print(sum)
 #Write a Python program to convert height (in feet and inches) to centimeters

h=float(input("Enter your height in foot and inches:"))
cm=h*30.48
print("Your height in centimeters is ",cm)