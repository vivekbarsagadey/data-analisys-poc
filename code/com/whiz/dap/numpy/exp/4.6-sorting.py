import numpy as np


# sort a 1d array in ascending order
foo = np.array([1, 7, 3, 9, 0, 9, 1])
np.sort(foo)

# If you have an array with nan values, sort pushes them to the end of the array
bar = np.array([5, np.nan, 3, 11])
np.sort(bar)  # [ 3.,  5., 11., nan]

# sort an array in descending order
np.sort(bar)[::-1]  # reverse the sorted array
-np.sort(-bar)      # negate the sorted values of the negated array

# If you need a stable sorting algorithm, set kind = 'stable'
np.sort(np.array([2, 1, 3, 2]), kind='stable')

# sort on a 2d array
boo = np.array([
    [10, 55, 12],
    [0, 81, 33],
    [92, 11, 3]
])
np.sort(a = boo, axis = 0)   # sorts along the row axis
np.sort(a = boo, axis = 1)   # sorts along the column axis
np.sort(a = boo, axis = -1)  # (default) sorts along the last axis (in this case, the column axis)

# sort the rows of foo based on the values in the 1st column
boo[np.array([1, 0, 2])]

# argsort()
goo = np.array([3, 0, 10, 5])  # [3, 0, 10, 5]
np.argsort(goo)                # [1, 0,  3,  2]
np.sort(goo)                   # [0, 3,  5  10]

# sort a 2d array's rows based on a certain column
boo[np.argsort(boo[:, 1])]   # sort by column 1 ascending
boo[np.argsort(-boo[:, -1])]  # sort by last column, descending