import numpy as np

#  4x3 array
bart = np.array([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
])

# add 5 to the 1st column, 3 to the 2nd column and 10 to the 3rd column
lisa = np.array([
    [5, 3, 10],
    [5, 3, 10],
    [5, 3, 10],
    [5, 3, 10]
])
bart + lisa

# Use broadcasting v1
bart + np.array([[5, 3, 10]])

# Use broadcasting v2
bart +  np.array([5, 3, 10])

# shift and scale array
np.array([1,2,3]) + 0.5  # [1.5, 2.5, 3.5]
np.array([1,2,3]) * -1   # [-1, -2, -3]

# try adding bart to a 4 element vector
bart + np.array([0, 0, 0, 0])  # error

## So how does broadcasting work and when can we use it?
## Suppose we want to add or multiply two arrays, A and B
## Moving backwards from the last dimension of each array, we check if their dimensions are compatible
## Dimensions are compatible they are equal or either of them is 1
## If all of A's dimensions are compatible with B's dimensions, or vice versa, they are compatible arrays

### Examples

# Example 1
np.random.seed(1234)
A = np.random.randint(low = 1, high = 10, size = (3, 4))
B = np.random.randint(low = 1, high = 10, size = (3, 1))

A.shape  # (3, 4)
B.shape  # (3, 1)
#           ^  ^
#         compatible

# Example 2
np.random.seed(4321)
A = np.random.randint(low = 1, high = 10, size = (4, 4))
B = np.random.randint(low = 1, high = 10, size = (2, 1))

A.shape  # (4, 4)
B.shape  # (2, 1)
#           ^  ^
#         not compatible


# Example 3
np.random.seed(1111)
A = np.random.randint(low = 1, high = 10, size = (3, 1, 4))
B = np.random.randint(low = 1, high = 10, size = (2, 1))

A.shape  # (3, 1, 4)
B.shape  # (   2, 1)
#           ^  ^  ^
#         compatible