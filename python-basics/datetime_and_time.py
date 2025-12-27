"""
datetime_and_time.py

This file explains:
- Working with date and time in Python
- datetime, date, time, timedelta
- Formatting dates
"""

from datetime import datetime, date, time, timedelta

# -----------------------------
# 1. CURRENT DATE & TIME
# -----------------------------
now = datetime.now()
print("Current datetime:", now)

today = date.today()
print("Today's date:", today)

current_time = now.time()
print("Current time:", current_time)

# -----------------------------
# 2. CREATING CUSTOM DATE & TIME
# -----------------------------
custom_date = date(2025, 1, 1)
custom_time = time(10, 30, 0)
custom_datetime = datetime(2025, 1, 1, 10, 30, 0)

print("Custom date:", custom_date)
print("Custom time:", custom_time)
print("Custom datetime:", custom_datetime)

# -----------------------------
# 3. DATE FORMATTING (strftime)
# -----------------------------
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")
formatted_full = now.strftime("%d %B %Y, %I:%M %p")

print("Formatted date:", formatted_date)
print("Formatted time:", formatted_time)
print("Formatted full:", formatted_full)

# -----------------------------
# 4. STRING TO DATETIME (strptime)
# -----------------------------
date_string = "2025-12-27"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed datetime:", parsed_date)

# -----------------------------
# 5. TIME DIFFERENCE (timedelta)
# -----------------------------
future_date = now + timedelta(days=7)
past_date = now - timedelta(days=3)

print("7 days in future:", future_date)
print("3 days in past:", past_date)

# -----------------------------
# 6. PRACTICAL EXAMPLE
# -----------------------------
def days_until_event(event_date):
    """Returns number of days until a given event date"""
    difference = event_date - date.today()
    return difference.days

event = date(2025, 12, 31)
print("Days until event:", days_until_event(event))

print("Datetime and time concepts executed successfully!")
