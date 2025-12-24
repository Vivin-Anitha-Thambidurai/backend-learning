"""
modules_and_packages.py
-----------------------
This file explains:
1. What modules are
2. How to import built-in modules
3. How to import specific functions
4. How to create and use your own modules
5. The purpose of __name__ == "__main__"
"""

# 1️⃣ Importing a built-in module
import math

print("Square root of 16:", math.sqrt(16))
print("Value of PI:", math.pi)


# 2️⃣ Importing specific functions from a module
from math import pow, factorial

print("2 power 3:", pow(2, 3))
print("Factorial of 5:", factorial(5))


# 3️⃣ Importing with alias
import random as rnd

print("Random number between 1 and 10:", rnd.randint(1, 10))


# 4️⃣ Creating and using your own module
# Assume we have a file named functions.py in the same folder
# and it contains a function called greet(name)

import functions

functions.greet("Vivin")


# 5️⃣ __name__ == "__main__"
def main():
    print("This code runs only when this file is executed directly.")


if __name__ == "__main__":
    main()
