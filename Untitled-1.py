#Write a function that calculates the area of a circle, given its radius. Write a function that calculates the area of a square, given its side length. Use your functions to answer the question: "Which has more area, a circle with radius 2 or a square with side length 3?
import math

class circle(): # practicing making classes
    def __init__(self, radius): 
        self.radius = radius
    def print_radius(self):
        print(self.radius)
    def c_area(self):
        return math.pi*self.radius*self.radius
c = circle(2)

class square():
    def __init__(self, side):
        self.side = side
    def print_side(self):
        print(self.side)
    def s_area(self):
        return self.side**2
s = square(3)

if c.c_area() > s.s_area():
    print(f"The circle has a greater area than the square.")
elif s.s_area() > c.c_area():
    print(f"The square has a greater area than the circle.")
else:
    print(f"The circle and square have the same area.")