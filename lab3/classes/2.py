class Shape(object):
    def __init__(self):
        pass

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length


    def area(self):
        return self.length ** 2

input_Square = Square(int(input()))
print(input_Square.area())

