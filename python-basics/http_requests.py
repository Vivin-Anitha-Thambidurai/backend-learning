"""
http_requests.py

This file demonstrates how to make HTTP requests in Python
using the requests library.
"""

import requests


# ------------------------
# Simple GET request
# ------------------------

def get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())


# ------------------------
# GET with query parameters
# ------------------------

def get_posts_by_user(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    response = requests.get(url, params=params)
    print(f"Posts by user {user_id}:")
    print(response.json())


# ------------------------
# POST request
# ------------------------

def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Hello Backend",
        "body": "Learning Python HTTP requests",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    print("Status Code:", response.status_code)
    print("Created Post:", response.json())


# ------------------------
# Error handling
# ------------------------

def handle_error():
    url = "https://jsonplaceholder.typicode.com/invalid"

    response = requests.get(url)
    if response.status_code != 200:
        print("Request failed:", response.status_code)


# ------------------------
# Entry point
# ------------------------

if __name__ == "__main__":
    get_post()
    print("\n-------------------\n")
    get_posts_by_user(1)
    print("\n-------------------\n")
    create_post()
    print("\n-------------------\n")
    handle_error()
