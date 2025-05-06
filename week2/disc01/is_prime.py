def is_prime(n):
    """check input N is prime or not.

    >>> is_prime(3)
    True

    >>> is_prime(6)
    False

    >>> is_prime(13)
    True
    """
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True