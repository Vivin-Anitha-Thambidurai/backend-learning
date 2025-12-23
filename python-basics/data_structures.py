"""
data_structures.py
------------------
Python core data structures:
- list, tuple, set, dict
Includes quick examples + small mini-exercises.
Run: python data_structures.py
"""

from collections import Counter


def lists_demo():
    print("\n=== LISTS ===")
    nums = [10, 20, 30]
    print("start:", nums)

    nums.append(40)           # add to end
    nums.insert(1, 15)        # insert at index
    nums.extend([50, 60])     # add multiple
    print("after add:", nums)

    removed = nums.pop()      # remove last
    nums.remove(20)           # remove first matching value
    print("removed last:", removed)
    print("after remove:", nums)

    print("slice [1:4]:", nums[1:4])
    print("reverse slice:", nums[::-1])

    # Comprehension
    squares = [n * n for n in nums if n % 2 == 0]
    print("even squares:", squares)

    # Sorting
    words = ["banana", "apple", "cherry"]
    print("words:", words)
    words.sort()
    print("sorted:", words)
    words.sort(key=len, reverse=True)
    print("sorted by len desc:", words)


def tuples_demo():
    print("\n=== TUPLES ===")
    point = (3, 7)
    x, y = point  # unpacking
    print("point:", point, "x:", x, "y:", y)

    # Tuples are immutable (cannot point[0] = 99)
    people = [("Vivin", 24), ("Alex", 30), ("Sam", 21)]
    # sort list of tuples by age
    people_sorted = sorted(people, key=lambda p: p[1])
    print("people:", people)
    print("sorted by age:", people_sorted)


def sets_demo():
    print("\n=== SETS ===")
    a = {1, 2, 3, 3, 2}
    b = {3, 4, 5}
    print("a (unique):", a)
    print("b:", b)

    print("union:", a | b)
    print("intersection:", a & b)
    print("difference a-b:", a - b)
    print("symmetric diff:", a ^ b)

    seen = set()
    items = [1, 2, 2, 3, 1, 4]
    uniques_in_order = []
    for it in items:
        if it not in seen:
            seen.add(it)
            uniques_in_order.append(it)
    print("unique in order:", uniques_in_order)


def dicts_demo():
    print("\n=== DICTS ===")
    user = {"name": "Vivin", "role": "student", "city": "Sheffield"}
    print("user:", user)

    print("name:", user["name"])
    print("get missing (safe):", user.get("age", "N/A"))

    user["city"] = "UK"                 # update
    user["skills"] = ["python", "sql"]   # add new key
    print("updated:", user)

    # iterate
    for k, v in user.items():
        print(f"{k} -> {v}")

    # build frequency map
    text = "backend backend api sql sql sql"
    freq = {}
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1
    print("freq map:", freq)

    # collections.Counter is even easier
    print("Counter:", Counter(text.split()))


def mini_exercises():
    print("\n=== MINI EXERCISES ===")

    # 1) List: keep only strings longer than 3 chars
    words = ["api", "rest", "backend", "sql", "fastapi", "git"]
    long_words = [w for w in words if len(w) > 3]
    print("long_words:", long_words)

    # 2) Dict: invert mapping (value -> list of keys)
    grades = {"Vivin": "A", "Alex": "B", "Sam": "A", "Nina": "C"}
    inverted = {}
    for name, grade in grades.items():
        inverted.setdefault(grade, []).append(name)
    print("inverted grades:", inverted)

    # 3) Set: find duplicates in a list
    nums = [1, 2, 2, 3, 4, 4, 4, 5]
    seen = set()
    duplicates = set()
    for n in nums:
        if n in seen:
            duplicates.add(n)
        else:
            seen.add(n)
    print("dupli
