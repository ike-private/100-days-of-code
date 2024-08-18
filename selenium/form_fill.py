from selenium import webdriver
from selenium.webdriver.common.by import By

#keep the browser open after execution

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, value='fName')
fname.send_keys("Ike")

lname = driver.find_element(By.NAME, value='lName')
lname.send_keys("olag")

email = driver.find_element(By.NAME, value='email')
email.send_keys("Ike@test.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()


driver.quit()