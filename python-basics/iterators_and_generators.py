"""
iterators_and_generators.py
----------------------------
This file explains:
1. Iterators
2. The iter() and next() functions
3. Creating custom iterators
4. Generators using yield
"""

# 1️⃣ Iterator example
numbers = [1, 2, 3, 4]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# 2️⃣ Custom iterator
class CountUpTo:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


counter = CountUpTo(3)

for num in counter:
    print("Count:", num)


# 3️⃣ Generator function
def count_down(start):
    while start > 0:
        yield start
        start -= 1


for number in count_down(5):
    print("Countdown:", number)


# 4️⃣ Generator expression
squares = (x * x for x in range(5))

for sq in squares:
    print("Square:", sq)


# Entry point
if __name__ == "__main__":
    print("Iterators and generators example executed.")
