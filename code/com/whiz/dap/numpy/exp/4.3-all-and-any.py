import numpy as np

foo = np.array([
    [np.nan, 4.4],
    [1.0, 3.2],
    [np.nan, np.nan],
    [0.1, np.nan]
])

# which rows have at least one nan value
mask = np.any(np.isnan(foo), axis = 1)
foo[mask]

# which rows have all nan values
mask = np.all(np.isnan(foo), axis = 1)
foo[mask]