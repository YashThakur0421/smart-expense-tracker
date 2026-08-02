from fastapi import FastAPI, HTTPException
from src.models import Expense
from src.storage import load_expenses, save_expenses

app = FastAPI(title="Smart Expense Tracker API")


@app.get("/")
def home():
    return {"message": "Smart Expense Tracker API"}


# Add Expense
@app.post("/expenses")
def add_expense(expense: Expense):
    expenses = load_expenses()

    expenses.append(expense.model_dump(mode="json"))

    save_expenses(expenses)

    return {
        "message": "Expense added successfully",
        "expense": expense
    }


# View All Expenses
@app.get("/expenses")
def get_expenses():
    return load_expenses()


# Filter Expenses by Category
@app.get("/expenses/category/{category}")
def get_expenses_by_category(category: str):
    expenses = load_expenses()

    filtered = [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]

    return filtered


# Calculate Total Expenses
@app.get("/expenses/total")
def get_total_expenses():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    return {
        "total_expenses": total
    }


# Calculate Total Expenses by Category
@app.get("/expenses/total/{category}")
def get_total_by_category(category: str):
    expenses = load_expenses()

    total = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"].lower() == category.lower()
    )

    return {
        "category": category,
        "total_expenses": total
    }


# Delete Expense
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_expenses()

    updated_expenses = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    save_expenses(updated_expenses)

    return {
        "message": f"Expense {expense_id} deleted successfully"
    }