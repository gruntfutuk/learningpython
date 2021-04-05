def sum_nums(*args):
    """return total of nums or list of totals of lists/tuples/nums"""
    results = []
    tots = -1
    for arg in args:
        if isinstance(arg, (list, tuple)):
            results.append(sum(arg))
        else:
            if tots < 0:
                tots = len(results)
                results.append(arg)
            else:
                results[tots] += arg

    return results


if __name__ == "__main__":

    tests = [
        ((1, 2, 3), [6]),
        ((1, 2, 3, [4, 5]), [6, 9]),
        (((1, 2, 3), (10, 20), [100, 200]), [6, 30, 300]),
        (([5], 1, 2, 3), [5, 6]),
        ((1, 2, 3, [4, 5], 8), [14, 9]),
        (((1000, 2000), 5, (10, 20), 6, [100, 200], 7), [3000, 18, 30, 300]),
    ]

    for test, expected in tests:
        try:
            assert (result := sum_nums(*test)) == expected
        except AssertionError:
            print(f"***> ERROR\n\t{test},"
                  f"\n\texpected: {expected},\n\t"
                  f"returned: {result}")
        else:
            print(f"Correct for {test},\n\treturned: {expected}.")