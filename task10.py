# Data Type Conversion Tasks

# 1. Convert String to Integer
# Task: Create a function that takes a string as input and attempts to convert it to an integer.
# If the conversion fails, it should return None.
def string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        return None

# 2. Convert Integer to String
# Task: Create a function that takes an integer as input and converts it to a string.
def integer_to_string(n):
    return str(n)

# 3. Convert Float to Integer
# Task: Create a function that takes a float as input and converts it to an integer by rounding down.
def float_to_integer(f):
    return int(f // 1)

# 4. Convert List of Strings to List of Integers
# Task: Create a function that takes a list of strings as input and converts it to a list of integers.
# If a string cannot be converted, that element should be skipped.
def list_of_strings_to_list_of_integers(lst):
    result = []
    for s in lst:
        try:
            result.append(int(s))
        except ValueError:
            continue
    return result

# Arithmetic Operation Tasks

# 5. Addition of Two Numbers
# Task: Create a function that takes two numbers as input and returns their sum.
def add_two_numbers(a, b):
    return a + b

# 6. Subtraction of Two Numbers
# Task: Create a function that takes two numbers as input and returns their difference.
def subtract_two_numbers(a, b):
    return a - b

# 7. Multiplication of Two Numbers
# Task: Create a function that takes two numbers as input and returns their product.
def multiply_two_numbers(a, b):
    return a * b

# 8. Division of Two Numbers
# Task: Create a function that takes two numbers as input and returns the result of their division.
# The function should handle the case where the divisor is zero.
def divide_two_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# String Operation Tasks

# 9. Concatenate Two Strings
# Task: Create a function that takes two strings as input and returns their concatenation.
def concatenate_two_strings(s1, s2):
    return s1 + s2

# 10. Reverse a String
# Task: Create a function that takes a string as input and returns the string reversed.
def reverse_string(s):
    return s[::-1]