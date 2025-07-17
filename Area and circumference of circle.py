import cmath
class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area= Circle.pi* radius*radius
    def get_circumference(self):
        return 2 * self.pi * self.radius
circle_1= Circle(5)
print(circle_1.get_circumference())
print(circle_1.area)
