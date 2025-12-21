"""
variables_and_types.py
----------------------
This file introduces basic Python variables and built-in data types.
Run this file using: python variables_and_types.py
"""

# 1. Integer
age = 22
print("Age:", age, "| Type:", type(age))

# 2. Float
height = 5.9
print("Height:", height, "| Type:", type(height))

# 3. String
name = "Vivin"
print("Name:", name, "| Type:", type(name))

# 4. Boolean
is_student = True
print("Is student:", is_student, "| Type:", type(is_student))

# 5. Multiple assignment
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# 6. Type casting
age_str = str(age)
height_int = int(height)

print("Age as string:", age_str, "| Type:", type(age_str))
print("Height as int:", height_int, "| Type:", type(height_int))

print("\n✅ Variables and data types demo completed successfully!")
