# Expense Tracker API

A RESTful Expense Tracker backend built using FastAPI. This application allows users to create, view, update, and delete expenses while storing data in a SQLite database.

## Features

* Create new expenses
* View all expenses
* Update existing expenses
* Delete expenses
* Data persistence using SQLite
* Request validation using Pydantic

## Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy
* Pydantic
* Insomnia

## API Endpoints

### Get All Expenses

```http
GET /expenses
```

### Add Expense

```http
POST /expenses
```

Request Body:

```json
{
  "title": "Food",
  "amount": 250
}
```

### Update Expense

```http
PUT /expenses/{expense_id}
```

### Delete Expense

```http
DELETE /expenses/{expense_id}
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd expense-tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Testing

API endpoints can be tested using:

* Insomnia
* Postman
* FastAPI Swagger UI (`/docs`)

## Author

Avanthika Sreejith
