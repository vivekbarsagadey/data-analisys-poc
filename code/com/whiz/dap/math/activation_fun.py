import numpy as np

# It is used to determine the output of neural network like yes or no.
# It maps the resulting values in between 0 to 1 or -1 to 1 etc. (depending upon the function).
from com.whiz.dap.math.math_fun import MathFunction


class LinerActivationFunction:
    def __init__(self):
        print('Liner Activation Function init')

    def f(self , x , b = 1, c = 0):
        m = np.full((x.__len__()), b)
        y = m * x + c
        return y

class NonLinerActivationFunction:
    def __init__(self):
        print('Liner Activation Function init')

    def ftanh(self , x ):
        y =MathFunction().ftanh(x)
        return y

    def fsigmoid(self , x ):
        b = np.full((x.__len__()), 1)
        ex = MathFunction().fexp(x)
        c =ex+b
        return ex/c

    def frelu(self , x ):
        X = list(map(lambda i: i if i > 0 else 0, x))
        return X
    def fleakedrelu(self , x , a=0.01):
        Y = list(map(lambda i: i if i > 0 else a*i, x))
        return Y



