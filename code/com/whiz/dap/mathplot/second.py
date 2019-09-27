import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [1, 2, 6, 7]

plt.plot(x,y,'ro')

# axis -- [xmin, xmax, ymin, ymax]
plt.axis([0, max(x)+2, 0, max(y)+2])
plt.ylabel('y numbers')
plt.xlabel('x numbers')
plt.show()