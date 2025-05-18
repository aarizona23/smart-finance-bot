from fastapi import FastAPI, Request
from app.telegram.bot import telegram_webhook, init_bot, shutdown_bot

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_bot()

@app.on_event("shutdown")
async def shutdown():
    await shutdown_bot()

@app.post("/webhook")
async def telegram_webhook_handler(request: Request):
    return await telegram_webhook(request)
