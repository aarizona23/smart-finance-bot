from fastapi import FastAPI, Request
from app.telegram.bot import telegram_webhook

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook_handler(request: Request):
    return await telegram_webhook(request)
