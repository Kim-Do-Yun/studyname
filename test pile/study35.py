class Circle:
    def __init__ (self, radius):
        self.radius = radius
    def clacPerimeter(self):
        return self.radius*3.14*2
    def clacarea(self):
        return 3.14*self.radius**2
    def __str__(self) :
        return "radius = " + str(self.radius)

myCircle = Circle(100)
print(myCircle.clacPerimeter())
print(myCircle.clacarea())

print(myCircle)