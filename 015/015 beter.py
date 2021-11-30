import numpy as np

grid = np.ones((21, 21))

for i in range(1, 21):
    for j in range(1, 21):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid[20][20])

# With help from Frank
# Probably can be even faster by using Pascal's triangle formula
