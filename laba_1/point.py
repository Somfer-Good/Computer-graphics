#Класс точки
class Point:
    def __init__(self, x,y,z=0):
        self.X = x
        self.Y=y
        self.Z=z
    
    @property
    def x(self):        
        return self.X
     
    @property 
    def y(self):        
        return self.Y

    @property 
    def z(self):        
        return self.Z