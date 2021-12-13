file_name = "data/p067_triangle.txt"

with open(file_name) as file:
    pyramid = [[int(y) for y in x.split(" ")] for x in file.read().split("\n")]

for row in range(len(pyramid)):
    for col in range(row + 1):
        pyramid[row][col] = pyramid[row][col] + max(pyramid[row - 1][col - 1] if col > 0 else 0,
                                                   pyramid[row - 1][col] if col < row else 0)

print(max(pyramid[len(pyramid) - 1]))
