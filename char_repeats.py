def Mark_Geyzer_count2(target):
    count = 0
    tail = target[-2:]
    while target != tail:
        count += target[:2] == tail
        target = target[1:]
    return count


def test_funcs(*funcs):
    ''' test of supplied function to count occurences of last 2 char substring in source'''
    tests = [('abab', 1),
             ('abcdefxy', 0),
             ('abcdabcdab', 2),
             ('abbcdabbbcbb', 3),
             ('abbbcdabbcbb', 3),
             ("xxx", 1),
             ('', 0), ('ab', 0), ('abc', 0),
             ('failedtest - this test is designed to fail', 999)
             ]

    for func in funcs:
        print(f'\nTesting function {func.__name__}\n')
        for test, assertion in tests:
            count = func(test)
            try:
                assert count == assertion
            except AssertionError:
                print(
                    f'*** ERROR **>> test data {test} returned a count of {count} instead of {assertion}')
            else:
                print(
                    f'passed: {test[-2:]} found in {test} {count} times.')


''' testing functions '''
if __name__ == '__main__':
    func_list = [func for name, func in globals().items()
                 if callable(func) and name[0:2] not in ('__')
                 and name[0:4] not in ('exit', 'quit', 'get_', 'test')]
    test_funcs(*func_list)
