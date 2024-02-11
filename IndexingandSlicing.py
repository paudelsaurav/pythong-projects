a=list(range(100))
print(a)
print(a[0:100:2])

#WAP in python to check whether the entered number is palindrome or not.

num=(input("Enter the number"))
n=num[::-1]
if(num==n):
    print("the number is palondrome")
else:
    print("the number is not palindrome")