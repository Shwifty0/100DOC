from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

email = "YOUR EMAIL"
password = "YOUR PW"

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3806661769&f_AL=true&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
driver.get(URL)
time.sleep(4)
sign_in = driver.find_elements(By.CSS_SELECTOR, value="div a")[-2]
sign_in.click()
fill_username = driver.find_element(By.ID, value="username").send_keys(email)
fill_password = driver.find_element(By.ID, value="password").send_keys(password)
second_sign_in = driver.find_element(By.CSS_SELECTOR, value="form div button")
second_sign_in.click()


jobs_list_container = driver.find_elements(By.ID, value="ember193")
apply_button = driver.find_element(By.CSS_SELECTOR, value="div.mt5 button")
apply_button.click()

submit_button = driver.find_element(By.CSS_SELECTOR, value = "form.pt4 footer button")
time.sleep(5)
submit_button.click()
# for item in jobs_list_container:
#     print(item.)






#time.sleep(10)

