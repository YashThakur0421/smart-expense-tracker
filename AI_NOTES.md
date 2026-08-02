# AI Usage Notes

## AI Tools Used

* ChatGPT

AI assistance was used during development for understanding implementation approaches, generating initial code structure, reviewing code quality, and improving documentation.

---

# AI Generated Components

The following parts were initially generated with AI assistance:

* FastAPI project structure suggestion
* Initial API endpoint implementation ideas
* Pytest test case structure
* README documentation template
* Error handling suggestions

---

# My Contributions and Changes

I reviewed, modified, and validated all generated content before using it.

My implementation work included:

* Setting up the FastAPI application
* Creating API routes for expense operations
* Implementing JSON-based storage handling
* Adding request validation using Pydantic models
* Handling duplicate expense IDs
* Implementing category filtering logic
* Implementing total expense calculations
* Implementing delete functionality
* Writing and executing API tests
* Debugging and fixing issues during development

---

# Validation and Testing

I verified the application by:

* Running the API locally using Uvicorn
* Testing endpoints using Swagger UI
* Running automated tests using Pytest

Test scenarios covered:

* Creating an expense
* Fetching all expenses
* Filtering expenses by category
* Calculating total expenses
* Calculating category-wise totals
* Deleting expenses

Final test result:

```
6 passed
```

---

# AI Suggestions Not Used

Some AI suggestions were intentionally not implemented:

### Database Integration

A database approach was considered, but JSON file storage was selected because:

* The assignment explicitly allowed local file storage.
* It keeps the implementation simple and focused.
* It avoids unnecessary setup complexity.

### Authentication

Authentication was not added because:

* The assignment focuses on expense management functionality.
* User management was outside the requested scope.

---

# Final Review

All AI-assisted code was reviewed, understood, tested, and modified where required.

AI was used as a development assistant, while the final implementation decisions and validation were performed manually.
