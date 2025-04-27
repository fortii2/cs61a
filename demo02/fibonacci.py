def fib(n):
    k = 0
    pre, cur = 1, 0

    while k < n:
        print(cur)
        pre, cur = cur, pre + cur
        k += 1 