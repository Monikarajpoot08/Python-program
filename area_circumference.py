class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.pi*self.radius**2
    def circumference(self):
        return self.pi*2*self.radius
obj1=Circle(5)
print(obj1.area())
print(obj1.circumference())
