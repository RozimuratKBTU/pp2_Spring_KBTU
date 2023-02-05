def solve(numheads,numlegs):
    for i in range(36):
        for j in range(95):
            if i + j == numheads and 2*i + 4*j == numlegs:
                return i,j

numheads = 35
numlegs = 94
print(solve(35,94))