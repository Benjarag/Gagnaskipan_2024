def foo_recur(n):
    if n < 0:
        return
    foo_recur(n - 1)
    print(n)

foo_recur(3)