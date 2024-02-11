class Geom_series:
    def __iter__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r
        return self
    
    def __next__(self):
        term=self.a
        series=[term]
        for _ in range(self.r-1):
           term*=self.r
           series.append(term)
        return series
       
        
        
        
