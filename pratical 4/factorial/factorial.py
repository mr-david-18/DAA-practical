# Time Complexity: O(n)
# Space Complexity: O(n)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = 5
print("Input number:", n)
result = factorial(n)
print(f"Factorial of {n} is:", result)
