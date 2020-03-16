import numpy as np

# make a new, 3x4 array from list of lists
bar = np.array([
    [5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60]
])

# return the element at position (1,2)
bar[1, 2]

# return row 1 as a 1d array
bar[0]

# return row 1 as a 2d array
bar[0, None]

# return the 2nd and 3rd columns in rows 2-3
bar[1:3, [-2, -1]]

# replace element (0, 0) with -1
bar[0, 0] = -1

# replace the 2nd row using the 3rd row
bar[1] = bar[2]

# insert 0s on diagonal
bar[[0, 1, 2], [0, 1, 2]] = [0, 0, 0]