import numpy as np

# simulate rolling a 6-sided die 3 times
np.random.randint(low=1, high=7, size=3)  # [1, 3, 2]

# set a random seed to get reproducible results
np.random.seed(2357)
np.random.randint(low=1, high=7, size=3)  # [2, 4, 1]
np.random.randint(low=1, high=7, size=3)  # [3, 1, 6]
np.random.seed(2357)
np.random.randint(low=1, high=7, size=3)  # [2, 4, 1]
np.random.randint(low=1, high=7, size=3)  # [3, 1, 6]

# draw three values between 1 and 6 without relpacement?
np.random.seed(2357)
np.random.choice(
    a = np.arange(1, 7),
    size = 3,
    replace = False,
    p = None
)  # [6, 5, 1]

# draw three values between 1 and 6 with probabilities
np.random.choice(
    a = np.arange(1, 7),
    size = 3,
    replace = False,
    p = np.array([0.1, 0.1, 0.1, 0.1, 0.3, 0.3])
)  # [5, 2, 6]

# draw three values from an array of strings
np.random.choice(
    a = np.array(['you', 'can', 'use', 'strings', 'too']),
    size = 3,
    replace = False,
    p = None
)  # ['use', 'you', 'can']

## Sample rows from a 2d array
foo = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
])

# with replacement
np.random.seed(1234)
rand_rows = np.random.randint(
    low=0,
    high=foo.shape[0],
    size=3
)  # [3, 4, 4]
foo[rand_rows]

# without replacement
rand_rows = np.random.choice(
    a=np.arange(start=0, stop=foo.shape[0]),
    replace=False,
    size=3
)  # [4, 2, 3]
foo[rand_rows]

# row-wise shuffle
np.random.permutation(foo)

## uniform() will give you values from a uniform distribution
np.random.uniform(low = 1.0, high = 2.0, size = (2, 2))

## normal() from a normal distribution
np.random.normal(loc = 0.0, scale = 1.0, size = 2)

## binomial() from a binomial distribution
np.random.binomial(n = 10, p = 0.25, size = (3, 2))

## If you want to see more distributions, check out
## https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.random.html
