"""
encapsulation_and_abstraction.py
--------------------------------
This file explains:
1. Encapsulation (private variables & methods)
2. Getter and Setter methods
3. Abstraction using abstract base classes
"""

# 1️⃣ Encapsulation
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private variable

    def login(self, password):
        if self.__password == password:
            print("Login successful")
        else:
            print("Invalid password")

    # Getter
    def get_password(self):
        return "Access denied"


user = User("vivin", "secret123")
user.login("secret123")
user.login("wrongpass")

# Trying to access private variable directly (not recommended)
# print(user.__password)  # ❌ will cause error


# 2️⃣ Getter and Setter example
class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount()
account.deposit(100)
account.withdraw(40)
print("Balance:", account.get_balance())


# 3️⃣ Abstraction
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rect = Rectangle(5, 4)
circle = Circle(3)

print("Rectangle area:", rect.area())
print("Circle area:", circle.area())


# Entry point
if __name__ == "__main__":
    print("Encapsulation and abstraction example executed.")
