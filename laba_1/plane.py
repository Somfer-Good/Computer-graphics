#Класс плоскости
class Plane:
    def __init__(self, a,b,c,d):
        self.A = a
        self.B=b
        self.C=c
        self.D=d
    
    @property 
    def a(self):       
        return self.A
    @property 
    def b(self):        
        return self.B
    @property 
    def c(self):        
        return self.C

    @property 
    def d(self):        
        return self.D