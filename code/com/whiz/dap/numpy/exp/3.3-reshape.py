import numpy as np

# Suppose we have the following 1d array with 8 elements
foo = np.arange(start = 1, stop = 9)  # [1, 2, 3, 4, 5, 6, 7, 8]

# reshape into a 2x4 array using either the .reshape method of the array object, or the free function np.reshape()
bar = foo.reshape((2,4))
bar = np.reshape(a = foo, newshape = (2,4))

# slightly different interfaces
foo.reshape(2,4)  # allowed
foo.reshape(newshape = (2,4))  # error

## reshape bar from a 2x4 array to a 4x2 array
# C-style order reorders the last axis first
bar.reshape((4,2), order = 'C')

# Fortran-style order reorders the first axis first
bar.reshape((4,2), order = 'F')

# matrix transpose of bar
bar.T

# reshape foo into higher dimensions, like a 2x2x2 array
bar.reshape((2,2,2))

# reshape foo into 2x2x3 array
bar.reshape((2,2,3)) # error

# use -1 for exactly one of the newshape dimensions and numpy will calculate it for you
bar.reshape((-1, 2))