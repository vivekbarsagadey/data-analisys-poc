import numpy as np

foo = np.array(['b', 'b', 'a', 'a', 'c', 'c'])

# get uniques
np.unique(foo)   # ['a', 'b', 'c', 'nan']

# get uniques sorted by first occurrence
uniques, first_positions = np.unique(foo, return_index = True)
uniques[np.argsort(first_positions)]  # ['b', 'a', 'c']

# get uniques with counts
np.unique(foo, return_counts=True)