# -*- coding: utf-8 -*-

"""
This module holds some types we'll have use for along the way.

It's your job to implement the Closure and Environment types.
The LispError class you can have for free :)
"""

class LispError(Exception): 
    """General lisp error class."""
    pass

class Closure:
    
    def __init__(self, env, params, body):
        raise NotImplementedError("DIY")

    def __str__(self):
        return "<closure/%d>" % len(self.params)

class Environment:

    def __init__(self, variables=None):
        self.variables = variables if variables else {}

    def lookup(self, symbol):
        if symbol in self.variables:
            return self.variables[symbol]
        else:
            raise LispError(format(symbol))

    def extend(self, variables):
        # The `extend` function returns a new environment,
        env = self.variables.copy()
        # extended with more bindings.
        extenv = dict(self.variables.items() + variables.items())
        return Environment(extenv)

    def set(self, symbol, value):
        raise NotImplementedError("DIY")
