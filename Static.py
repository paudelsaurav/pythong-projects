class Person: 
    count = 0 
 
    def __init__(self, name, sex='Male', age=20):    #default values, sex and age 
        Person.count = Person.count + 1      #count is static variable 
        self.name = name 
        self.sex = sex 
        self.age = age 
 
    @staticmethod        # Function decorator for static method 
    def countPerson():        # No self parameter because it is staticmethod 
        print('Number of person ->', Person.count) 
 
# Create 3 objects of Person class  
p1 = Person('Harendra') 
p2 = Person('Rajesh') 
p3 = Person('Rukmani', 'Female', 30) 
Person.countPerson()  # Call to static method countPerson() of Person Class

