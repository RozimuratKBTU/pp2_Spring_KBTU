class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width



input_Rectangle = Rectangle(int(input()),int(input()))
print(input_Rectangle.area())