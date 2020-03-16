import numpy as np

# 3x3 array of positive integers. we want tocreplace every 3 with 0
foo = np.array([
    [3, 9, 7],
    [2, 0, 3],
    [3, 3, 1]
])

# Checking foo == 3, numpy gives us a 3x3 array of boolean values
mask = foo == 3

# Now we can use this array of boolean values to index our original array, identify which elements are 3
foo[mask]
foo[mask] = 0
foo

# use 1d boolean arrays to pick out specific rows or columns
rows_1_and_3 = np.array([True, False, True])
cols_2_and_3 = np.array([False, True, True])
foo[rows_1_and_3]  # returns rows 1 and 3
foo[:, cols_2_and_3]  # returns cols 2 and 3

## Be careful about using multiple boolean indexes together
foo[rows_1_and_3, cols_2_and_3] # equivalent to foo[[0,2], [1,2]]

# --- logical operators ---------------------------------------

# combine boolean arrays using bitwise operators
b1 = np.array([False, False, True, True])
b2 = np.array([False, True, False, True])
b1 & b2  # [False, False, False,  True]  # and
b1 | b2  # [False,  True,  True,  True]  # or
b1 ^ b2  # [False,  True,  True, False]  # xor

# negation
~np.array([False, True])

# Examples
names = np.array(["Dennis", "Dee", "Charlie", "Mac", "Frank"])
ages = np.array([43, 44, 43, 42, 74])
genders = np.array(['male', 'female', 'male', 'male', 'male'])

# Who's at least 44?
names[ages >= 44]

# Which males are over 42?
names[(genders == "male") & (ages > 42)]

# Who's a not a male or younger than 43?
names[~(genders == "male") | (ages < 43)]