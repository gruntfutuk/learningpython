''' beginners exercise to count and return occurrences of last 2 char
    substring in preceding part of a string argument '''


def Stuart_Moore_count2(source):
    count = 0
    if source[3:]:
        search = source[-2:]
        prev = source[0]
        for ch in source[1:-2]:
            if prev + ch == search:
                count += 1
            prev = ch
    return count


def Mark_Geyzer_count2(target):
    count = 0
    tail = target[-2:]
    while target != tail:
        count += target[:2] == tail
        target = target[1:]
    return count


def Srinivasa_Reddy_Varimadugu_count2(target):
    count = 0
    flag = False
    osubstr = target[-2::]
    tail = target[-2::-1]
    otail = tail[::-1]
    for i in otail:
        if i == osubstr[1] and flag:
            count += 1
            flag = False
        flag = osubstr[0] == i
    return count


def Kevin_Stout_count2(xs):

    def bigrams(xs):
        a, b = None, None

        for x in xs:
            a, b = b, x
            if a:
                yield a, b

    freq = {}
    xy = None

    for xy in bigrams(xs):
        freq[xy] = freq.get(xy, 0) + 1

    return freq.get(xy, 1) - 1


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


def Pierre_Chiggles_count2(Haystack):
    count = 0
    while True:
        try:
            needle = Haystack[-2] + Haystack[-1]
            pos = -3
            while True:
                try:
                    needleTest = Haystack[pos] + Haystack[pos + 1]
                    if needle == needleTest:
                        count += 1
                    pos -= 1
                except:
                    return count
        except:
            return count


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
    test_a_count_f(Stuart_Moore_count2, Mark_Geyzer_count2,
                   Srinivasa_Reddy_Varimadugu_count2, Kevin_Stout_count2, Zarren_Donovan_Spry_count2, Pierre_Chiggles_count2)
