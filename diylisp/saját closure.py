__author__ = 'Zsuzsanna'
elif ast[0] == 'closure':
        closure = ast[0]
        if len(ast[1:]) != len(closure.params):
            raise LispError('Wrong number of arguments')

        bindings = {}
        for x in ast[1:]:
            arg1 = evaluate(x, env)
            param1 = closure.params[x]
            bindings.update({param1: arg1})
        return evaluate(closure.body, closure.env.extend(bindings))