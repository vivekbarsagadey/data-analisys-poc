import numpy as np;

print('broadcasting')

#  4x3 array
bart = np.array([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
])

# add 5 to the 1st column, 3 to the 2nd column and 10 to the 3rd column
lisa = np.array([
    [5, 3, 10],
    [5, 3, 10],
    [5, 3, 10],
    [5, 3, 10]
])

print(bart + np.array([[5, 3, 1]]))
print(bart + np.array([5, 3, 1]))

# shift and scale array
np.array([1, 2, 3]) + 0.5  # [1.5, 2.5, 3.5]
np.array([1, 2, 3]) * -1  # [-1, -2, -3]

# Example 1
np.random.seed(1234)
A = np.random.randint(low=1, high=10, size=(3, 4))
B = np.random.randint(low=1, high=10, size=(3, 1))

print(A + B)

print("newaxis >>>>>>>>>>>> \n")

# make 1d arrays
A = np.array([3, 11, 4, 5])
B = np.array([5, 0, 3])

# Deduct each element of B from each element of A
A[np.newaxis, :] - B[:, np.newaxis]

# Same as above, using None
A[None, :] - B[:, None]

print('A            ----------->\n', A)
print('A[None, :]   ----------->\n', A[None, :])
print('A[:, None])  ----------->\n', A[:, None])

print('reshape >>>>>>>>>>>>>>>>>> ')
foo = np.arange(start=1, stop=9)
print(foo.reshape((2, 4)))

# reshape into a 2x4 array using either the .reshape method of the array object, or the free function np.reshape()
bar = foo.reshape((2, 4))
bar = np.reshape(a=foo, newshape=(2, 4))

## reshape bar from a 2x4 array to a 4x2 array
# C-style order reorders the last axis first
bar.reshape((4, 2), order='C')

# Fortran-style order reorders the first axis first
bar.reshape((4, 2), order='F')

# matrix transpose of bar
bar.T

# reshape foo into higher dimensions, like a 2x2x2 array
bar.reshape((2, 2, 2))

# use -1 for exactly one of the newshape dimensions and numpy will calculate it for you
bar.reshape((-1, 2))

mask = bar == 3
print(mask)

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

# bot, 2 missing values
bot = np.ones(shape=(3, 4))
bot[[0, 2], [1, 2]] = np.nan

# np.inf and np.NINF
np.array([np.inf, np.NINF])  # [ inf, -inf]

np.random.seed(2357)
np.random.randint(low=1, high=7, size=3)  # [2, 4, 1]
np.random.randint(low=1, high=7, size=3)  # [3, 1, 6]

# draw three values between 1 and 6 without relpacement?
np.random.seed(2357)
np.random.choice(
    a=np.arange(1, 7),
    size=3,
    replace=False,
    p=None
)

## uniform() will give you values from a uniform distribution
np.random.uniform(low=1.0, high=2.0, size=(2, 2))

## normal() from a normal distribution
np.random.normal(loc=0.0, scale=1.0, size=2)

## binomial() from a binomial distribution
np.random.binomial(n=10, p=0.25, size=(3, 2))
