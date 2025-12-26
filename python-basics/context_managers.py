"""
context_managers.py
--------------------
This file explains:
1. What context managers are
2. Using built-in context managers
3. Creating context managers using a class
4. Creating context managers using contextlib
"""

# 1️⃣ Built-in context manager
with open("sample.txt", "w") as file:
    file.write("Hello, this file is managed by a context manager")


with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


# 2️⃣ Custom context manager using a class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file")
        self.file.close()
        return False  # Propagate exceptions if any


with FileManager("custom.txt", "w") as f:
    f.write("Managed using custom context manager")


# 3️⃣ Context manager using contextlib
from contextlib import contextmanager


@contextmanager
def managed_resource(name):
    print(f"Acquiring resource: {name}")
    try:
        yield name
    finally:
        print(f"Releasing resource: {name}")


with managed_resource("DatabaseConnection"):
    print("Using the resource")


# Entry point
if __name__ == "__main__":
    print("Context managers example executed.")
