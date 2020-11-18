import matplotlib.pyplot as plt # comprehensive library for creating static, animated, and interactive visualizations in Python.

class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self, other): # building another point type, asssuming other is another point
        if isinstance(other, Point): # (object,type) if instance is object 'other' of type 'Point' class
            x = self.x + other.x # 
            y = self.y + other.y # 
            return Point(x,y) # return new coordinates of (x + x) and (y + y) 
        else: # account for integers and floats
            x = self.x + other 
            y = self.y + other
            return Point(x,y)

    def plot(self):
        plt.scatter(self.x, self.y)


point1 = Point(4,5)
print(point1.x)

# a = Point(3,4)
# a.plot()

# Operator overide for 'adding' new coordinates 
# a = Point(1,3)
# b = Point(2,2)
# c = a + b
# print(c.x, c.y) 

a = Point(0,2)
c = a + 5
d = a + Point(1,2)
print(c.x, c.y)
print(d.x, d.y)

plt.show() # enable to see graph


# Operater overload to override the 'add' operator for point class