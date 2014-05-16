# -*- coding: utf-8 -*-
# nosetests tests/test_2_evaluating_simple_expressions.py --stop

from types import Environment, LispError, Closure
from ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_integer
from asserts import assert_exp_length, assert_valid_definition, assert_boolean
from parser import unparse

"""
This is the Evaluator module. The `evaluate` function below is the heart
of your language, and the focus for most of parts 2 through 6.

A score of useful functions is provided for you, as per the above imports, 
making your work a bit easier. (We're supposed to get through this thing 
in a day, after all.)
"""

def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""

    # evaluating booleans, integers, symbols and quotes
    if is_boolean(ast):
        return ast
    elif is_integer(ast):
        return ast
    elif is_symbol(ast):
        return ast
    elif ast[0] == "quote":
        return ast[1]

    # evaluating atom and eq functions
    if ast[0] == "atom":
        return is_atom(evaluate(ast[1], env))
    if ast[0] == "eq":
        aste = [evaluate(s, env) for s in ast[1:]]
        return is_atom(aste[0]) and aste[0] == aste[1]

    raise NotImplementedError("DIY")
