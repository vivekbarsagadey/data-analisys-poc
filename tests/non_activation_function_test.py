import unittest

from com.whiz.dap.mathplot.activation_function_plot import ActionFunctionProcesser , LINER ,NON_LINEAR

class NonLinerActivationFunctionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.afp = ActionFunctionProcesser(NON_LINEAR)

    def test_is_linier(self):
        self.assertFalse(self.afp.is_linier(), 'this is not NON_LINEAR fucntion ')

    def test_activation_function_name(self):
        self.assertEqual(self.afp.activation_function_name(), NON_LINEAR, 'Liner function IS NOT ')

    def test_process(self):
        self.assertIsNotNone(self.afp.process(), "Processer Not define")
        self.afp.process().buildTanh().buildSigmoid().buildRelu().buildLeakedRelu().show()



if __name__ == '__main__':
    unittest.main()
