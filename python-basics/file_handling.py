"""
file_handling.py
----------------
Read/write files safely.
Also covers JSON + CSV which are common in backend work.
Run: python file_handling.py
"""

import json
import csv
from pathlib import Path


BASE_DIR = Path(__file__).parent
TXT_PATH = BASE_DIR / "sample.txt"
JSON_PATH = BASE_DIR / "sample.json"
CSV_PATH = BASE_DIR / "sample.csv"


def write_and_read_text():
    print("\n=== TEXT FILES ===")

    # Write text (overwrites)
    TXT_PATH.write_text("Hello Vivin!\nThis is line 2.\n", encoding="utf-8")
    print(f"Wrote: {TXT_PATH.name}")

    # Append text
    with TXT_PATH.open("a", encoding="utf-8") as f:
        f.write("Appended line 3.\n")

    # Read text
    content = TXT_PATH.read_text(encoding="utf-8")
    print("Content:\n", content)


def read_lines_safely():
    print("\n=== READ LINES SAFELY ===")
    with TXT_PATH.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            print(f"{i}: {line.rstrip()}")


def json_write_and_read():
    print("\n=== JSON ===")
    data = {
        "name": "Vivin",
        "role": "backend-learner",
        "skills": ["python", "sql", "apis"],
        "active": True,
    }

    # Write JSON
    with JSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote: {JSON_PATH.name}")

    # Read JSON
    with JSON_PATH.open("r", encoding="utf-8") as f:
        loaded = json.load(f)
    print("Loaded JSON:", loaded)
    print("Name:", loaded["name"])


def csv_write_and_read():
    print("\n=== CSV ===")

    rows = [
        {"id": 1, "task": "learn python", "done": "yes"},
        {"id": 2, "task": "build API", "done": "no"},
        {"id": 3, "task": "practice SQL", "done": "no"},
    ]
    fieldnames = ["id", "task", "done"]

    # Write CSV
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote: {CSV_PATH.name}")

    # Read CSV
    with CSV_PATH.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print("Row:", row)


def file_paths_demo():
    print("\n=== PATHS (Pathlib) ===")
    print("Current folder:", BASE_DIR)
    print("TXT exists?", TXT_PATH.exists())
    print("All .py files here:", [p.name for p in BASE_DIR.glob("*.py")])


def mini_exercises():
    print("\n=== MINI EXERCISES ===")

    # 1) Count words in sample.txt
    text = TXT_PATH.read_text(encoding="utf-8")
    word_count = len(text.split())
    print("Word count in sample.txt:", word_count)

    # 2) Update JSON: add a new key and rewrite
    with JSON_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    data["updated"] = True

    with JSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("Updated JSON with 'updated': True")

    # 3) Read CSV and collect tasks that are not done
    not_done = []
    with CSV_PATH.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["done"].lower() != "yes":
                not_done.append(row["task"])

    print("Not done tasks:", not_done)


def main():
    write_and_read_text()
    read_lines_safely()
    json_write_and_read()
    csv_write_and_read()
    file_paths_demo()
    mini_exercises()


if __name__ == "__main__":
    main()
