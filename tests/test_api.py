from fastapi.testclient import TestClient
from src.main import app
from src.storage import save_expenses

client = TestClient(app)


def setup_function():
    save_expenses([])


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    assert response.status_code == 200
    assert response.json()["expense"]["title"] == "Lunch"


def test_get_all_expenses():
    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_by_category():
    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    response = client.get("/expenses/category/Food")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_total_expenses():
    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    client.post(
        "/expenses",
        json={
            "id": 2,
            "title": "Uber",
            "amount": 100,
            "category": "Travel",
            "date": "2026-08-02"
        }
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total_expenses"] == 350


def test_total_by_category():
    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    response = client.get("/expenses/total/Food")

    assert response.status_code == 200
    assert response.json()["total_expenses"] == 250


def test_delete_expense():
    client.post(
        "/expenses",
        json={
            "id": 1,
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    response = client.delete("/expenses/1")

    assert response.status_code == 200

    expenses = client.get("/expenses")

    assert len(expenses.json()) == 0