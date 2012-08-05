import unittest
from pybot.irc import *

class EvaluatorTestCase(unittest.TestCase):

    def setUp(self):
        self.evaluator = Evaluator()

    def test_myexec_with_single_line_result(self):
        result = self.evaluator.myexec("print (1 + 1)")
        self.assertEquals("2\n", result)

        result = self.evaluator.myexec("print (1 + 2)")
        self.assertEquals("3\n", result)

    def test_myexec_with_multiple_lines_result(self):
        result = self.evaluator.myexec('print("line1\\nline2")')
        self.assertEquals("line1\nline2\n", result)

    def test_myexec_should_change_environment(self):
        self.evaluator.myexec('x = 1')
        result = self.evaluator.myexec('print(x)')
        self.assertEquals("1\n", result)

    def test_myexec_with_import(self):
        self.evaluator.myexec('from string import upper')
        result = self.evaluator.myexec('print upper("abc")')
        self.assertEquals("ABC\n", result)

    def test_myexec_with_def(self):
        code="""
def foo(n):
    return n
print foo(5)
"""
        result = self.evaluator.myexec(code)
        self.assertEquals("5\n", result)

    def test_eval_with_numerical_expression(self):
        result = self.evaluator.eval('1 + 2')
        self.assertEquals(3, result)

