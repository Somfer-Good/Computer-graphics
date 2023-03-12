#Класс линии
class Line:
    def __init__(self, a,b,c):
        self.A = a
        self.B=b
        self.C=c
    
    @property 
    def a(self):       
        return self.A
    @property 
    def b(self):        
        return self.B
    @property 
    def c(self):        
        return self.C
