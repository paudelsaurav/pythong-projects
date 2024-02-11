class University:
    def __init__(self):
        self.name = "TU" 
    def display(self): 
        return ''f'in the university {self.name}''' 
    
class Branch(University):
    def __init__(self):
        University.__init__(self)
        self.brname="School of Mathematics"
        
    def display(self):
        return ''f'at the branch {self.brname} in {University.display(self)}'''
    
class Course(University): 
    def __init__(self): 
        University.__init__(self) 
        self.coname = "Acturial Science" 
 
    def display(self): 
        return ''f'is studying a course {self.coname}'''
    
class Student(Course, Branch):
    def __init__(self):
        Course.__init__(self)
        Branch.__init__(self)
        self.stname="Saurav"
        
    def display(self):
        print(f'The student {self.stname} {Course.display(self)} {Branch.display(self)}')
        
if __name__ == '__main__':
    student = Student()
    student.display()
         