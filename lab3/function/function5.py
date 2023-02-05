

from itertools import permutations 
def func(s): 
    a = permutations(s)
    for i in list(a):
        print(list("".join(i)))
    print(len(list(permutations(i))))

if __name__ == "__main__":
    s = input()
    func(s)