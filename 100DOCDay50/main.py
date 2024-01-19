from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#driver.maximize_window()

FB_EMAIL = "your email"
FB_PW = "your pw"

tinder_url = "https://tinder.com/"
driver.get(tinder_url)
#driver.maximize_window()

time.sleep(2)
cancel_cookies = driver.find_element(By.CSS_SELECTOR, value='#u1516451066 > div > div.Pos\(f\).Start\(0\).End\(0\).Z\(2\).Bxsh\(\$bxsh-4-way-spread\).B\(0\).Bgc\(\$c-ds-background-primary\).C\(\$c-ds-text-secondary\) > div > div > div.D\(f\)--ml > div:nth-child(2) > button')
cancel_cookies.click()

login = driver.find_element(By.LINK_TEXT, value='Log in')
time.sleep(2)
login.click()

time.sleep(4)
login_fb = driver.find_element(By.XPATH, value = '//*[@id="u1737791502"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
window_before = driver.window_handles[0]
login_fb.click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

time.sleep(2)
input_email = driver.find_element(By.ID, value='email').send_keys(FB_EMAIL)
time.sleep(2)
input_pass = driver.find_element(By.ID, value='pass').send_keys(FB_PW)
time.sleep(2)
log_into = driver.find_element(By.ID, value='loginbutton').click()
time.sleep(2)

input("Press enter after authentication")

driver.switch_to.window(window_before)

time.sleep(2)
allow_loc = driver.find_element(By.XPATH, value='//*[@id="u1737791502"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_loc.click()
time.sleep(2)
disable_noti = driver.find_element(By.XPATH, value='//*[@id="u1737791502"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
disable_noti.click()

for i in range(10):
    time.sleep(2)
    swipe_right = driver.find_element(By.XPATH, value='//*[@id="Tinder"]/body').send_keys(Keys.ARROW_RIGHT)
    
    
#Keys.ARROW_RIGHT