"""
json_and_csv.py

This file explains:
- Working with JSON data
- Reading and writing JSON files
- Reading and writing CSV files
"""

import json
import csv

# -----------------------------
# 1. WORKING WITH JSON
# -----------------------------
python_data = {
    "name": "Vivin",
    "role": "Python Learner",
    "skills": ["Python", "Git", "Problem Solving"],
    "active": True
}

# Convert Python dict to JSON string
json_string = json.dumps(python_data, indent=4)
print("JSON String:\n", json_string)

# Write JSON to file
with open("data.json", "w") as json_file:
    json.dump(python_data, json_file, indent=4)

# Read JSON from file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("Loaded JSON data:", loaded_data)

# -----------------------------
# 2. WORKING WITH CSV
# -----------------------------
csv_data = [
    ["Name", "Age", "Country"],
    ["Vivin", 22, "India"],
    ["Alex", 25, "UK"],
    ["Sam", 23, "USA"]
]

# Write CSV file
with open("data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)

print("CSV file written successfully")

# Read CSV file
with open("data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print("CSV Row:", row)

# -----------------------------
# 3. PRACTICAL USE CASE
# -----------------------------
"""
JSON:
- APIs
- Config files
- Data exchange

CSV:
- Spreadsheets
- Reports
- Data analysis
"""

print("JSON and CSV concepts executed successfully!")
