"""
typing_and_type_hints.py

This file demonstrates Python type hints
to improve readability and catch bugs early.
"""

from typing import List, Dict, Tuple, Optional, Union


# ------------------------
# Basic type hints
# ------------------------

name: str = "Vivin"
age: int = 22
height: float = 5.8
is_student: bool = True


# ------------------------
# Function type hints
# ------------------------

def greet(user: str) -> str:
    return f"Hello, {user}!"


def add(a: int, b: int) -> int:
    return a + b


# ------------------------
# Collections
# ------------------------

numbers: List[int] = [1, 2, 3, 4]
scores: Dict[str, int] = {"math": 90, "science": 85}
point: Tuple[int, int] = (10, 20)


# ------------------------
# Optional & Union
# ------------------------

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Admin"
    return None


def process_value(value: Union[int, str]) -> str:
    return str(value)


# ------------------------
# Real-world example
# ------------------------

def calculate_average(marks: List[int]) -> float:
    return sum(marks) / len(marks)


# ------------------------
# Entry point
# ------------------------

if __name__ == "__main__":
    print(greet(name))
    print("Sum:", add(3, 4))
    print("User:", find_user(2))
    print("Processed:", process_value(100))
    print("Average:", calculate_average([80, 90, 85]))
