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


print(sum_nums(1, 2, 3))
print(sum_nums(1, 2, 3, [4, 5]))
print(sum_nums((1, 2, 3), (10, 20), [100, 200]))
print(sum_nums([5], 1, 2, 3))
print(sum_nums(1, 2, 3, [4, 5], 8))
print(sum_nums((1000, 2000), 5, (10, 20), 6, [100, 200], 7))