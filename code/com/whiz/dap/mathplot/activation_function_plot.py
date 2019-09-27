from com.whiz.dap.math.activation_fun import LinerActivationFunction ,NonLinerActivationFunction
import numpy as np
import matplotlib.pyplot as plt

LINER ="LINER"
NON_LINEAR ="NON_LINEAR"


class LinerActionFunctionProcesser:
    def __init__(self ):
        print("init ActionFunctionProcesser ")
        self.af = LinerActivationFunction()
    def showLiner(self):
        x = [3, 4, 5, 6]
        y = self.af.f(x)
        print("Y >>>>>>>>>>>>>>>>>> ",y)
        plt.axis([min(x) - 2, max(x) + 2, min(y) - 2, max(y) + 2])
        plt.plot(x, y)
        plt.ylabel('y numbers')
        plt.xlabel('x numbers')
        plt.show()

class NonLinerActionFunctionProcesser:

    def __init__(self ):
        print("init ActionFunctionProcesser ")
        self.plotIndex = 230
        self.af = NonLinerActivationFunction()
        plt.figure()

    def plotGraph(self,subplotnum, x, y, lable):
        plt.subplot(subplotnum)
        plt.axis([min(x) - 1, max(x) + 2, min(y) - 1, max(y) + 2])
        plt.plot(x, y)
        plt.ylabel(lable)
        plt.xlabel('x')
        plt.grid(True)
        print(y)

    def buildTanh(self):
        x = np.arange(-3, 3, 0.5)
        y = self.af.ftanh(x)
        print("Y >>>>>>>>>>>>>>>>>> ",y)
        self.plotIndex = self.plotIndex + 1
        self.plotGraph(self.plotIndex, x, y, 'tanh')
        return self

    def buildSigmoid(self):
        x = np.arange(-3, 3, 0.5)
        y = self.af.fsigmoid(x)
        print("buildSigmoid >>>>>>>>>>>>>>>>>> ",y)
        self.plotIndex = self.plotIndex + 1
        self.plotGraph(self.plotIndex, x, y, 'Sigmoid')
        return self


    def buildRelu(self):
        x = np.arange(-3, 3, 0.5)
        #x = np.sort([-3, 2, -4 , 8])
        y = self.af.frelu(x)
        print("buildRelu Y >>>>>>>>>>>>>>>>>> ",x,y)
        self.plotIndex = self.plotIndex + 1
        self.plotGraph(self.plotIndex, x, y, 'Relu')
        return self

    def buildLeakedRelu(self):
        x = np.arange(-3, 3, 0.5)
        #x = np.sort([-3, 2, -4 , 8])
        y = self.af.fleakedrelu(x,0.1)
        print("buildLeakedRelu Y >>>>>>>>>>>>>>>>>> ",x,y)
        self.plotIndex = self.plotIndex + 1
        self.plotGraph(self.plotIndex, x, y, 'Leaked Relu')
        return self

    def show(self):
        plt.show()
        return self



class ActionFunctionProcesser:
    def __init__(self , type=LINER):
        print("init LinerActionFunctionProcesser ")
        self.type = type
        if self.is_linier() :
            self.processer = LinerActionFunctionProcesser()
        else:
            self.processer = NonLinerActionFunctionProcesser()

    def is_linier(self):
        return True if self.type==LINER  else False

    def activation_function_name(self):
        return self.type

    def process(self):
        return self.processer


