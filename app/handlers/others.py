from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Smart Finance Bot!\nUse /add to log expenses.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/add <amount> [category] [description] - Add an expense or an income\n"
        "/remove <record_id> - Remove a record\n"
        "/calculate - Calculate total expenses and income\n"
        "/help - Show this help message\n"
        "/news - Get the latest news\n"
        "/get_ai_advice - Get AI advice\n"
    )
    await update.message.reply_text(help_text)