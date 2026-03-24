from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_add_book_success():
    response = client.post("/books", json={"id": 1, "title": "Book1", "author": "Author"})
    assert response.status_code == 200
    assert response.json()["book"]["title"] == "Book1"


def test_add_book_duplicate():
    client.post("/books", json={"id": 2, "title": "B", "author": "A"})
    response = client.post("/books", json={"id": 2, "title": "B2", "author": "A2"})
    assert response.status_code == 400
    assert response.json()["detail"] == "ID already exists"


def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)