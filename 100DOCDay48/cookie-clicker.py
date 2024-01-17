from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to url
driver.get("https://orteil.dashnet.org/experiments/cookie/")

five_seconds = time.time() + 5
timeout = time.time() + 60 * 5
while True:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()

    if time.time() > five_seconds:
        store = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        cookie_store = {}
        for i in range(len(store)-1):
            cookie_store[f"buy{store[i].text.strip().split('-')[0].strip()}"] = int(store[i].text.strip().split("-")[1].replace(",", ""))

        # cookie price
        cookie_price = driver.find_element(By.ID, value="money")
        affordable_upgrades = {}
        for id, price in cookie_store.items():
            if int(cookie_price.text.replace(",","")) > price:
                affordable_upgrades[id] = price
        print(affordable_upgrades)
        max_upgrade = max(affordable_upgrades.values())
        print(max_upgrade)
        for k, v in affordable_upgrades.items():
            if max_upgrade == v:
                driver.find_element(By.ID, value=k).click()
        five_seconds = time.time() + 5
    
        
        if time.time() > timeout:
            cookie_per_s = driver.find_element(by=By.ID, value="cps").text
            print(cookie_per_s)
            break

driver.quit()