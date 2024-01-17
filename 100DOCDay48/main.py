# Selenium Web Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org") 
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

dates = [event.get_attribute("datetime").split("T")[0] for event in events]
names = [name.text for name in event_names]

event_dict = {}
for i in range(len(dates)):
    event_dict[i] = {"time":dates[i], "name":names[i]}
print(event_dict)
driver.quit()
