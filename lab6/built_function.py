"""
1.Write a Python program with builtin function to multiply all the numbers in a list/

2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters.

3. Write a Python program with builtin function that checks whether a passed string is palindrome or not. .

4.Write a Python program that invoke square root function after specific milliseconds. Sample Input: 25100 2123 Sample Output: Square root of 25100 after 2123 miliseconds is 158.42979517754858

5. Write a Python program with builtin function that returns True if all elements of the tuple are true
"""




# 1
from functools import reduce

def func(txt):
    return reduce(lambda x,y: (x+y)**2,txt)


txt = [1,2,3]
print(func(txt))

# 2
import string
string = input()
l_lower = []
l_upper = []
count1 = 0
count2 = 0
for i in string:
    if 'A' <= i <= 'Z':
        l_upper.append(i)
        count1 +=1
    elif 'a' <= i <= 'z':
        l_lower.append(i)
        count2 +=1

print(f'Upper Case: {count1}')
print(f'Lower Case: {count2}')

# Built Function

txt = input()
upper = 0
lower = 0
for i in txt:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1

print(f'Upper case: {upper}')
print(f'Lower case: {lower}')

# 3

import string
def Polindrome(txt):
    # string1 = string.lower().replace(' ','')
    string1 = ''.join(txt)
    first = 0
    last = len(txt)-1
    while first < last:
        if string1[first] ==string1[last]:
            first += 1
            last -= 1
        else:
            return  'String None Polindrome'
        return 'String Polindrome'
txt = input()
print(Polindrome(txt))

# 4
import time
import math

num = int(input('Input number: '))
millisecond = int(input('Input millesecond: '))
time.sleep(millisecond / 1000)

res = math.sqrt(num)
print(f'Square root of {num} after {millisecond} milliseconds is {res}')

# 5
def tup(tx):
    if not any(tx) or all(tx):
        return False
    return True
tx = (0, [1, 2, 3], (4, 5, 6), 7.0, 'knjbihuvgfc')
print(tup(tx))