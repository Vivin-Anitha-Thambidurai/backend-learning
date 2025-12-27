"""
regex.py

This file explains:
- What regular expressions are
- Common regex functions
- Practical examples
"""

import re

# -----------------------------
# 1. BASIC REGEX MATCHING
# -----------------------------
text = "My email is vivin123@gmail.com"

match = re.search(r"\w+@\w+\.\w+", text)
if match:
    print("Email found:", match.group())
else:
    print("No email found")

# -----------------------------
# 2. FIND ALL MATCHES
# -----------------------------
text_numbers = "Order numbers: 123, 456, 789"

numbers = re.findall(r"\d+", text_numbers)
print("Numbers found:", numbers)

# -----------------------------
# 3. MATCH VS SEARCH
# -----------------------------
text_word = "Python is powerful"

match_start = re.match(r"Python", text_word)
search_any = re.search(r"powerful", text_word)

print("Match at start:", bool(match_start))
print("Search anywhere:", bool(search_any))

# -----------------------------
# 4. REPLACE TEXT (sub)
# -----------------------------
text_dirty = "My phone number is 9876543210"

clean_text = re.sub(r"\d", "*", text_dirty)
print("Masked text:", clean_text)

# -----------------------------
# 5. VALIDATION EXAMPLES
# -----------------------------
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

print("Valid email:", is_valid_email("test@example.com"))
print("Valid email:", is_valid_email("invalid-email"))

# -----------------------------
# 6. COMMON REGEX PATTERNS
# -----------------------------
"""
\\d  -> digit
\\w  -> word character
\\s  -> whitespace
+    -> one or more
*    -> zero or more
^    -> start of string
$    -> end of string
"""

print("Regex concepts executed successfully!")
