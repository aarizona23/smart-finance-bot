💰 Smart Finance Bot
A Telegram bot to help users manage their personal finances. It supports:

Adding/removing incomes and expenses

Getting personalized financial advice (OpenAI)

Receiving daily finance news (via web scraping)

Persisting data with PostgreSQL or SQLite

Easy deployment with Docker

🚀 Features
/add_income <amount> [category] [description]: Add income

/add_expense <amount> [category] [description]: Add expense

/remove <record_id>: Remove a record

/advice <days>: Get AI advice based on your income and expenses

/news: Get latest finance news scraped from trusted sources

/summary <days>: View summary of your income and expenses

🛠 Tech Stack
Python 🐍

python-telegram-bot

FastAPI (optional webhook support)

SQLAlchemy + PostgreSQL/SQLite

OpenAI API

BeautifulSoup4 (Web scraping)

Docker + Docker Compose

🧾 Prerequisites
Python 3.11+

Telegram Bot Token (via @BotFather)

OpenAI API Key (optional)

Docker and Docker Compose (for deployment)

📁 Project Structure
bash
Copy
Edit
smart-finance-bot/
├── main.py
├── handlers/               # Telegram command handlers
├── database/               # SQLAlchemy models and DB setup
├── services/
│   ├── news.py             # Finance news scraper
│   └── advisor.py          # OpenAI advisor
├── .env                    # Secrets
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
🐳 Docker Usage
1. Create .env
env
Copy
Edit
TELEGRAM_BOT_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_key
DATABASE_URL=sqlite:///./finance.db  # or PostgreSQL URI
2. Run locally with Docker Compose
bash
Copy
Edit
docker-compose up --build
💬 Webhook Support (Optional)
If using FastAPI + webhook, expose your endpoint using ngrok:

bash
Copy
Edit
ngrok http 8000
Then set the webhook:

python
Copy
Edit
import requests
BOT_TOKEN = "your_bot_token"
WEBHOOK_URL = "https://your-ngrok-url/webhook"
requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}")
📈 Example Output
bash
Copy
Edit
/add_income 500 Freelance Website
✅ Added income #1:
💰 500 in category 'Freelance'

/advice 30
📊 OpenAI Advice:
"You’ve spent 80% of your income. Consider reducing discretionary spending..."

/news
📰 Wall Street gains ahead of earnings season
https://reuters.com/...
