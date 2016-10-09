# -*- coding: utf-8 -*-

class PyEvaluator(object):
    @classmethod
    def create(cls):
        return cls()

    def eval(self, code, *args):
        return eval(code)(*args)
