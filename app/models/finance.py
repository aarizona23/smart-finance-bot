from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from app.database import Base
from sqlalchemy import CheckConstraint

class FinanceRecord(Base):
    __tablename__ = "finance_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)  # Telegram user ID
    amount = Column(Float)
    type = Column(String)  # 'income' or 'expense'
    category = Column(String)
    description = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        CheckConstraint("type IN ('income', 'expense')", name="check_record_type"),
    )