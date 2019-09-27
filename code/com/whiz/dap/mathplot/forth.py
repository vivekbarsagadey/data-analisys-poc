import matplotlib.pyplot as plt
import numpy as np

print(np.arange(10))
print(np.random.randn(10))
print(np.random.randint(0, 50, 2))
numberOfDi = 50
data = {'a': np.arange(numberOfDi),
        'c': np.random.randint(0, 50, numberOfDi),
        'd': np.random.randn(numberOfDi)}
data['b'] = data['a'] + 10 * np.random.randn(numberOfDi)
data['d'] = np.abs(data['d']) * 100


plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()