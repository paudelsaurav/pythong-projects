class Animal:  #base class
    def __init__(self):  #constructor
        print(''f'I am {self.__class__}'''+"\n")
        
class Tiger(Animal):  # derived class level 1 
    def __init__(self, voice):   # constructor 
        self.voice = voice 
        super().__init__()  # calling base constructor 
 
    def sound(self):  #method
        return ''f'I {self.voice} when gets angry'''
    
class Dog(Animal):  #derived class level 2
    def __init__(self,voice):
        self.voice = voice
        super().__init__()  #calling base constructor
    def sound(self):  # method overriding 
        return ''f'I {self.voice} when gets angry and hungry''' 
 
# Main function 
if __name__ == '__main__':  # executing the code from the current file 
    t = Tiger("Roar") 
    print(t.sound()) 
    d = Dog("Bark") 
    print(d.sound()) 
    
    
