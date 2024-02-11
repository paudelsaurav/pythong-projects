class EvenNumbers:
    def __iter__(self):
        self.a=2
        return self
    
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a += 2
            return x
        else:
            raise StopIteration
        
evenObj=EvenNumbers()
evenIter=iter(evenObj)  #making it iterable
print("The even numbers between 1 and 20 are as follows;") 
for x in evenIter: 
  print(x) 

            