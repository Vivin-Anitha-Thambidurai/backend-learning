"""
decorators.py
--------------
This file explains:
1. What decorators are
2. Creating a simple decorator
3. Using decorators with functions
4. Decorators with arguments
"""

# 1️⃣ Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


# 2️⃣ Decorator with arguments
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper


@decorator_with_args
def add(a, b):
    return a + b


result = add(5, 3)
print("Result:", result)


# 3️⃣ Practical example – authentication decorator
def login_required(func):
    def wrapper(user_logged_in):
        if not user_logged_in:
            print("Access denied. Please log in.")
            return
        return func(user_logged_in)
    return wrapper


@login_required
def view_dashboard(user_logged_in):
    print("Welcome to your dashboard")


view_dashboard(False)
view_dashboard(True)


# Entry point
if __name__ == "__main__":
    print("Decorators example executed.")
