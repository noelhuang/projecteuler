grid_size = 21
grid = [[1 for _ in range(grid_size)] for _ in range(grid_size)]
for i in range(1, grid_size):
    for j in range(1, grid_size):
        grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
print(grid[grid_size - 1][grid_size - 1])
