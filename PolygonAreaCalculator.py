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
        
Rectangle = Polygon(4,"Rectangle","l*b")
Rectangle.display()
Rectangle.display2()

Triangle = Polygon(3,"Triangle","(l*b)/2")
Triangle.display()
Triangle.display2()