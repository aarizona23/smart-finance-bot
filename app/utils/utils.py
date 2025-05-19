from datetime import datetime, timedelta
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.finance import FinanceRecord
from app.database import get_db

def get_total_calculations(user_id, period):
    db: Session = next(get_db())
    if period == "today":
        start_date = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = datetime.utcnow().replace(hour=23, minute=59, second=59, microsecond=999999)
    elif period == "week":
        start_date = datetime.utcnow() - timedelta(days=7)
        end_date = datetime.utcnow()
    elif period == "month":
        start_date = datetime.utcnow() - timedelta(days=30)
        end_date = datetime.utcnow()
    else:
        start_date = datetime(1970, 1, 1)
        end_date = datetime.utcnow()

    total_income = db.query(func.sum(FinanceRecord.amount)).filter(
        FinanceRecord.user_id == user_id,
        FinanceRecord.type == "income",
        FinanceRecord.timestamp >= start_date,
        FinanceRecord.timestamp <= end_date
    ).scalar() or 0.0

    total_expenses = db.query(func.sum(FinanceRecord.amount)).filter(
        FinanceRecord.user_id == user_id,
        FinanceRecord.type == "expense",
        FinanceRecord.timestamp >= start_date,
        FinanceRecord.timestamp <= end_date
    ).scalar() or 0.0

    total_remainder = total_income - total_expenses

    return total_income, total_expenses, total_remainder