def sum(n):
    if n == 0:
        return 0
        
    return n + sum(n-1)

print(sum(8))
# 8+7+6+5+4+3+2+1
