from selenium import webdriver
from selenium.webdriver.common.by import By

#keep the browser open after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.co.uk/Z-Edge-Monitor-Refresh-3840x2160-Speakers/dp/B0BYZGHRS7/ref=sr_1_6?crid=20MDTQ6D3PT9N&keywords=monitor+28+inches&qid=1702308558&s=instant-video&sprefix=monitor+28+inches%2Cinstant-video%2C71&sr=1-6&ufe=app_do%3Aamzn1.fos.23648568-4ba5-49f2-9aa6-31ae75f1e9cd")

price_pounds = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_decimal = driver.find_element(By.CLASS_NAME, value="a-price-decimal").text
print(f"price is {price_pounds}.{price_decimal}")


search_bar = driver.find_element(By.NAME, value="field-keywords")
print(search_bar.tag_name)
#close a single tap
# driver.close()

#close the entire web session
driver.quit()