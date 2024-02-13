# Divide and Conquer ==>
# https://www.geeksforgeeks.org/divide-and-conquer/


# Dynamic programming
# https://en.wikipedia.org/wiki/Dynamic_programming


# Recursive Function
def recursive_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


# Example:  5! = 5*4*3*2*1
# 5 * recursive (4) = 5* 4 * recursive(3) = 5*4*3* recursive(2) = 5*4*3*2*recursive(1)

print(recursive_factorial(5))
