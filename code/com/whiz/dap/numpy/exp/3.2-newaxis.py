import numpy as np

# make 1d arrays
A = np.array([3, 11, 4, 5])
B = np.array([5, 0, 3])

# Deduct each element of B from each element of A
A[np.newaxis, :] - B[:, np.newaxis]

# Same as above, using None
A[None, :] - B[:, None]