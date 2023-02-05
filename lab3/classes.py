
def Prime(number):

    for i in range(2, number // 2 + 1):
        if number % i == 0:
           return 0
    else:
        return 1


if __name__ =="__main__":
    number_of_list = [3,5,7,11,19,21,4,6,29]
    new_list = []

    for num in number_of_list:
        if num == 0 or num == 1:
            continue
        if Prime(num):
            new_list.append(num)
    if len(new_list):
        for ans in new_list:
            print(ans,end=',')
    else:
        print('No numbers from prime numbers,EMPTY')






