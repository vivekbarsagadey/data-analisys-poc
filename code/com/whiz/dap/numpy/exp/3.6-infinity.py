import numpy as np

# np.inf and np.NINF
np.array([np.inf, np.NINF])  # [ inf, -inf]

# more commonly, these values occur when you divide by 0
np.array([-1, 1])/0  # [-inf,  inf]

# behaviors
np.inf * 22  # inf
np.inf + np.inf # inf
np.inf - np.inf  # nan
np.inf / np.inf    # nan

# positive infinity equals positive infinity and negative infinity equals negative infinity
np.inf == np.inf   # True
np.NINF == np.NINF # True

# isolate infinite values by checking == positive infinity or == negative infinity
foo = np.array([4.4, np.inf, 1.0, np.NINF, 3.1, np.inf])
foo == np.inf  # [False,  True, False, False, False,  True]
foo == np.NINF # [False, False, False,  True, False, False]

# Alternatively,
np.isposinf(foo)  # [False,  True, False, False, False,  True]
np.isneginf(foo)  # [False, False, False,  True, False, False]
np.isinf(foo)     # [False,  True, False,  True, False,  True]