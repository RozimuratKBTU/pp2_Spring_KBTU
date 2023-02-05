
def spy_game(list):
    list2 = []
    for j in range(list):
        if j == 0 and j == 7:
            list2.apppend(j)
    k = ''.join(list2)
    if '007' == k:
        print("True")
    else:
        print('False') 

if __name__ == "__name__":
    list = []
    nums = int(input())
    for i in range(nums):
        a = input()
        list.append(a)
    spy_game(list)
    

