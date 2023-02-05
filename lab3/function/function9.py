import math
from math import pow 
def func(r):
    radius = (4/3)* math.pi*pow(r,3)
    print(radius)

r = float(input())
func(r)