# functions.py
# -------------
# This file demonstrates defining and using functions

def greet_user(name):
    """Function to greet a user"""
    return f"Hello, {name}! Welcome to Python."

def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

# Calling the functions
username = input("Enter your name: ")
print(greet_user(username))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add_numbers(num1, num2)

print("Sum:", result)
