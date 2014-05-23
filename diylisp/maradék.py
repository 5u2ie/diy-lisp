#nosetests tests/test_4_working_with_variables_and_environments.py --stop
#nosetests tests/test_5_adding_functions_to_the_mix.py --stop
#nosetests tests/test_6_working_with_lists.py --stop
#nosetests tests/test_7_using_the_language.py --stop


elif ast[0] == 'cons':
        def eval_cons(ast, env):
            assert_exp_length(ast, 3)
            args = [evaluate(x, env) for x in ast[1:]]
            return [args[0]] + args[1]

    elif ast[0] == 'head':
        def eval_head(ast, env):
            assert_exp_length(ast, 2)
            args = [evaluate(x, env) for x in ast[1:]]
            if len(args[0]) == 0:
                raise LispError('empty list')
            return args[0][0]

    elif ast[0] == 'tail':
        def eval_tail(ast, env):
            assert_exp_length(ast, 2)
            args = [evaluate(x, env) for x in ast[1:]]
            return args[0][1:]

    elif ast[0] == 'empty':
        def eval_empty(ast, env):
            assert_exp_length(ast, 2)
            args = [evaluate(x, env) for x in ast[1:]]
            return (len(args[0]) == 0)

    elif is_symbol(ast[0]) or is_list(ast[0]):
        closure = evaluate(ast[0], env)
        return evaluate([closure] + ast[1:], env)
    else:
        raise LispError('Argument is not a function!')__author__ = 'Zsuzsanna'
