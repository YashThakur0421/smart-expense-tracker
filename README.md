# 💰 Smart Expense Tracker API

A production-ready RESTful API built with **FastAPI** for managing personal expenses. The application provides complete expense management functionality including creating, retrieving, filtering, calculating summaries, and deleting expenses.

The project follows clean backend development practices with:

* REST API architecture
* Request validation
* Modular code structure
* Automated testing
* API documentation
* File-based persistence

---

# 🚀 Features

## Expense Management

✅ Create new expenses
✅ Retrieve all expenses
✅ Filter expenses by category
✅ Calculate total spending
✅ Calculate category-wise spending
✅ Delete expenses

## Developer Features

✅ FastAPI automatic Swagger documentation
✅ Pydantic data validation
✅ JSON-based persistence layer
✅ Modular backend architecture
✅ Automated API testing with Pytest
✅ Clean project structure

---

# 🏗️ Architecture Overview

The application follows a simple layered architecture:

```text
                 Client
                   |
                   |
             HTTP Request
                   |
                   |
              FastAPI App
                   |
        -----------------------
        |                     |
   Validation Layer     API Controllers
        |                     |
        -----------------------
                   |
            Storage Layer
                   |
             expenses.json
```

---

# 🛠️ Technology Stack

| Technology  | Purpose                               |
| ----------- | ------------------------------------- |
| Python 3.11 | Core programming language             |
| FastAPI     | REST API framework                    |
| Pydantic    | Request validation and data modelling |
| Uvicorn     | Application server                    |
| Pytest      | Automated testing                     |
| JSON        | Lightweight data persistence          |

---

# 📁 Project Structure

```text
smart-expense-tracker/

│
├── README.md
├── AI_NOTES.md
├── requirements.txt
│
├── src/
│   │
│   ├── main.py
│   │   └── FastAPI application and API routes
│   │
│   ├── models.py
│   │   └── Request/response data models
│   │
│   ├── storage.py
│   │   └── JSON file storage operations
│   │
│   └── expenses.json
│       └── Expense data storage
│
└── tests/
    │
    └── test_api.py
        └── API test cases
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd smart-expense-tracker
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

Application will run at:

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

You can test all endpoints directly from the browser.

---

# 🔌 API Endpoints

## 1. Health Check

### GET

```
/
```

Response:

```json
{
  "message": "Smart Expense Tracker API"
}
```

---

# Expense APIs

## Create Expense

### POST

```
/expenses
```

Example Request:

```json
{
  "id": 1,
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "date": "2026-08-01"
}
```

Response:

```json
{
  "message": "Expense added successfully"
}
```

---

## Get All Expenses

### GET

```
/expenses
```

Example Response:

```json
[
  {
    "id":1,
    "title":"Lunch",
    "amount":250,
    "category":"Food",
    "date":"2026-08-01"
  }
]
```

---

## Filter Expenses By Category

### GET

```
/expenses/category/{category}
```

Example:

```
/expenses/category/Food
```

---

## Get Total Expenses

### GET

```
/expenses/total
```

Response:

```json
{
 "total_expenses":2500
}
```

---

## Get Category Wise Total

### GET

```
/expenses/total/{category}
```

Example:

```
/expenses/total/Food
```

Response:

```json
{
 "category":"Food",
 "total_expenses":750
}
```

---

## Delete Expense

### DELETE

```
/expenses/{expense_id}
```

Example:

```
/expenses/1
```

Response:

```json
{
 "message":"Expense deleted successfully"
}
```

---

# 🧪 Running Tests

The project includes automated API tests using Pytest.

Run:

```bash
pytest
```

or:

```bash
python -m pytest -v
```

Example output:

```text
6 passed
```

---

# ✅ Testing Coverage

The test suite validates:

| Test Case                  | Covered |
| -------------------------- | ------- |
| Create expense             | ✅       |
| Retrieve expenses          | ✅       |
| Category filtering         | ✅       |
| Total calculation          | ✅       |
| Category total calculation | ✅       |
| Delete expense             | ✅       |

---

# 💾 Data Storage

The application uses a JSON file for persistence.

Example:

`expenses.json`

```json
[
 {
  "id":1,
  "title":"Groceries",
  "amount":500,
  "category":"Food",
  "date":"2026-08-01"
 }
]
```

The storage layer handles:

* Reading expense data
* Updating records
* Saving changes

---

# 🔒 Validation & Error Handling

The API validates:

* Empty titles
* Invalid amounts
* Duplicate expense IDs
* Missing expense records
* Invalid request formats

Example:

Duplicate ID:

```json
{
 "detail":"Expense ID already exists"
}
```

---

# 🤖 AI Usage Disclosure

This project includes an `AI_NOTES.md` file explaining:

* Where AI assistance was used
* What was modified manually
* Validation performed
* AI suggestions that were rejected

---

# 🔮 Future Improvements

Possible production enhancements:

### Database Layer

Replace JSON storage with:

* PostgreSQL
* MySQL
* MongoDB

### Authentication

Add:

* JWT authentication
* User accounts
* Role-based access

### Advanced Analytics

Add:

* Monthly expense reports
* Spending trends
* Budget alerts
* Data visualization

### Deployment

Add:

* Docker support
* CI/CD pipeline
* Cloud deployment

---

# 👨‍💻 Author

**Yash Thakur**

Computer Science Engineer

GitHub: <your-github-profile>

---

# 📄 License

This project is created for learning and demonstration purposes.
