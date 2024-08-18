import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("WEATHER_ENDPOINT")
API_key = os.getenv("WEATHER_API_KEY")
account_sid = os.getenv("WEATHER_ACCOUNT_SID")
auth_token = os.getenv("WEATHER_AUTH_TOKEN")
#auth_token = os.envrion.get("AUTH_TOKENS")


parameters = {
    "lat": 51.574219,
    "lon": 0.410500,
    "exclude": "current,minutely,daily",
    "appid": API_key
}

response = requests.get(endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly = weather_data['hourly']
day = hourly[:12]

will_rain = False
for hour in day:
    code = hour["weather"][0]['id']
    if int(code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today! ",
        from_='+447403933671',
        to='+447462346404'
    )
    print(message.status)


