from telegram import Update
from telegram.ext import ContextTypes
from app.services.finance_news import FinanceNewsService
from app.services.ai_advices import FinanceAIAdviceService
from app.utils.utils import get_total_calculations

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    service = FinanceNewsService()
    news_text = service.get_news()
    if not news_text:
        await update.message.reply_text("❌ No news found.")
        return

    await update.message.reply_text(news_text)

async def get_ai_advice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    if not context.args:
        period = "all"
    else:
        period = context.args[0]

    total_income, total_expenses, _ = get_total_calculations(user_id, period)
    service = FinanceAIAdviceService(total_income, total_expenses, period)
    advice_text = service.get_openai_answer()
    if not advice_text:
        await update.message.reply_text("❌ No advice found.")
        return
    await update.message.reply_text(advice_text)




