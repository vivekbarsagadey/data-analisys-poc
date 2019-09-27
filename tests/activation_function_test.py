import unittest

from com.whiz.dap.mathplot.activation_function_plot import ActionFunctionProcesser , LINER ,NON_LINEAR

class LinerActivationFunctionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.afp = ActionFunctionProcesser(LINER)
    def test_is_linier(self):
        self.assertTrue(self.afp.is_linier(), 'is_linier return false ')

    def test_activation_function_name(self):
        self.assertEqual(self.afp.activation_function_name(), LINER, 'Liner function IS NOT ')

    def test_process(self):
        self.assertIsNotNone(self.afp.process(), "Processer Not define")
        self.afp.process().showLiner()


if __name__ == '__main__':
    unittest.main()
