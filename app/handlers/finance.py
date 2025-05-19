from telegram import Update
from telegram.ext import ContextTypes
from app.models.finance import FinanceRecord
from app.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime

from app.utils.utils import get_total_calculations

async def add_record(update: Update, context: ContextTypes.DEFAULT_TYPE, record_type: str):
    user_id = str(update.effective_user.id)

    if not context.args:
        await update.message.reply_text("❌ Please provide an amount. Usage: /add <amount> [category] [description]")
        return

    try:
        amount = float(context.args[0])
    except ValueError:
        await update.message.reply_text("❌ Amount must be a number.")
        return

    category = context.args[1] if len(context.args) > 1 else "Uncategorized"
    description = " ".join(context.args[2:]) if len(context.args) > 2 else None

    db: Session = next(get_db())
    record = FinanceRecord(
        user_id=user_id,
        amount=amount,
        type=record_type,
        category=category,
        description=description if description else None,
        timestamp=datetime.utcnow()
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    await update.message.reply_text(
        f"✅ Added {record_type} #{record.id}:\n💸 {amount} in category '{category}'"
    )

async def add_income(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await add_record(update, context, "income")

async def add_expense(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await add_record(update, context, "expense")

async def remove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Please provide a record ID. Usage: /remove <record_id>")
        return

    record_id = context.args[0]
    db: Session = next(get_db())
    record = db.query(FinanceRecord).filter(FinanceRecord.id == record_id).first()

    if record:
        db.delete(record)
        db.commit()
        await update.message.reply_text(f"✅ Removed record with ID: {record_id}")
    else:
        await update.message.reply_text(f"❌ Record with ID {record_id} not found.")

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if not context.args:
        period = "all"
    else:
        period = context.args[0]
    total_income, total_expenses, total_remainder = get_total_calculations(user_id, period)

    await update.message.reply_text(
        f"📊 Your financial summary:\n"
        f"💰 Total Income Records: {total_income}\n"
        f"💸 Total Expense Records: {total_expenses}\n"
        f"💵 Total Remainder: {total_remainder}\n"
    )
