from selenium import webdriver
from selenium.webdriver.common.by import By

#keep the browser open after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')

print(number.text)
driver.quit()