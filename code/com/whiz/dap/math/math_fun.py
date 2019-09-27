import numpy as np


class MathFunction:
    def __init__(self):
        print('init')

    def fx2(self,x):
        a = np.array(x)
        y = a * a
        return y

    def fx3(self,x):
        a = np.array(x)
        y = a * a * a
        return y

    def fsig(self,x):
        y = np.sin(x)
        return y

    def fsigh(self,x):
        y = np.sinh(x)
        return y

    def fcos(self,x):
        y = np.cos(x)
        return y

    def fcosh(self,x):
        y = np.cosh(x)
        return y

    def ftan(self,x):
        y = np.tan(x)
        return y

    def ftanh(self,x):
        y = np.tanh(x)
        return y

    def fexp(self,x):
        y = np.exp(x)
        return y

    def freexp(self,x):
        y = np.exp(-x)
        return y

    def fliner(self ,x , m = 5, c = -5):
        b = np.full((x.__len__()), m)
        print('m >', b)
        y = b * x + c
        return y
