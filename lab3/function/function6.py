
def func(str):
    for i in reversed(str.split()):
        print(i,end=" ")
        
        
if __name__ == "__main__":
    str = input()
    func(str)