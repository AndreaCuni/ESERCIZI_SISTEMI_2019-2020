d = {1:[1,2],2:[2,4]}

grid = [[True, True, True, True, True, False],
    [False, False, True, True, True, False],
    [True, True, True, False, True, True],
    [True, False, False, True, True, False],
    [True, False, True, True, False, True],
    [True, False, True, True, True, False]]


n = 1
defM = []
matrix = []

for i in grid:
    matrix = []
    for x in i:
        if (x == True):
            matrix.append(n)
            n=n+1
        else: 
            matrix.append(-1) 
    defM.append(matrix)

print (defM)