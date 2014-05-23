__author__ = 'Zsuzsanna'
# -*- coding: utf-8 -*-

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
        return env.lookup(ast)
    elif ast[0] == "quote":
        return ast[1]

    # everything else is of list form
    elif is_list(ast):

        # evaluating atom and eq functions
        if ast[0] == "atom":
            return is_atom(evaluate(ast[1], env))
        elif ast[0] == "eq":
            aste = [evaluate(s, env) for s in ast[1:]]
            return is_atom(aste[0]) and aste[0] == aste[1]

        # evaluating basic math operators
        elif ast[0] == "+":
            if is_integer(evaluate(ast[1], env)) and is_integer(evaluate(ast[2], env)):
                return evaluate(ast[1], env) + evaluate(ast[2], env)
            else:
                raise LispError('Arguments must be integers')

        elif ast[0] == "-":
            if is_integer(evaluate(ast[1], env)) and is_integer(evaluate(ast[2], env)):
                return evaluate(ast[1], env) - evaluate(ast[2], env)
            else:
                raise LispError('Arguments must be integers')

        elif ast[0] == "*":
            if is_integer(evaluate(ast[1], env)) and is_integer(evaluate(ast[2], env)):
                return evaluate(ast[1], env) * evaluate(ast[2], env)
            else:
                raise LispError('Arguments must be integers')

        elif ast[0] == "mod":
            if is_integer(evaluate(ast[1], env)) and is_integer(evaluate(ast[2], env)):
                return evaluate(ast[1], env) % evaluate(ast[2], env)
            else:
                raise LispError('Arguments must be integers')

        elif ast[0] == "/":
            if is_integer(evaluate(ast[1], env)) and is_integer(evaluate(ast[2], env)):
                return evaluate(ast[1], env) / evaluate(ast[2], env)
            else:
                raise LispError('Arguments must be integers')

        elif ast[0] == ">":
            return evaluate(ast[1], env) > evaluate(ast[2], env)
        elif ast[0] == "<":
            return evaluate(ast[1], env) < evaluate(ast[2], env)

        # Evaluating complex expressions

        # basic if statement
        elif ast[0] == 'if':
            if (evaluate(ast[1], env)) is True:
                return evaluate(ast[2], env)
            else:
                return evaluate(ast[3], env)

        # definitions of variables
        elif ast[0] == "define":
            if is_symbol(ast[1]):
                if len(ast) == 3:
                    return env.set(ast[1], evaluate(ast[2], env))
                else:
                    raise LispError("Wrong number of arguments")
            else:
                raise LispError("non-symbol")

        # evaluating a list in which the first element is a closure
        elif is_closure(ast[0]):
            closure = ast[0]
            arguments = ast[1:]
            parameters = closure.params

            if len(arguments) != len(parameters):
                raise LispError('wrong number of arguments, expected 2 got 3')

            bindings = {}
            for x in range(len(ast[1:])):
                arg1 = evaluate(arguments[x], env)
                param1 = parameters[x]
                bindings.update({param1: arg1})
            return evaluate(closure.body, closure.env.extend(bindings))

        elif ast[0] == 'lambda':
            if not is_list(ast[1]):
                raise LispError('not a list')
            if len(ast) == 3:
                return Closure(env, ast[1], ast[2])
            else:
                raise LispError('number of arguments')

        elif is_symbol(ast[0]) or is_list(ast[0]):
            closure = evaluate(ast[0], env)
            return evaluate([closure] + ast[1:], env)

        else:
            raise LispError("not a function")