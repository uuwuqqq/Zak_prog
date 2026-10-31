#1
class Rectangle:
    def __init__ (self,width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
    def scale(self,factor):
        self.vidth*=factor
        self.height*=factor
    def describe(self):
        return f" Obdelnik {self.width} x {self.height}, obsah: {self.area()}, perimeter: {self.perimeter()}"

rectangles=[
    Rectangle(5,7),
    Rectangle(8,2),
    Rectangle(10,5)
]

for i in rectangles:
    print(i.describe())
rectangle_max = max(rectangles, key=lambda r: r.area())
print(f" Nejvetsi obdelnik -{rectangle_max.describe()}")

#2
import math
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def length(self):
        return math.sqrt(self.x**2+self.y**2)
    def add(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)
    def scale(self,k):
        return Vector2D(self.x*k, self.y*k)
    def dot(self, other):
        return self.x*other.x+self.y*other.y
    def angle_to(self, other):
        soucin=self.dot(other)
        return math.acos(soucin/(self.length()*other.length()))
    def __str__(self):
        return f"({self.x}, {self.y})"
u = Vector2D(3, 4)
v = Vector2D(1, 0)
print(u, u.length())                    # (3, 4) 5.0
print(u.add(v))                         # (4, 4)
print(v.angle_to(Vector2D(0, 1)))       # 90.0

#3


    
    
    
    
    
    
    
    
    

