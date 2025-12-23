"""
exceptions.py
-------------
Learn how to handle errors safely using try / except / else / finally.
Run: python exceptions.py
"""


def basic_exception():
    print("\n=== BASIC EXCEPTION ===")
    try:
        x = int("abc")  # error
    except ValueError:
        print("ValueError: Cannot convert string to int")


def multiple_exceptions():
    print("\n=== MULTIPLE EXCEPTIONS ===")
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print("Result:", a / b)
    except ValueError:
        print("Please enter valid numbers")
    except ZeroDivisionError:
        print("Cannot divide by zero")


def exception_else_finally():
    print("\n=== ELSE & FINALLY ===")
    try:
        num = int(input("Enter positive number: "))
        if num < 0:
            raise ValueError("Number must be positive")
    except ValueError as e:
        print("Error:", e)
    else:
        print("Valid number:", num)
    finally:
        print("Execution finished")


def custom_exception():
    print("\n=== CUSTOM EXCEPTION ===")

    class AgeTooSmallError(Exception):
        pass

    def check_age(age):
        if age < 18:
            raise AgeTooSmallError("Age must be 18 or above")
        return "Access granted"

    try:
        print(check_age(16))
    except AgeTooSmallError as e:
        print("Custom Error:", e)


def file_exception():
    print("\n=== FILE EXCEPTION ===")
    try:
        file = open("missing_file.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File not found")
    finally:
        print("File handling done")


def mini_exercises():
    print("\n=== MINI EXERCISES ===")

    # 1) Safe integer input
    def safe_int():
        try:
            return int(input("Enter int: "))
        except ValueError:
            return 0

    print("safe_int result:", safe_int())

    # 2) Handle dictionary key safely
    data = {"name": "Vivin"}
    print("Age:", data.get("age", "Not available"))

    # 3) Catch all (not recommended but useful)
    try:
        x = 10 / 0
    except Exception as e:
        print("Caught error:", type(e).__name__)


def main():
    basic_exception()
    multiple_exceptions()
    exception_else_finally()
    custom_exception()
    file_exception()
    mini_exercises()


if __name__ == "__main__":
    main()
