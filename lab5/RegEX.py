import re
# 1
txt = input()
regex = re.search('^a(b*)$', txt)
if regex:
    print("True")
else:
    print("False")


# 2
txt = input()
regex = re.search('^a(b){2,3}&',txt)
if regex:
    print("True")
else:
    print("False")


# 3
txt = input()
regex = re.search('[a-z]{1}(_){1}', txt)
if regex:
    print("True")
else:
    print("False")


# 4
txt = input()
regex = re.search('^[A-Z]{1}([a-z]*)$',txt)
if regex:
    print("True")
else:
    print("False")


# 5
txt = input()
regex = re.search('a.(b{1})',txt)
if regex:
    print("True")
else:
    print("False")

# 6

txt = input()
regex = re.sub('[ ,.]', ":",txt)
print(regex)

# 7

list = []
txt = input()
camel = re.split('_', txt)
for i in camel:
    list.append(i.capitalize())
camel_case = "".join(list)
print(camel_case)

# 8

txt = input()
result = re.split('[A-Z]', txt)
print(result)

# 9

txt = input()
result = re.findall('[A-Z][a-z]*', txt)
for i in result:
    print(i, end = " ")


# 10
txt = str(input())
result = re.findall('[A-Z][a-z]*', txt)
for i in result:
    x = i.lower()
    print(x, end="_")