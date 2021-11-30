from random import random

temppath = []

paths = []

gridsize = 2

for j in range(1, 10000):
    for i in range(1, (2*gridsize)+1):
        num = random()
        if num > 0.5:
            if temppath.count('r') >= gridsize:
                temppath.append('d')
            else:
                temppath.append('r')

        else:
            if temppath.count('d') >= gridsize:
                temppath.append('r')
            else:
                temppath.append('d')
    temptuple = tuple(temppath)
    paths.append(temptuple)
    temppath = []

print(paths)
print(f"{len(paths)} is path number with duplicates")
nodupepaths = set(paths)
print(f"{len(nodupepaths)} is path number with no duplicates")