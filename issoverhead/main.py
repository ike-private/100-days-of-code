import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("TEST_GMAIL_ADDRESS")
password = os.getenv("TEST_GMAIL_PASSWORD")

MY_LAT = 51.574220
MY_LONG = 0.410500

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def close_to_position():
    if round(iss_longitude) in range(round(MY_LONG - 5), round(MY_LONG + 5)) \
            and round(iss_latitude) in range(round(MY_LAT - 5), round(MY_LAT + 5)):
        return True


def look_up():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="olagunjuikeoluwa@gmail.com",
                            msg=f"Subject: LOOK UP!!! \n\n ISS Space station above, LOOK UP TO SEE IT!")


if close_to_position() and (time_now.hour > sunset or time_now.hour < sunrise):
    look_up()

close_to_position()
