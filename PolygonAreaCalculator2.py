class Shape:
    def __init__(self,sides):
        self.sides = sides
    
    def display(self):
        print(self.sides)
        
class Polygon(Shape):
    def __init__(self,sides,name,area):
        self.name = name
        self.area = area
        
        super().__init__(sides)
    
    def display2(self):
        print(self.name)
        print(self.area)
        
import math
Pentagon = Polygon(5,"Pentagon","1/4*sqrt(5*(5+(2*sqrt(5))))*s²")

Trapezium = Polygon(4,"Trapezium","h((a+b)/2)")