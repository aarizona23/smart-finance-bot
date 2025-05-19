# 💰 Smart Finance Bot

A Telegram bot that helps users track their finances, get AI-generated financial advice, and stay updated with the latest finance news.

---

## 🚀 Features

- `/add_income <amount> [category] [description]` — Add income
- `/add_expense <amount> [category] [description]` — Add expense
- `/remove <record_id>` — Remove a financial record
- `/advice <days>` — Get financial advice based on last N days
- `/news` — Get the latest finance news
- `/summary <days>` — View a summary of incomes and expenses

---

## 🛠 Tech Stack

- FastAPI
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- SQLAlchemy
- PostgreSQL / SQLite
- OpenAI (for advice)
- BeautifulSoup (for scraping news)
- Docker + Docker Compose

