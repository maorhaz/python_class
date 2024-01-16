from functools import reduce

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    return 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1))

# Test cases
print(calculate_factorial(5))  # Output: 120
print(calculate_factorial(0))  # Output: 1
print(calculate_factorial(10))  # Output: 3628800
print(calculate_factorial(-2))  # Output: "Factorial is not defined for negative numbers"
print("maor hazut ")