from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

# keep the browser open after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(1)
        cookies = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        cookies.click()
        time.sleep(1)

        go_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                             '3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(50)

        download_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                  '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                                  '1]/div[1]/div/div[2]/span')
        self.down = download_speed.text
        print(self.down)

        upload_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                                '1]/div[2]/div/div[2]/span')
        self.up = upload_speed.text
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email_login = self.driver.find_element(By.XPATH,
                                               value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div['
                                                     '2]/div/div[5]/label/div/div[2]/div/input')
        email_login.send_keys(TWITTER_EMAIL)

        click_next = self.driver.find_element(By.XPATH,
                                              value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div['
                                                    '2]/div/div[6]')
        click_next.click()
        time.sleep(2)

        password_field = self.driver.find_element(By.XPATH,
                                                  value='//*[@id="react-root"]/div/div/div/main/div/div/div/div['
                                                        '2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]')
        password_field.send_keys(TWITTER_PASSWORD)

        login_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div['
                                                      '2]/div[2]/div/div/div[1]/div/div/div')
        login_button.click()
        time.sleep(2)

        tweet = self.driver.find_element(By.XPATH,
                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                               '3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                               '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                               '1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(
            f"Hey Sky, why is my internet speed {self.down} down / {self.up} up. When i pay for {PROMISED_DOWN} down / {PROMISED_UP} up")

        tweet_button = self.driver.find_element(By.XPATH, value=
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
        '2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
