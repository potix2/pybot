# -*- encoding: utf-8 -*-

class Evaluator():
    def eval(self, expr):
        result = eval(expr)
        if type(result) == str:
            return result.split('\n')
        else:
            return [result]

class PyBot(object):
    def action(self, user, channel, msg):
        self.msg(channel, "2")

    def msg(self, channel, msg):
        pass
