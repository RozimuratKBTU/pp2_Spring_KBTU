# def Prime(num):
#     if num <= 1:
#         return False
#     for i in range(2,num):
#         if  num % i == 0:
#             return False
        
#     return True
    

# num = int(input())
# print(Prime(num))

def Prime(num):
    list = []
    for i in range(2,num+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            list.append(i)
    return list

print(Prime(int(input())))