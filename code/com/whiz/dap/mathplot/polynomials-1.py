import numpy as np
import matplotlib.pyplot as plt

from com.whiz.dap.math import math_fun


class MathGraph:
    def __init__(self,plt):
        self.plt =plt
        print('init')

    def plotGraph(self,subplotnum, x, y, lable):
        self.plt.subplot(subplotnum)
        self.plt.axis([min(x) - 1, max(x) + 2, min(y) - 1, max(y) + 2])
        self.plt.plot(x, y)
        self.plt.ylabel(lable)
        self.plt.xlabel('x')
        self.plt.grid(True)
        print(y)

    def fx2(self,x):
        a = np.array(x)
        y = a * a
        return y




# x= [3,4,5,6]
mathFunction = math_fun.MathFunction();
mathGraph = MathGraph(plt)
x = np.arange(-5, 5.0, 0.1)
print(x)

plt.figure()
i = 231;
mathGraph.plotGraph(i, x, mathFunction.fx2(x), '')
mathGraph.plotGraph(i, x, mathFunction.fx3(x), 'y = x pow 2 and 3')
i = i + 1
mathGraph.plotGraph(i, x, mathFunction.fsig(x), '')
mathGraph.plotGraph(i, x, mathFunction.fcos(x), 'y = sin(x)/cos(x)')
i = i + 1
mathGraph.plotGraph(i, x, mathFunction.fsigh(x), '')
mathGraph.plotGraph(i, x, mathFunction.fcosh(x), 'y = sinh(x)/cosh(x)')
i = i + 1
mathGraph.plotGraph(i, x, mathFunction.ftan(x), '')
mathGraph.plotGraph(i, x, mathFunction.ftanh(x), 'y = tan(x)/tanh(x)')
i = i + 1
mathGraph.plotGraph(i, x, mathFunction.fexp(x), '')
mathGraph.plotGraph(i, x, mathFunction.freexp(x), 'y = exp(x)/-exp(x)')

plt.show()
