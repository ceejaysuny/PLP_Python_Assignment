"""
Coding Question

Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False
"""


def large_power(base, exponent):
    # Calculate the result of base to the power of exponent
    result = base ** exponent
    
    # Use an if statement to test if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Example usage:
print(large_power(10, 3))  # Output: False
print(large_power(10, 4))  # Output: True



"""
Coding question

Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, and False otherwise. 
Consider using modulo operator % to check for divisibility.
"""

def divisible_by_ten(num):
    # Calculate the remainder of the input divided by 10
    remainder = num % 10
    
    # Use an if statement to check if the remainder was 0
    if remainder == 0:
        return True
    else:
        return False

# Example usage:
print(divisible_by_ten(20))  # Output: True
print(divisible_by_ten(33))  # Output: False

