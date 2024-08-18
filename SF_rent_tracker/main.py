from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_FORM_LINK = os.getenv("GOOGLE_FORM_LINK")
ZILLOW_URL = os.getenv("ZILLOW_URL")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


response = requests.get(ZILLOW_URL)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

links = [item['href'] for item in soup.find_all("a", attrs={'href': True, 'data-test': 'property-card-link'})]
prices = [item.text.replace('+','/').split('/',1)[0] for item in soup.find_all("span", attrs={'data-test': 'property'
                                                                                                           '-card-price'})]
addresses = [item.text.strip() for item in soup.find_all("address", attrs={'data-test': 'property-card-addr'})]


driver.get(GOOGLE_FORM_LINK)
time.sleep(4)

for i in range(len(addresses)):
    form_address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_address.send_keys(addresses[i])

    form_rent = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_rent.send_keys(prices[i])

    form_link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_link.send_keys(links[i])

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    another_one = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_one.click()
    time.sleep(1)