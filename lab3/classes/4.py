import math

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Show(self):

        return self.x, self.y

    def Move(self, x, y):
        self.x += x
        self.x += y

    def Dist(self, C):
        subtract_x = C.x - self.x
        subtract_y = C.y - self.y

        return math.sqrt(subtract_x ** 2 - subtract_y**2)
















