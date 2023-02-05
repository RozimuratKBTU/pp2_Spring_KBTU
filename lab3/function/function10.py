def func(str):
    list = []
    for i in range(len(str)):
        
        if not str[i] in list:
            list.append(str[i])
    k = ''.join(list)
    print(k)
if __name__ == '__main__':
   str = input()
   func(str) 