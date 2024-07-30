# String to Integer with Fallback
def string_to_int_with_fallback(s, default):
    try:
        return int(s)
    except ValueError:
        return default

# Example usage
print(string_to_int_with_fallback("123", 0))  # 123
print(string_to_int_with_fallback("abc", 0))  # 0

# Integer to String with Formatting
def int_to_string_with_format(n, format_spec):
    return format(n, format_spec)

# Example usage
print(int_to_string_with_format(1234, "04d"))  # '1234'
print(int_to_string_with_format(1234, "e"))    # '1.234000e+03'

# Float to Integer with Multiple Rounding Options
import math

def float_to_int_with_rounding(f, strategy):
    if strategy == "up":
        return math.ceil(f)
    elif strategy == "down":
        return math.floor(f)
    elif strategy == "nearest":
        return round(f)
    else:
        raise ValueError("Invalid rounding strategy")

# Example usage
print(float_to_int_with_rounding(3.6, "up"))      # 4
print(float_to_int_with_rounding(3.6, "down"))    # 3
print(float_to_int_with_rounding(3.6, "nearest")) # 4

# List of Strings to List of Integers with Error Logging
def list_of_strings_to_ints_with_logging(strings):
    ints = []
    errors = []
    for s in strings:
        try:
            ints.append(int(s))
        except ValueError:
            errors.append(s)
    return ints, errors

# Example usage
print(list_of_strings_to_ints_with_logging(["1", "2", "abc", "4"]))  
# ([1, 2, 4], ['abc'])

# Addition with Type Enforcement
class NotANumberError(Exception):
    pass

def add_with_type_enforcement(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise NotANumberError("Both inputs must be numbers")
    return a + b

# Example usage
print(add_with_type_enforcement(1, 2))  # 3
# print(add_with_type_enforcement(1, "2"))  # NotANumberError: Both inputs must be numbers

# Cumulative Subtraction with List Validation
class InvalidListError(Exception):
    pass

def cumulative_subtraction(numbers):
    if len(numbers) < 2 or not all(isinstance(n, (int, float)) for n in numbers):
        raise InvalidListError("List must contain at least two numeric values")
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

# Example usage
print(cumulative_subtraction([10, 3, 2]))  # 5
# print(cumulative_subtraction([10]))  # InvalidListError: List must contain at least two numeric values

# Exponentiation Table
def exponentiation_table(base, exponent_range):
    return [f"{base}^{i} = {base**i}" for i in range(1, exponent_range + 1)]

# Example usage
print(exponentiation_table(2, 5))  
# ['2^1 = 2', '2^2 = 4', '2^3 = 8', '2^4 = 16', '2^5 = 32']

# Safe Division with Custom Error Handling
class DivisionByZeroError(Exception):
    pass

def safe_division(a, b, precision):
    if b == 0:
        raise DivisionByZeroError("Division by zero is not allowed")
    return round(a / b, precision)

# Example usage
print(safe_division(10, 2, 2))  # 5.0
# print(safe_division(10, 0, 2))  # DivisionByZeroError: Division by zero is not allowed

# Advanced String Split and Conditional Join
def advanced_split_and_join(s, delimiter1, delimiter2):
    parts = s.split(delimiter1)
    return delimiter2.join([part for part in parts if len(part) > 3])

# Example usage
print(advanced_split_and_join("this,is,a,test,string", ",", "-"))  # 'this-test-string'

# Enhanced Palindrome Check with Character Frequency Analysis
import re
from collections import Counter

def palindrome_check_with_frequency(s):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    is_palindrome = cleaned == cleaned[::-1]
    char_frequency = Counter(cleaned)
    return is_palindrome, dict(char_frequency)

# Example usage
print(palindrome_check_with_frequency("A man, a plan, a canal, Panama"))
# (True, {'a': 8, 'm': 2, 'n': 4, 'p': 1, 'l': 2, 'c': 1})