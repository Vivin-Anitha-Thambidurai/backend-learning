"""
env_and_config.py

This file demonstrates how to load environment variables
securely using python-dotenv.
"""

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# ------------------------
# Read environment variables
# ------------------------

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"


def print_config():
    print("Database URL:", DATABASE_URL)
    print("Debug mode:", DEBUG)
    print("Secret key loaded:", bool(SECRET_KEY))


if __name__ == "__main__":
    print_config()
