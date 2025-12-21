"""
input_output.py
---------------
This file demonstrates user input and output in Python.
Run this file using: python input_output.py
"""

# 1. Simple output
print("Welcome to Python Input & Output demo")

# 2. Taking input from user
name = input("Enter your name: ")
age = input("Enter your age: ")

# 3. Input is always a string by default
print("\nRaw input types:")
print("Name type:", type(name))
print("Age type:", type(age))

# 4. Type casting input
age = int(age)

print("\nAfter type casting:")
print("Age:", age)
print("Age type:", type(age))

# 5. Formatted output (important for backend logs & APIs)
print(f"\nHello {name}, you are {age} years old.")

# 6. Multiple inputs in one line
x, y = input("\nEnter two numbers separated by space: ").split()
x = int(x)
y = int(y)

print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)

print("\n✅ Input and output demo completed successfully!")
