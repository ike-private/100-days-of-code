import unicodedata

import requests
from datetime import date, timedelta
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")
API_KEY_NEWS = os.getenv("API_KEY_NEWS ")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
auth_token = os.getenv("STOCK_AUTH_TOKEN")
account_sid = os.getenv("STOCK_ACCOUNT_SID")

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY
}
yesterday = date.today() - timedelta(days = 1)
day_before_yesterday = date.today() - timedelta(days = 2)

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

yesterday_close = float(stock_data[str(yesterday)]["4. close"])
day_before_yesterday_close = float(stock_data[str(day_before_yesterday)]["4. close"])
difference = day_before_yesterday_close - yesterday_close
difference = abs(difference)
five_percent_of_day_before_yesterdays = 0.05 * day_before_yesterday_close

news_parameters = {
    "apiKey" : API_KEY_NEWS,
    "qInTitle" : COMPANY_NAME,
    "from" : yesterday
}

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
articles = news_data["articles"][:3]
titles = [unicodedata.normalize("NFKD",a["title"]) for a in articles]
client = Client(account_sid, auth_token)
print(titles)
if difference > five_percent_of_day_before_yesterdays :
    for t in titles:
        message = client.messages.create(
            body=t,
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),
            to=os.getenv("TWILIO_VERIFIED_NUMBER")
        )

