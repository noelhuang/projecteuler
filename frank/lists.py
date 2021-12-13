import numpy as np

grid_3d = np.ones([3, 6, 3]).reshape([3, 3, 6], )
# print(grid_3d)

manual_3d = [[[1 for _ in range(3)] for _ in range(3)] for _ in range(3)]
# print(manual_3d)

sample_lists = [[1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 7]]
for path in sample_lists:
    for index, value in enumerate(path):
        print(f"{index}, {value}")
