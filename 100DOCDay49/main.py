from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
email = "YOUR EMAIL"
password = "YOUR PASSWORD"

# You can change the URL to whatever job postings you want to save
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3808263564&f_AL=true&geoId=101165590&keywords=Python%20Developer&location=United%20Kingdom&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"
driver.get(URL)
time.sleep(4)

# Click Sign-In option:
sign_in = driver.find_elements(By.CSS_SELECTOR, value="div a")[-2]
sign_in.click()

# Fill username and password
fill_username = driver.find_element(By.ID, value="username").send_keys(email)
fill_password = driver.find_element(By.ID, value="password").send_keys(password)

# Sign in with the username and password
second_sign_in = driver.find_element(By.CSS_SELECTOR, value="form div button")
second_sign_in.click()

# Function that clicks the save button on the job posting.
def save_job():
    save_button = driver.find_element(
    By.CLASS_NAME,
    "jobs-save-button",
    )
    save_button.click()


# By Pass Captcha:
input("Press enter to continue the script after completing the captcha: ")


# Find all the jobs
jobs_list_container = driver.find_elements(
    By.CLASS_NAME, value="job-card-container--clickable"
)

# Loop trough the jobs and save them rather than applying.
for item in jobs_list_container:
    item.click()
    time.sleep(3)
    save_job()
    time.sleep(3)
