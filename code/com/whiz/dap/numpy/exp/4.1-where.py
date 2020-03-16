import numpy as np

# make two 1d arrays, each with length 5
foo = np.array([1, 2, 3, 4, 5])
bar = np.array([0, 1, 0, 0, 1])

# create a third array called baz such that, where bar is 0, you double the corresponding value
# of foo, otherwise, you take half the corresponding value of foo. You might be inclined to do this with a for loop
baz = np.zeros(foo.shape[0])
for i in range(foo.shape[0]):
    if bar[i] == 0:
        baz[i] = 2 * foo[i]
    else:
        baz[i] = foo[i] / 2

# Use where() (vectorized solution)
baz = np.where((bar == 0), foo * 2.0, foo / 2.0)