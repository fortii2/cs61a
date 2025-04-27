def summation(n, term):
    """Sum the first N natural numbers, after call term() on these numbers
    
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(n):
    """return n * n * n
    >>> cube(5)
    125
    """
    return pow(n, 3)

def normal(n):
    """return n
    >>> normal(5)
    5
    """
    return n