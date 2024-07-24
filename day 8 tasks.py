def print_greeting():
  """Prints 'Hello, World!' to the console."""
  print("Hello, World!")

print_greeting()  # Call the function

def max_value(text):
  """Returns the maximum alphabetical character from a string."""
  return max(text)

result = max_value("Hello World")
print("Max character:", result)

def convert_to_float(number):
  """Converts an integer to its floating-point representation."""
  return float(number)

float_value = convert_to_float(42)
print("Float:", float_value)

def add_numbers(num1, num2):
  """Adds two numbers and returns the sum."""
  return num1 + num2

summation = add_numbers(10, 20)
print("Sum:", summation)

def greet(language_code):
  """Prints a greeting based on the language code."""
  greetings = {
      'en': "Hello",
      'es': "Hola",
      'fr': "Bonjour"
  }
  print(greetings.get(language_code, "Invalid language code"))

greet('en')  # Hello
greet('es')  # Hola
greet('fr')  # Bonjour
greet('xx')  # Invalid language code

def compute_pay(hours, rate):
  """Calculates weekly pay with overtime."""
  pay = hours * rate
  if hours > 40:
    overtime = hours - 40
    pay += overtime * rate * 1.5
  return pay

weekly_pay = compute_pay(45, 10)
print("Weekly pay:", weekly_pay)

def is_integer(text):
  """Checks if a string can be converted to an integer."""
  try:
    int(text)
    return True
  except ValueError:
    return False

is_int = is_integer("123")
is_string = is_integer("hello")
print("123 is integer:", is_int)
print("hello is integer:", is_string)

def print_lyrics(lyrics):
  """Prints the lyrics of a song. (Replace with your actual lyrics)"""
  # Replace this with the actual lyrics you want to print
  print("Write your song lyrics here!")

print_lyrics("...")  # Replace "..." with lyrics

def multiply_numbers(num1, num2):
  """Multiplies two numbers and returns the product."""
  return num1 * num2

product = multiply_numbers(7, 8)
print("Product:", product)

def calculate_expression():
  """Evaluates and returns the result of the expression."""
  expression = 1 + 2 * float(3) / 4 - 5
  return expression

result = calculate_expression()
print("Expression result:", result)