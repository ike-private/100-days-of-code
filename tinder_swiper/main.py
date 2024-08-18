from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

FB_EMAIL = os.getenv("FB_EMAIL")
FB_PASSWORD = os.getenv("FB_PASSWORD")


#keep the browser open after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
time.sleep(2)

login = driver.find_element(By.XPATH, value='//*[@id="o2120851872"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(2)
base_window = driver.window_handles[0]

facebook_login = driver.find_element(By.XPATH, value='//*[@id="o392470796"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
facebook_login.click()
time.sleep(2)
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(2)


email = driver.find_element(By.XPATH, value='//*[@id="email"]')
email.send_keys(FB_EMAIL)

password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
password.send_keys(FB_PASSWORD)

fb_login = driver.find_element(By.ID, value='loginbutton')
fb_login.click()

driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
time.sleep(5)

#Allow location
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="o392470796"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
cookies.click()
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()


