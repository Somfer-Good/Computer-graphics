#Класс вектора
class vector:
    def __init__(self, x,y):
        self.X = x
        self.Y=y
    
    @property
    def x(self):        
        return self.X
     
    @property 
    def y(self):        
        return self.Y