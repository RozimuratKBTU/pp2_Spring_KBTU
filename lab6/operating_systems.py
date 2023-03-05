"""

1. Write a Python program to list only directories, files and all directories, files in a specified path.

2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path.

3. Write a Python program to test whether a given path exists or not. If the path exists find the filename and directory portion of the given path.

4. Write a Python program to count the number of lines in a text file.

5. Write a Python program to write a list to a file.

6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt .

7. Write a Python program to copy the contents of a file to another file.

8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not
"""

import os
# 1
path = os.getcwd()
print('Directors: ')
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)
print('\nFiles: ')
for j in os.listdir(path):
    if os.path.isfile(os.path.join(path, j)):
        print(j)
print('\nAll Directors and Files: ')

for index, folder,file in os.walk(path):
    for i in folder:
        print(os.path.join(index, i))
    for j in file:
        print(os.path.join(index, j))
# 2

path = input()
print(path)
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))
print(os.path.exists(path))

# 3
path = input()
a = os.path.exists(path)
print(a)
b = os.path.basename(path)
print(b)
s = os.path.dirname(path)
print(s)
# 4
path = input()

with open(path, 'r') as re:
    x = len(re.readlines())
    print('Total lines:', x)
# 5

list1 = ['Rozimurad', 'Mango', 'Banana', 'Samandar','KBTU']
path = 'b.txt'
with open(path, 'w') as wr:
    wr.writelines(f'{list1}\t')
wr.close()
#6
import string

for i in string.ascii_uppercase:
    with open(f'{i}.txt', 'w') as file:
        file.write(f'{i}')

file.close()

# 7
with open('aka.txt') as f:
    with open('b.txt', 'w') as f2:
        for i in f:
            f2.write(i)
f.close()
#Second way

import shutil
shutil.copy('aka.txt','b.txt')

# 8
import os

path = input()

path2 = os.getcwd()

print(os.path.exists(path))

print(os.path.exists(path2))

os.remove(path)

os.remove(path2)


