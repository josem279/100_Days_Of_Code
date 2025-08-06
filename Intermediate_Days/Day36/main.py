import requests
import os
from collections import defaultdict
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHA_API_KEY = os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
TWILIO_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]

alpha_url = STOCK_ENDPOINT
alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_API_KEY}

yesterday = datetime.date(datetime.now() - timedelta(days=1))
day_before = datetime.date(datetime.now() - timedelta(days=2))

alpha_response = requests.get(alpha_url, params=alpha_params)
alpha_data = alpha_response.json()

yest_closing = float(alpha_data['Time Series (Daily)'][str(yesterday)]['4. close'])
day_before_closing = float(alpha_data['Time Series (Daily)'][str(day_before)]['4. close'])

pct_delta = (yest_closing - day_before_closing) / day_before_closing * 100

news_url = NEWS_ENDPOINT
news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}



if abs(pct_delta) > 0:
    news_response = requests.get(url=news_url, params=news_params)
    news_data = news_response.json()
    most_recent_3 = news_data["articles"][:3]
    
    formatted_articles = [f"Headline: {article["title"]}. \nBrief: {article["description"]}" for article in most_recent_3]
    
print(formatted_articles)


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body= article,
        from_=TWILIO_NUMBER,
        to= "YOUR PHONE NUMBER",
    )