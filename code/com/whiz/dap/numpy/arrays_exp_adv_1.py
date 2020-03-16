import numpy as np;


foo = np.array([1, 2, 3, 4, 5])
bar = np.array([0, 1, 0, 0, 1])

#baz = np.where((bar == 0), foo * 2.0, foo / 2.0)
np.where((bar==0), foo + 6, foo)
np.where((bar==0),  6, foo)
np.where((bar==0),  False, foo)


squee = np.array(
    [[5.0, 2.0, 9.0],
     [1.0, 0.0, 2.0],
     [1.0, 7.0, 8.0]]
)


np.sum(squee, axis =0)