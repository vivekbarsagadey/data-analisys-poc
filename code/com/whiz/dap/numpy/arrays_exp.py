import numpy as np;

one_d = np.array(['a', 'b', 'c'])
print('np.array([])  > Get one dimension array > \n', one_d)
two_d = np.array([['a', 'b', 'c'], ['e', 'f', 'g']])
print(two_d)

zeor_2d = np.zeros(shape=(2, 3))
print(zeor_2d)

cats_2d = np.full(shape=(3, 4), fill_value='cat');
print(cats_2d)

arg = np.arange(start=2, stop=30, step=2)
print(arg)

rand = np.random.randint(low=2, high=9, size=(6, 4))
print(rand)

print('Length of rand is : ', len(rand))
print('Shape of rand is : ', rand.shape)

print('rand[:2]  > Get every element before index 2 > \n', rand[:2]);
print('rand[2:]  > Get every element after index 2  > \n', rand[2:]);
print('rand[::2] > Get every 2nd element            > \n', rand[::2]);
print('rand[2:6:2] > Get every 2nd element, start from2 and end 6th > \n', rand[2:6:2]);

# multi dimension array

bar = np.array([
    [5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60]
])

print('shape', bar.shape)
print(len(bar))
print(bar[1, 2])
print('means >> sum of all  / no of element ', bar.mean())
print('bar[[0, 1, 2], [0, 1, 2]]', bar[[0, 1, 2], [0, 1, 2]])


# basic operation
# make 2x2 arrays
print('basic operation\n')
foo = np.array([[4,3], [1,0]])
bar = np.array([[1,2], [3,4]])

print(foo)
print(bar)
print(foo + bar)
print(foo - bar)
print(foo * bar)
print(foo / bar)
print('matrix multiplication, you can use the @ operator')
print(foo @ bar)