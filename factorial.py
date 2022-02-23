

def factorial(n) -> int:
    """
    accepts number to find factorial of
    return factorial of number
    """
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n


factorial_number = int(input("Number to find factorial of: "))
print(factorial(factorial_number))