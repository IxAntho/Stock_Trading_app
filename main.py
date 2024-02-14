import requests
from datetime import datetime, timedelta
from twilio.rest import Client

# Day before yesterday's date
db_yesterday_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')

# Get yesterday's date
yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

# Stock API tools
STOCK = "TSLA"
COMPANY_NAME = "tesla"
STOCK_API_KEY = "L0POZSOSEA1A72X0"
STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

# News API tools
NEWS_API_KEY = "3a729889d6de45599c8b233890dba015"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-14&sortBy=publishedAt&apiKey=3a729889d6de45599c8b233890dba015"

# Twilio API tools
ACCOUNT_SID = "AC4d533db3a87b0a2f43da993e2ef02faf"
AUTH_TOKEN = "4c559637bd9d9beaeea5d619483eaf78"


def calculate_percentage_change():
    response = requests.get(url=STOCK_API_ENDPOINT, params=STOCK_PARAMETERS)
    data = response.json()
    yesterday_close = float(data["Time Series (Daily)"][f"{yesterday_date}"]["4. close"])
    db_yesterday_close = float(data["Time Series (Daily)"][f"{db_yesterday_date}"]["4. close"])
    percentage_change = ((yesterday_close - db_yesterday_close) / db_yesterday_close) * 100
    # if percentage_change >= 5 or percentage_change <= 5:
    #     print("Get News!")
    if percentage_change > 0:
        return f"🔺{round(percentage_change, 4)}%"
    else:
        return f"🔻{round(percentage_change, 4)}%"


def get_news():
    response = requests.get(url=NEWS_API_ENDPOINT)
    data = response.json()
    articles = data["articles"]
    news = []
    for i in range(0, 3):
        title = articles[i]["title"]
        description = articles[i]["description"]
        new = {
            "headline": title,
            "brief": description,
        }
        news.append(new)
    return news


def send_message(percentage, news):
    new_1 = f"Headline: {news[0]['headline']}.\nBrief: {news[0]['brief']}."
    new_2 = f"Headline: {news[1]['headline']}.\nBrief: {news[1]['brief']}."
    new_3 = f"Headline: {news[2]['headline']}.\nBrief: {news[2]['brief']}."
    body_message = f"TSLA: {percentage}\n{new_1}\n{new_2}\n{new_3}"

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_='+15077347375',
        body=f'{body_message}',
        to='+50245064076'
    )
    print(message)


def is_weekend():
    # Get today's day of the week (0: Monday, 1: Tuesday, ..., 6: Sunday)
    today = datetime.now().weekday()

    # Check if today is Saturday (5), Sunday (6) or Monday (0)
    if today == 5 or today == 6 or today == 0:
        return True
    else:
        return False


def stock_trading_app():
    percentage = calculate_percentage_change()
    tesla_news = get_news()
    send_message(percentage, tesla_news)


if not is_weekend():
    stock_trading_app()
