from fastapi import FastAPI
from fastapi import HTTPException
from databases import SessionLocal
from models import Expense
from schemas import ExpenseCreate

app=FastAPI()

expenses = []


@app.get("/")
def home():
    return {"message": "Expense Tracker API running"}


@app.get("/expenses")
def get_expenses():
    db=SessionLocal()
    expenses=db.query(Expense).all()
    return expenses

@app.post("/expenses")
def add_expense(expense: ExpenseCreate):

    db = SessionLocal()

    db_expense = Expense(
        title=expense.title,
        amount=expense.amount
    )

    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)

    return db_expense

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    db = SessionLocal()

    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    if not expense:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    db.delete(expense)
    db.commit()

    return {
        "message": "Expense deleted successfully"
    }

@app.put("/expenses/{expense_id}")
def update_expense(
    expense_id: int,
    updated_expense: ExpenseCreate
):

    db = SessionLocal()

    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    if not expense:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    expense.title = updated_expense.title
    expense.amount = updated_expense.amount

    db.commit()
    db.refresh(expense)

    return {
        "message": "Expense updated successfully",
        "data": expense
    }