"""Instagram Follower Bot"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
IG_ACC = ""
IG_PW = ""

class InstaFollower:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
    
    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(2)
        username_element = self.driver.find_element(By.CSS_SELECTOR, value="input[aria-label='Phone number, username, or email']")
        password_element = self.driver.find_element(By.CSS_SELECTOR, value="input[aria-label='Password']")
        login_element = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
        username_element.send_keys(IG_ACC)
        time.sleep(1)
        password_element.send_keys(IG_PW)
        login_element.click()
        time.sleep(5)
        save_info_popup = self.driver.find_element(By.CSS_SELECTOR, value='div[class="_ac8f"]')
        save_info_popup.click()
        time.sleep(2)
        enable_noti_popup = self.driver.find_element(By.CSS_SELECTOR, value='button[class="_a9-- _ap36 _a9_1"]')
        enable_noti_popup.click()

    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/followers")
        time.sleep(2)
        
        followers = self.driver.find_element(By.CSS_SELECTOR, value='button[class=" _acan _acap _acas _aj1- _ap30"]')
        time.sleep(5)
        followers.click()
        
# Instantiate the bot
bot = InstaFollower()
bot.login()
bot.find_followers()