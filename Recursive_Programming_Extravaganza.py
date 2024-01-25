def multiply(a, b):    
    
    if a == 0 or b == 0:
        return 0
    
    elif a == 1:
        return b
    
    elif b == 1:
        return a
    
    negative_result = False

    if a < 0:
        a = -a
        negative_result = not negative_result

    if b < 0:
        b = -b
        negative_result = not negative_result

    lower = min(a, b)
    higher = max(a, b)

    result = 0
    for _ in range(lower):
        result += higher

    return -result if negative_result else result

# print(multiply(3,6))

def multiply(a, b):    
    
    if a == 0 or b == 0:
        return 0
    elif b > 0:
        return a + multiply(a, b-1)
    elif b < 0:
        return -a + multiply(a, b+1)

# print(multiply(3,6))

def sum_of_digits(n):
    if n == 0:
        return 0 # return 0 if the number is 0
    return (n % 10) + sum_of_digits(n//10)

# print(sum_of_digits(254))

def factorial(n):
    if n == 0:
        return 1 
    return n*(factorial(n-1))

# print(factorial(5))

def power(base, exp):
    if exp == 0:
        return 1
    return base*(power(base, exp-1))

# print(power(2,3))

def fibonacci(n): # this function takes more time
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 
    
# print(fibonacci(8)) 

def fibonacci_2(n): # this functiion takes less time
    def fibonacci_helper(a, b, count):
        if count == 0:
            return a
        else:
            return fibonacci_helper(b, a + b, count - 1)

    if n < 0:
        return "Invalid input, please provide a non-negative integer."
    else:
        return fibonacci_helper(0, 1, n)

# print(fibonacci_2(34))





    
