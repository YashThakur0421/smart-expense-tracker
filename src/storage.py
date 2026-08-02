import json
from pathlib import Path


# Always points to the current src directory
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "expenses.json"


def load_expenses():
    """
    Load expenses from JSON file.
    Returns empty list if file does not exist
    or contains invalid JSON.
    """

    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    """
    Save expenses list into JSON file.
    """

    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)