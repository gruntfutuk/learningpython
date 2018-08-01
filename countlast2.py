''' beginners exercise to count occurrences of last 2 char
    substring in preceding part of a string '''

# solution from Stuart Moore


def stuart_count2(source):
    ''' return count occurrences of last 2 char
    substring in preceding part of source string '''
    count = 0
    if source[3:]:
        search = source[-2:]
        prev = source[0]
        for ch in source[1:-2]:
            if prev + ch == search:
                count += 1
            prev = ch
    return count

# Solution from Mark Geyzer


def mark_count2(target):
    count = 0
    tail = target[-2:]
    while target != tail:
        count += target[:2] == tail
        target = target[1:]
    return count

# Test function for any solution


def test_a_count_f(*funcs):
    ''' test of supplied function to count occurences of last 2 char substring in source'''
    tests = [('abab', 1),
             ('abcdabcdab', 2),
             ('abbcdabbcbb', 3),
             ('abbbcdabbcbb', 3),
             ('', 0), ('ab', 0), ('abc', 0),
             ('failedtest', 999)
             ]

    for func in funcs:
        print(f'\n\nTesting function {func.__name__}\n')
        for test, assertion in tests:
            count = func(test)
            try:
                assert count == assertion
            except AssertionError:
                print(
                    f'test data {test} returned a count of {count} instead of {assertion}')
            else:
                print(
                    f'{test[-2:]} found in {test} {count} times excluding end occurence.')


if __name__ == "__main__":
    test_a_count_f(stuart_count2, mark_count2)
