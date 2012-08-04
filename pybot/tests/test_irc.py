import unittest
from pybot.irc import *

class EvaluatorTestCase(unittest.TestCase):

    def test_eval_with_single_line_result(self):
        evaluator = Evaluator()
        result = evaluator.eval("1 + 1")
        self.assertEquals([2], result)

        result = evaluator.eval("1 + 2")
        self.assertEquals([3], result)

    def test_eval_with_multiple_lines_result(self):
        evaluator = Evaluator()
        result = evaluator.eval("\"line1\\nline2\"")
        self.assertEquals(["line1","line2"], result)
