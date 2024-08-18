from twilio.rest import Client
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("TEST_GMAIL_ADDRESS")
password = os.getenv("TEST_GMAIL_PASSWORD")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Encrypt message before sending incase it is intercepted in transmission
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8'))
