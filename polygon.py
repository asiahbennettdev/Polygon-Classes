import turtle # python drawing board module

""" Define polygon by certain amount of sides or name """
class Polygon: # trianlges, squares, pentagons, hexagons, ect. 
    def __init__(self, sides, name, size=100, color="blue", line_thinckness=3): # initialize with parameters - whats import to a polygon? 
        self.sides = sides 
        self.name = name 
        self.size = size
        self.color = color
        self.line_thickness = line_thinckness
        self.interior_angles = (self.sides - 2)*180 # find sum of all interior angles. number of sides -2 * 180 - (n-2)*180
        self.angle = self.interior_angles/self.sides # EX: sum of interior angle for square is 360 each angle is 90 degrees
    
    def draw(self): # can access parameters of Polygon class by passing in self 
        turtle.pensize(self.line_thickness)
        turtle.color(self.color)
        for i in range(self.sides):
            turtle.forward(self.size) 
            turtle.right(180-self.angle) # defining exterior andgle insert 180-self.sides, finding supplement of interior angles 
        #turtle.done()

def draw_function(sides, size, angle, line_thickness, color):
    turtle.pensize(line_thickness)
    turtle.color(color)
    for i in range(sides):
        turtle.forward(size) 
        turtle.right(180-angle) 
    turtle.done()

class Square(Polygon):
    def __init__(self, size=100, color="black", line_thickness=3):
        super().__init__(4, "Square", size, color, line_thickness)
    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()
# override draw method
    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()

square = Square(color="#321abc", size=200)
print(square.draw())
turtle.done()

# DEFINING SHAPES

# square = Polygon(4, "Square") # based on what was initalized in __init_ pass in parameters
# pentagon = Polygon(5, "Pentagon", color="red", line_thinckness=25) # size not provided defaults to 100
# hexagon = Polygon(6, "Hexagon", 10) #size gives tiny hexagon 

# print(square.sides) # prints 4
# print(square.name) # prints Square
# print(square.interior_angles) # prints 360
# print(square.angle) # prints 90
# print(pentagon.name) # prints 5
# print(pentagon.sides) # prints Pentgon

# pentagon.draw() 
# hexagon.draw()
# square.draw()
# draw_function(4, 50, 90, 4, "pink") # not utilizing predefined class methods



# NOTES
# self - allows us to access everything we've intialized in the class Polygon in nice succinct manner 
# inheritance - subclassing - define class specifically
# we have created a polygon class we set sides and name through __init__ method by feeding in parameters
# encapsulating information from Polygon class 