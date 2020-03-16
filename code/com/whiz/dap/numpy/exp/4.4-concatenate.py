import numpy as np

roux = np.zeros(shape = (3, 2))
gumbo = np.ones(shape = (2,2))

# combine roux with a couple copies of itself row-wise
np.concatenate((roux, roux, roux), axis = 0)

# column-wise
np.concatenate((roux, roux, roux), axis = 1)

# combine roux and gumbo row-wise
np.concatenate((roux, gumbo), axis = 0)

# combine them column-wise
np.concatenate((roux, gumbo), axis = 1)  # error