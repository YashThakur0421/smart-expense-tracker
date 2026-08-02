import json
from pathlib import Path

DATA_FILE = Path("src/expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)