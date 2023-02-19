# Exercise 1
print(*[x**2 for x in range(1,int(input()))])

# Exercise 2

print(*[x for x in range(1,int(input())+1) if x % 2 ==0])

# Exercise 3

print(*[x for x in range(0,int(input())+1) if x % 4 == 0 and x % 3 ==0])

# Exercise 4

def squares(a,b):
    for i in range(a,b+1):
        a = i**2
        yield a
        a += 1

result = squares(int(input()),int(input()))

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

for x in result:
    print(x)

# Exercise 5

print(*[i for i in reversed(range(int(input())+1))])




