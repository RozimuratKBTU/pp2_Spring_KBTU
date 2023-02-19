# Exersice 1
import math

num = float(input())
print(math.radians(num))

# Exersice 2

import math

Height = float(input('Height: '))
wegth = float(input('Base, first value: '))
length = float(input('Base, second value: '))
trape = (wegth+length)*Height/2
print(trape)

# Exersice 3

import  math
n = float(input('Input number of sides: '))
s = float(input('Input the length of a side: '))

area = (n * pow(s,2))/ 4 * math.tan(math.pi / n)
print(f"The area of the polygon is: {area}")

# Exersice 4

import math
l =float(input('Length of base: '))
h = float(input('Height of parallelogram: '))
area = l * h
print(f'Expected Output: {area}')




