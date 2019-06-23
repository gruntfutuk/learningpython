def Stuart_Moore_shorty(sliding, base):
    return [sum(x * y for x, y in zip(sliding[counter:], base)) for counter in range(0, len(sliding) - len(base) + 1)]


def test_funcs(*funcs):
    import traceback

    tests = [([-1, 2, -2, 3, 41, 38, 22, 10, -1, 3],
              [40, 30, 20, 10],
              [10, 490, 1210, 2330, 3320, 2370, 1190]),
             ([56, -34, 20, -8, 15, 57, 16, 13, 2, -5],
              [5, 10, 15, 20],
              [80, 210, 1385, 1285, 1145, 680, 140])
             ]

    for func in funcs:
        print(f'\n\nTesting function {func.__name__}:\n')
        for sliding, base, answers in tests:
            result = func(sliding, base)
            try:
                assert result == answers
            except AssertionError:
                print(f'FAILED with {result}')
                print(f' sliding: {sliding}')
                print(f' base: base: {base}')
                print(f' expected: {answers}')
            else:
                print(f'Passed: {result}')


''' testing functions '''
if __name__ == '__main__':
    func_list = [func for name, func in globals().items()
                 if callable(func) and name[0:2] not in ('__')
                 and name[0:4] not in ('exit', 'quit', 'get_', 'test')]
    test_funcs(*func_list)
