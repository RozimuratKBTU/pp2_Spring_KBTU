def histogram(list):
    for i in list:
        print(i * "*")
    print('')
if __name__ == "__main__":
    list = []
    n = int(input())
    for i in range(1,n+1):
        c = int(input())
        list.append(c)
    histogram(list)