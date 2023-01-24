# Intro
print("Hello World")

# Syntax
if 5 > 2:
  print("Five is greater than two!")

if 5 > 2:
print("Five is greater than two!") #This is error

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
# ERROR
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")

# comments
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# VAriables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))


x = "John"
# is the same as
x = 'John'

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"
# 

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
# 
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# 
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
# 
x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = 20

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# 

x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = ("apple", "banana", "cherry")

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = range(6)

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = {"apple", "banana", "cherry"}

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# 
x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# f
x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# f
x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# 
x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# 
x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# 
x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# 
x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# 
x = None

#display x:
print(x)

#display the data type of x:
print(type(x)) 
# ;;
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
# flfllf
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# kkfkf
a = "Hello, World!"
print(a[1])
for x in "banana":
  print(x)
#   kfllf
txt = "The best things in life are free!"
print("free" in txt)
# ,fkf
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#   kflf

b = "Hello, World!"
print(b[2:5])
# lf
b = "Hello, World!"
print(b[:5])
# kkf
b = "Hello, World!"
print(b[2:])
# kf
b = "Hello, World!"
print(b[-5:-2])
# fkkf'
a = "Hello, World!"
print(a.upper())
# lkf
a = "Hello, World!"
print(a.lower())
# lof
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!
# lf

a = "Hello, World!"
print(a.replace("H", "J"))
# lf
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# 
age = 36
txt = "My name is John, I am " + age
print(txt)
# kkf
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# mflf
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# kflf
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# kd;d
# ESCAPE CHARACTERS

txt = 'It\'s alright.'
print(txt) 

txt = "Hello\nWorld!"
print(txt) 

txt = "Hello\rWorld!"
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

# BOOOLEANS
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


x = 200
print(isinstance(x, int))
# LIST



thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#   lflf

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# lff


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# ;f
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
# lff
newlist = [x for x in fruits if x != "apple"]
# ;d'd
newlist = [x for x in fruits]
# f;f
newlist = [x for x in range(10) if x < 5]

# c
newlist = ['hello' for x in fruits]
# lf

newlist = [x if x != "banana" else "orange" for x in fruits]
# lf'

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# lflf
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# lf;f

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# ;f

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
# lclc
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# lf;fmf
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# kflfkmf
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# llflf
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# lfkf
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# fff
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# lffflf
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
# lf;f
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
# f;f
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# flff

# IF ELSE

a = 33
b = 200
if b > a:
  print("b is greater than a")
#   kf
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

# lff
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#   lflf

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#   kkf
a = 2
b = 330
print("A") if a > b else print("B")
# mf
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# kfmlf
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#   kff
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    # kflff
a = 33
b = 200

if b > a:
  pass
#   kflf




