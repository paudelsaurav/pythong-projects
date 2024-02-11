from datetime import date
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    def age_calculator(cls,name,birth_year):   #cls=Self@Student
         # calculate age an set it as a age 
        # return new object 
        return cls(name, date.today().year -birth_year)
        #Silmilar to return Student(name,age) 
    def show(self):
        print(self.name+ "'s age is :" +str(self.age))
        
st1=Student('Saurav',19)
st1.show()
st2=Student.age_calculator("Abhishek",2004) #Accesing class method
st2.show()

        