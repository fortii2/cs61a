def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

def memo(func):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return memorized