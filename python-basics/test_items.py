"""
test_items.py

API tests for Item endpoints.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_item():
    response = client.post(
        "/api/items",
        json={
            "name": "Pen",
            "price": 2.5,
            "in_stock": True
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Pen"
    assert data["price"] == 2.5
    assert data["in_stock"] is True
    assert "id" in data


def test_get_items():
    response = client.get("/api/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item_by_id():
    # create item first
    create = client.post(
        "/api/items",
        json={
            "name": "Notebook",
            "price": 5.0,
            "in_stock": False
        }
    )
    item_id = create.json()["id"]

    # fetch item
    response = client.get(f"/api/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Notebook"


def test_get_item_not_found():
    response = client.get("/api/items/999999")
    assert response.status_code == 404
