#!/usr/bin/env python3


class searchString(object):
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    def stringLen(self, theString):
        result = 0
        for i in theString:
            result = result + 1
        return result

    def doSearch(self):
        lenString = self.stringLen(self.string)
        lenPattern = self.stringLen(self.pattern)
        i = 0
        matchCount = 0
        while i < lenPattern:
            searchPattern = self.pattern[i:i + lenString]
            if self.stringLen(searchPattern) == lenString:
                if searchPattern == self.string and i < (lenPattern - lenString):
                    matchCount = matchCount + 1
            i = i + 1
        if matchCount == 1:
            if lenPattern <= lenString + 1:
                return 0
            else:
                return matchCount
        else:
            return matchCount


tests = [('abab', 1),
         ('abcdefxy', 0),
         ('abcdabcdab', 2),
         ('abbcdabbbcbb', 3),
         ('abbbcdabbcbb', 3),
         ('', 0), ('ab', 0), ('abc', 0),
         ('failedtest', 999)
         ]

for test, assertion in tests:
    i = test[:-2]
    pattern = test[-2:]
    print(f"\nChecking for {pattern} in {i}")
    check = searchString(i, pattern)
    result = check.doSearch()
    try:
        assert result == assertion
    except AssertionError:
        print("*** ERROR **>> testing {} against {} returned a count of {} instead of {}".format(
            i, pattern, result, assertion))
    else:
        print("{} was found {} times in {} excluding the end occurence".format(
            i, result, pattern))
