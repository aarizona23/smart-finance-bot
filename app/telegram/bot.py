import telegram
from telegram.ext import Application, CommandHandler
from app.handlers import *
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

application = Application.builder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("add_expense", add_expense))
application.add_handler(CommandHandler("add_income", add_income))
application.add_handler(CommandHandler("remove", remove))
application.add_handler(CommandHandler("calculate", calculate))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("news", news))
application.add_handler(CommandHandler("get_AI_advice", get_ai_advice))

async def init_bot():
    await application.initialize()

async def shutdown_bot():
    await application.shutdown()

async def telegram_webhook(request):
    data = await request.json()
    update = telegram.Update.de_json(data, application.bot)
    await application.process_update(update)
    return {"ok": True}
