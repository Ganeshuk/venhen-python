class Shape:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return 'area'
    def perimenter(self):
        return "j"
class Rectangle(Shape):
    def __init__(self,height,width):
        super().__init__(height,width)
    def area(self):
        return self.height*self.width
    def perimenter(self):
        return (2*(self.height+self.width))
class Cricle(Shape):
    def __init__(self,height,width):
        super().__init__(height,width)
    def area(self):
        return self.height*self.width
    def perimenter(self):
        return (2*(self.height+self.width))
c=Cricle(12,2)
print(c.area()) 

