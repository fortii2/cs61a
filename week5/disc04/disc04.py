def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    def helper(x, y):
        result = 0
        if x == m and y == n:
            return 1
        elif x > m or y > n:
            return 0
        else:
            return helper(x + 1, y) + helper(x, y + 1)
    return helper(1, 1)




def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    if len(s) < 1:
        return 1
    return max(s[0] * max_product(s[2:]), max_product(s[1:]))




            
        