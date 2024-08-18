from selenium import webdriver
from selenium.webdriver.common.by import By

#keep the browser open after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

dates = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul').text
dates = dates.split("\n")
events = {}
output = {}
index = 0
for element in dates:
    if index % 2 == 0:
        events[int(index/2)] = output
        output["time"] = element
    else:
        output["name"] = element

    index+=1

print(events)

driver.quit()