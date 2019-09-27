# create line function
# y = mx+c
import numpy as np
import matplotlib.pyplot as plt
print(np.arange(1, 5.0, 0.1))
print(np.full((4), 5))


def f(x):
    m = np.full((x.__len__()), 5)
    print('m >', m)
    c = -5
    y = m*x+c
    return y



x= [3,4,5,6]

y = f(x)
print(y)
plt.axis([min(x)-2, max(x)+2, min(y)-2, max(y)+2])
plt.plot(x,y)
plt.ylabel('y numbers')
plt.xlabel('x numbers')
plt.show()
