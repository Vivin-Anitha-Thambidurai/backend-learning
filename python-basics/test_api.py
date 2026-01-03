"""
test_api.py

Basic API tests using pytest and FastAPI TestClient.
"""

from fastapi.testclient import TestClient
from basic_fastapi_app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_create_item():
    response = client.post(
        "/items",
        json={
            "name": "Book",
            "price": 10.5,
            "in_stock": True
        }
    )
    assert response.status_code == 200
    assert response.json()["item"]["name"] == "Book"
