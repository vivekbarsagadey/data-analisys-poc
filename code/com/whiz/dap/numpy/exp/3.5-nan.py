import numpy as np

# bot, 2 missing values
bot = np.ones(shape = (3, 4))
bot[[0, 2], [1, 2]] = np.nan
bot

# check bot == np.nan
bot == np.nan

# Be careful
np.nan == np.nan  # False
np.nan != np.nan  # True


# which elements of bot are nan?
np.isnan(bot)

# only works for for arrays of floats
foo = np.array([1, 2, 3], dtype = 'int64')
foo[1] = np.nan  # error