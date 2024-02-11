class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def __str__(self):
        return"{0} has {1} salary".format(self.name,self.salary)
    
    def __gt__(self,other):
        if(self.salary>other.salary):
            name=self.name
            salary=self.salary
            
        else:
            name=other.name
            salary=other.salary
            
        return Employee(name,salary)
    
emp1=Employee("saurav",60000)
