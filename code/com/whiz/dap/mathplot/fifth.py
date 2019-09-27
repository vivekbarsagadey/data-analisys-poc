import matplotlib.pyplot as plt
import numpy as np
names = ['group_a','group_b','group_c']
values = np.random.randint(0,100,names.__len__())

plt.figure(figsize=(10, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()

