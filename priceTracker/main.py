import smtplib
import requests
import bs4
import lxml
import os
from dotenv import load_dotenv

load_dotenv()
product_url = "https://www.amazon.co.uk/Z-Edge-Monitor-Refresh-3840x2160-Speakers/dp/B0BYZGHRS7/ref=sr_1_2?crid" \
              "=1TFTX7C33JOVJ&keywords=monitor+28+inches+with+speakers&qid=1701948032&s=instant-video&sprefix=monitor" \
              "+28+inches+with+speakers%2Cinstant-video%2C77&sr=1-2&ufe=app_do%3Aamzn1.fos.23648568-4ba5-49f2-9aa6" \
              "-31ae75f1e9cd"
r = requests.get(product_url,
                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, "
                                        "like Gecko) Chrome/116.0.0.0 Safari/537.36",
                          "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                          "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.7",
                          "sec-fetch-site": "cross-site",
                          "x-forwarded-proto":"https",
                          "x-https":"on",
                          "X-Forwarded-For":"5.69.21.85",
                          "sec-ch-ua-platform":"macOS",
                          "Accept-Encoding":"gzip, deflate, br"

})


my_email = os.getenv("TEST_GMAIL_ADDRESS")
password = os.getenv("TEST_GMAIL_PASSWORD")

soup = bs4.BeautifulSoup(r.content, 'lxml')
price = soup.find(class_="a-offscreen").get_text().split("£")[1]

BUY_PRICE = 120
if float(price) < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="janedoe@gmail.com",
                            msg=f"Subject: Monitor on sale!!! \n\n The monitor you have been watching at {product_url} is now less than £120".encode("utf-8"))

