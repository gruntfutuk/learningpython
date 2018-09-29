def str_merge(left, right):
    'return merged string, without duplication in overlap'
    chars = 0  # number of overlapping characters
    for ind in range(1, min(len(right), len(left)) + 1):
        print(left[-ind:], right[:ind], left.endswith(right[:ind]))
        if left.endswith(right[:ind]):
            chars = ind
    return left + right[chars:]
