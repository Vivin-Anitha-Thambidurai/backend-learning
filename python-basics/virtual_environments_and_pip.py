"""
virtual_environments_and_pip.py

This file explains:
- What a virtual environment is
- How to create and activate it
- How to use pip
- What requirements.txt is

NOTE:
Most commands here are meant to be run in the terminal, not inside Python.
"""

# -----------------------------
# 1. WHAT IS A VIRTUAL ENVIRONMENT?
# -----------------------------
"""
A virtual environment (venv) is an isolated environment
where Python packages are installed separately for each project.

Why we need it:
- Avoid package version conflicts
- Keep projects independent
- Professional project structure
"""

# -----------------------------
# 2. CREATE A VIRTUAL ENVIRONMENT
# -----------------------------
"""
Run this in terminal (inside your project folder):

python -m venv venv

This creates a folder named 'venv'
"""

# -----------------------------
# 3. ACTIVATE THE VIRTUAL ENVIRONMENT
# -----------------------------
"""
On macOS / Linux:
source venv/bin/activate

On Windows:
venv\\Scripts\\activate

After activation, you will see (venv) in terminal
"""

# -----------------------------
# 4. CHECK PYTHON & PIP
# -----------------------------
"""
Check python version:
python --version

Check pip version:
pip --version
"""

# -----------------------------
# 5. INSTALL PACKAGES USING PIP
# -----------------------------
"""
Install a package:
pip install requests

Install multiple packages:
pip install numpy pandas
"""

# Example usage after installing requests
import requests

response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)

# -----------------------------
# 6. LIST INSTALLED PACKAGES
# -----------------------------
"""
pip list
"""

# -----------------------------
# 7. REQUIREMENTS.TXT
# -----------------------------
"""
Generate requirements.txt:
pip freeze > requirements.txt

Install from requirements.txt:
pip install -r requirements.txt
"""

# -----------------------------
# 8. DEACTIVATE VIRTUAL ENVIRONMENT
# -----------------------------
"""
To exit virtual environment:
deactivate
"""

print("Virtual environment concepts explained successfully!")
