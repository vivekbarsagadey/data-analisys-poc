import numpy as np

foo = np.array(['a', 'b'])
bar = np.array(['c', 'd'])
baz = np.array([['e', 'f']])
bingo = np.array([['g', 'h', 'i']])
bongo = np.array(
    [['j', 'k'],
     ['l', 'm']]
)

# vstack foo and bar
np.vstack((foo, bar))

# vstack foo, bar, and baz
np.vstack((foo, bar, baz))

# vstack baz and bingo
np.vstack((baz, bingo))  # error

# hstack foo and bar
np.hstack((foo, bar))

# hstack baz and bingo
np.hstack((baz, bingo))

# hstack foo and bingo
np.hstack((foo, bingo))  # error

# hstack bingo and bongo
np.hstack((bingo, bongo))  # error

# stack foo and bar along axis 0
np.stack((foo, bar), axis = 0)

# stack foo and bar along axis 1
np.stack((foo, bar), axis = 1)

# stack foo and bar along axis 2
np.stack((foo, bar), axis = 2)  # error

# Use the shortcut axis = -1 to insert the new axis behind the last existing axis
np.stack((foo, bar), axis = -1)