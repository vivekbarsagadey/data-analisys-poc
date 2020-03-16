import numpy as np

squee = np.array(
    [[5.0, 2.0, 9.0],
     [1.0, 0.0, 2.0],
     [1.0, 7.0, 8.0]]
)

# sum
np.sum(squee)  # 35.0

# sum over rows, columns
np.sum(squee, axis = 0)  # sum across axis 0 (column sums)
np.sum(squee, axis = 1)  # sum across axis 1 (row sums)

# keepdims
np.sum(squee, axis = 0, keepdims=True)  # [[ 7.,  9., 19.]]

# sum with nans
squee[0, 0] = np.nan
np.sum(squee)  # sum across axis 1 (row sums) nan

# sum excluding nans
np.sum(squee, where = ~np.isnan(squee))  # 30.0

# or..
np.nansum(squee)  # 30.0