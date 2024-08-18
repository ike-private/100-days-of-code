import datetime as dt
import pandas as pd
import random
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("TEST_GMAIL_ADDRESS")
password = os.getenv("TEST_GMAIL_PASSWORD")
birthdays = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
day = now.day
month = now.month

templates = os.listdir("letter_templates")
for k,v in birthdays.iterrows():
    if v.month == month and v.day == day:
        template = random.choice(templates)
        with open(f"{os.getcwd()}/letter_templates/{template}", "r") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", v.recipient)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                    to_addrs=v.email,
                                    msg=f"Subject: Happy Birthday {v.recipient}!! \n\n {letter}")











