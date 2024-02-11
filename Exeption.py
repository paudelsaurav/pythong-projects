class AgeException(Exception):
    def __init__(self,message):
        self.message=message
        
def Age(age):
        if age<0:
            raise AgeException("Age less than zero exception")
        else:
             print("Age is valid") 
             
if __name__=="__main__":
    while True:
        age= int(input("enter your age:"))
        try:
            Age(age)
            break
        except AgeException:
            print("Exception occured and handled")
            
            
with open('saurav.csv','r') as file:
    line1 = file.readline() 
    line2 = file.readline() 
print(line1) # Prints the first line of the file 
print(line2) # Prints the second line of the file )


            