#factorial using recursive function
def factorial(n):
    if n in (0,1):
        return 1
    return factorial(n-1)*n
num = int(input("Enter a number"))
print("The factorial is ",(factorial(num)))



#Fibonacci series using recursive function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(input("Enter the number of terms in the Fibonacci series: "))
for i in range(num):
        print(fibonacci(i))
        
#WAP to find the greatest number among three numbers using nested if else statement.

num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
num3=int(input("Enter 3rd number"))

if(num1>num2):
    if(num1>num3):
        print("num1 is the greatest")
    else:
        print("num3 is greater")
else:
    if(num2>num3):
        print("num2 is greatest")
        
    else: 
        print("num3 is greatest")
    
