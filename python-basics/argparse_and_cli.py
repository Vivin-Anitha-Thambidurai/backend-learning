"""
argparse_and_cli.py

This file explains:
- What command-line interfaces (CLI) are
- How to use argparse
- How to accept arguments from terminal
"""

import argparse

# -----------------------------
# 1. WHAT IS A CLI?
# -----------------------------
"""
CLI (Command Line Interface) allows users to interact with a program
by passing arguments from the terminal instead of hardcoding values.
"""

# -----------------------------
# 2. BASIC ARGPARSE SETUP
# -----------------------------
parser = argparse.ArgumentParser(
    description="A simple CLI calculator"
)

# -----------------------------
# 3. ADDING ARGUMENTS
# -----------------------------
parser.add_argument(
    "a",
    type=float,
    help="First number"
)

parser.add_argument(
    "b",
    type=float,
    help="Second number"
)

parser.add_argument(
    "--operation",
    choices=["add", "sub", "mul", "div"],
    default="add",
    help="Operation to perform"
)

# -----------------------------
# 4. PARSE ARGUMENTS
# -----------------------------
args = parser.parse_args()

# -----------------------------
# 5. PERFORM OPERATION
# -----------------------------
def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            return "Error: Division by zero"
        return a / b

result = calculate(args.a, args.b, args.operation)

print("Result:", result)

# -----------------------------
# 6. HOW TO RUN THIS FILE
# -----------------------------
"""
Run from terminal:

python argparse_and_cli.py 10 5
python argparse_and_cli.py 10 5 --operation sub
python argparse_and_cli.py 10 5 --operation mul
python argparse_and_cli.py 10 5 --operation div
"""

print("CLI execution completed successfully!")
