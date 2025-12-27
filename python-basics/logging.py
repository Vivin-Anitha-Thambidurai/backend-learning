"""
logging.py

This file explains:
- Why logging is better than print()
- Logging levels
- Logging to console and file
"""

import logging

# -----------------------------
# 1. WHY LOGGING?
# -----------------------------
"""
print() is useful for learning, but in real projects we use logging because:
- We can control log levels
- Logs can be saved to files
- Easier debugging in production
"""

# -----------------------------
# 2. BASIC LOGGING CONFIGURATION
# -----------------------------
logging.basicConfig(
    level=logging.DEBUG,  # Minimum level to capture
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# 3. LOGGING LEVELS
# -----------------------------
logging.debug("This is a DEBUG message (used for detailed debugging)")
logging.info("This is an INFO message (general information)")
logging.warning("This is a WARNING message (something unexpected)")
logging.error("This is an ERROR message (serious problem)")
logging.critical("This is a CRITICAL message (program may crash)")

# -----------------------------
# 4. LOGGING INSIDE FUNCTIONS
# -----------------------------
def divide(a, b):
    logging.info("divide() function called")
    try:
        result = a / b
        logging.debug(f"Division result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted")
        return None

print("Result:", divide(10, 2))
print("Result:", divide(10, 0))

# -----------------------------
# 5. LOGGING TO A FILE
# -----------------------------
file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

file_logger.addHandler(file_handler)

file_logger.info("This log is written to app.log file")
file_logger.warning("File logging works correctly")

print("Logging concepts executed successfully!")
