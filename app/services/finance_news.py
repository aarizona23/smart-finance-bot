import requests
from bs4 import BeautifulSoup

class FinanceNewsService:
    def __init__(self):
        self.news = self.fetch_news()

    @staticmethod
    def fetch_news():
        url = "https://www.reuters.com/business/finance/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching news: {e}")
            return []
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = []
        div_content = soup.find("div", {"data-testid": "MainContent"})
        if not div_content:
            return []

        div1_content = div_content.find("div", {"data-testid": "Topic"})
        ul = div1_content.find("ul")
        if not ul:
            return []
        for li in ul.find_all("li", limit=3):
            h3 = li.find("h3", {"data-testid": "Heading"})
            a = h3.find("a") if h3 else None
            if a:
                title = a.get_text(strip=True)
                link = a.get("href", "")
                if not link.startswith("http"):
                    link = "https://www.reuters.com" + link
                news_list.append({"title": title, "link": link})

        return news_list

    def get_news(self):
        news_text = "📈 Latest Finance News:\n\n"
        for article in self.news:
            news_text += f"📰 {article['title']}\n{article['link']}\n\n"
        return news_text