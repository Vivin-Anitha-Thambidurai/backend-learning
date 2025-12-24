"""
classes_and_objects.py
----------------------
This file explains:
1. What a class is
2. Creating objects
3. The __init__ constructor
4. Instance variables
5. Instance methods
"""

# 1️⃣ Defining a class
class Person:
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance method
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


# 2️⃣ Creating objects (instances of the class)
person1 = Person("Vivin", 22)
person2 = Person("Alex", 25)

person1.introduce()
person2.introduce()


# 3️⃣ Another example – Bank Account
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited £{amount}. Current balance: £{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew £{amount}. Current balance: £{self.balance}")

    def check_balance(self):
        print(f"Account balance: £{self.balance}")


# 4️⃣ Using the BankAccount class
account = BankAccount("Vivin", 100)

account.deposit(50)
account.withdraw(30)
account.check_balance()


# 5️⃣ Why __name__ == "__main__" matters in OOP files
if __name__ == "__main__":
    print("Classes and objects example executed directly.")
