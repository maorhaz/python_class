
def generate_squared_dictionary(n):
    squared_dict = {num: (lambda x: x**2)(num) for num in range(1, n+1)}
    return squared_dict

# Test case
result_dict = generate_squared_dictionary(7)
print(result_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25