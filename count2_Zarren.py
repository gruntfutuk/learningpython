''' beginners exercise to count and return occurrences of last 2 char
    substring in preceding part of a string argument '''


def Zarren_Donovan_Spry_count2(pattern):
    #lenString = stringLen(string)

    def stringLen(theString):
        result = 0
        for i in theString:
            result = result + 1
        return result

    lenString = 2
    lenPattern = stringLen(pattern)
    i = 0
    matchCount = 0
    string = pattern[-lenString:]
    while i < lenPattern:
        searchPattern = pattern[i:i + lenString]
        if stringLen(searchPattern) == lenString:
            if searchPattern == string and i < (lenPattern - lenString):
                matchCount = matchCount + 1
        i = i + 1
    if matchCount == 1:
        if lenPattern <= lenString + 1:
            return 0
        else:
            return matchCount
    else:
        return matchCount


''' test harness for all of above solutions '''


def test_a_count_f(*funcs):
    ''' test of supplied function to count occurences of last 2 char substring in source'''
    tests = [('abab', 1),
             ('abcdefxy', 0),
             ('abcdabcdab', 2),
             ('abbcdabbbcbb', 3),
             ('abbbcdabbcbb', 3),
             ('', 0), ('ab', 0), ('abc', 0),
             ('failedtest', 999)
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
                    f'{test[-2:]} found in {test} {count} times.')


if __name__ == "__main__":
    print('''

Testing all solutions of beginner's exercise:
Count and return occurrences of last 2 char
substring in preceding part of a string argument.

The LAST occurrence (i.e. the search sub-string) is
not included in the counts.
''')
    test_a_count_f(Zarren_Donovan_Spry_count2)
