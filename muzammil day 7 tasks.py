# 1. Boolean Expressions (already provided)

# 2. One-Way Decision (already provided)

# 3. Indentation (assuming Python)
x = 5
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
    print('Done with 2')

# 4. Nested Decisions
number = int(input("Enter an integer: "))
if 10 <= number <= 20:
    print("Within range")
else:
    print("Out of range")

# 5. Two-Way Decision (already provided)

# 6. Multi-Way Decision
number = int(input("Enter an integer: "))
if number < 10:
    print("Small")
elif 10 <= number <= 20:
    print("Medium")
else:
    print("Large")

# 7. Try/Except Structure
try:
  rawstr = input("Enter a number: ")
  ival = int(rawstr)
  if ival > 0:
    print('Nice work')
  else:
    print('Not a number')
except ValueError:
  print("Invalid input. Please enter a number.")

# 8. Exercise with Computation
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
if hours > 40:
  pay = 40 * rate + (hours - 40) * 1.5 * rate
else:
  pay = hours * rate
print("Gross pay:", pay)

# 9. Logical Operators
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > 0 and num2 > 0:
  print("Both are positive")
elif num1 > 0 or num2 > 0:
  print("One is positive")
else:
  print("None are positive")

# 10. Comparison and Logical Operators
number = int(input("Enter a number: "))
if number > 0:
  if number % 2 == 0:
    print("Positive and even")
  else:
    print("Positive but odd")
else:
  print("Negative")