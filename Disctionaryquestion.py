#Input any 10 students in a dictionary and display in reverse order using dictionary



# Initialize an empty dictionary to store student information
student={} #empty dictionary
for i in range (10):
    x=input("Enter Student")
    student[i]=x
print(student)
print(dict(reversed(student.items())))
