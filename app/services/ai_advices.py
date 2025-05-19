from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class FinanceAIAdviceService:
    def __init__(self, income, expenses, period):
        self.income = income
        self.expenses = expenses
        self.period = period

    def get_openai_answer(self):
        prompt = (
            f"I have earned {self.income} USD and spent {self.expenses} USD over {self.period}. "
            f"Please give me personalized financial advice. "
            f"Help me reduce unnecessary expenses, suggest budgeting tips, and how to save more."
            f"Provide SHORT plan"
        )
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful financial advisor."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"OpenAI Error: {e}")
            return "Failed to get response from AI"
