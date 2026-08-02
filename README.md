# 💰 Smart Expense Tracker API

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green.svg)](https://fastapi.tiangolo.com/)
![Tests](https://github.com/YashThakur0421/smart-expense-tracker/actions/workflows/test.yml/badge.svg)

A RESTful API built using **FastAPI** for managing personal expenses. The application allows users to create, retrieve, filter, summarize, and delete expenses while maintaining data persistence in a local JSON file.

This project was developed as part of the **Software Engineering Apprenticeship Assignment**.

---

## 🚀 Quick Verification

Clone and run the project:

```bash
git clone https://github.com/YashThakur0421/smart-expense-tracker.git

cd smart-expense-tracker

pip install -r requirements.txt

python -m pytest -v

uvicorn src.main:app --reload
```

Expected test result:

```text
================== 6 passed ==================
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## ✨ Features

### Expense Management

- Add an expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate category-wise expenses
- Delete an expense

### Engineering Features

- FastAPI REST architecture
- Pydantic validation
- JSON-based persistence
- Automated testing with Pytest
- GitHub Actions CI workflow
- Interactive Swagger documentation

---

## 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python 3.11 | Programming Language |
| FastAPI | REST API Framework |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |
| Pytest | Testing Framework |
| GitHub Actions | Continuous Integration |
| JSON | Data Storage |

---

## 📂 Project Structure

```text
smart-expense-tracker/

├── .github/
│   └── workflows/
│       └── test.yml

├── README.md
├── AI_NOTES.md
├── requirements.txt

├── src/
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│   └── expenses.json

└── tests/
    └── test_api.py
```

---

## 📚 API Documentation

After starting the server:

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /expenses | Add new expense |
| GET | /expenses | Get all expenses |
| GET | /expenses/category/{category} | Filter by category |
| GET | /expenses/total | Get total expenses |
| GET | /expenses/total/{category} | Get category total |
| DELETE | /expenses/{id} | Delete expense |

---

## 🧪 Running Tests

```bash
python -m pytest -v
```

Current coverage includes:

- Add Expense
- Retrieve Expenses
- Filter By Category
- Total Expense Calculation
- Category-wise Total Calculation
- Delete Expense

---

## 🔒 Validation

The API validates:

- Positive expense amounts
- Required fields
- Duplicate expense IDs
- Invalid requests
- Missing expense records

---

## 🤖 AI Usage

Details regarding AI-assisted development, validation, and manual modifications are documented in:

```text
AI_NOTES.md
```

---

## 🔮 Future Improvements

- PostgreSQL integration
- JWT Authentication
- Docker support
- Monthly expense summaries
- User accounts
- Cloud deployment

---

## 👨‍💻 Author

Yash Thakur

GitHub:
https://github.com/YashThakur0421