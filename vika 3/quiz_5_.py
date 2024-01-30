
def bar(n, m):
    return n * bar(n, m-1)
print(bar(2, 3))