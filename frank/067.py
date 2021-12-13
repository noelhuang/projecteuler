file_name = "data/p067_triangle.txt"

with open(file_name) as file:
    pyramid = [[int(y) for y in x.split(" ")] for x in file.read().split("\n")]

result = [[0 for _ in range(i + 1)] for i in range(len(pyramid))]

for row in range(len(pyramid)):
    for col in range(row + 1):
        result[row][col] = pyramid[row][col] + max(result[row - 1][col - 1] if col > 0 else 0,
                                                   result[row - 1][col] if col < row else 0)

print(max(result[len(pyramid) - 1]))
