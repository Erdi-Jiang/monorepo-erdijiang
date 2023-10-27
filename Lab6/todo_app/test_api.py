# test_api.py

from fastapi.testclient import TestClient
from Lab6.myenv.my_fastapi import app

client = TestClient(app)


def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {"message": "GET request to /items/"}


def test_get_item():
    response = client.get("/items/123")  # Replace with a valid item ID
    assert response.status_code == 200
    assert response.json() == {"message": "GET request to /items/123"}


def test_get_items_with_query_params():
    response = client.get("/items/query/?skip=2&limit=10")
    assert response.status_code == 200
    assert response.json() == {"message": "GET request to /items/query/?skip=2&limit=10"}


def test_get_item_with_query_params():
    response = client.get("/items/123/details?skip=2&limit=10")  # Replace with a valid item ID
    assert response.status_code == 200
    assert response.json() == {"message": "GET request to /items/123/details?skip=2&limit=10"}


def test_create_item():
    data = {"name": "New Item", "description": "A new item"}
    response = client.post("/items/", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "POST request to /items/", "item": data}
