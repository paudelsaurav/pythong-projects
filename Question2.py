#WAP to sum the n entered number by user
def num(n):
    for i in range(n):
        yield int(input("Enter a number: "))

def sum_no(numbers):
    return sum(numbers)


n = int(input(" number you want to sum: "))

generator = num(n)
result = sum_no(generator)
print("The sum numbers is:",result)
