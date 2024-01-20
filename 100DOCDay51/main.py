from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math
"""
1. Get the Up/Down speed from speedtest.com
2. Log in to Twitter if the Down/Up speeds are less
3. Tweet.
"""
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_ACCOUNT = "YOUR X ACC"
TWITTER_PW = "YOUR PW"


class TwitterBot:
    def __init__(self) -> None:
        self.down = 0
        self.up = 0
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
    
    def get_internetSpeed(self):
        speed_test_url = "https://www.speedtest.net/"
        self.driver.get(speed_test_url)
        go_button = self.driver.find_element(By.CSS_SELECTOR, value='span.start-text')
        go_button.click()
        
        time.sleep(40)
        
        down_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        
        pop_up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button') 
        if pop_up:
            pop_up.click()
        
        self.down = math.floor(float(down_speed))
        self.up = math.floor(float(up_speed))

    def tweet_at_provider(self, tweet):
            speed_test_url = "https://www.twitter.com/"
            self.driver.get(speed_test_url)
            
            time.sleep(2)
            
            sign_in = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
            sign_in.click()
            
            time.sleep(5)
            
            self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(TWITTER_ACCOUNT)
            time.sleep(2)
            self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(Keys.ENTER)
            time.sleep(2)
            self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(TWITTER_PW)
            time.sleep(2)
            self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(Keys.ENTER)
            
            for i in range(10):
                time.sleep(3)
                self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(f"{tweet}({i+1})")
                time.sleep(4)
                post = self.driver.find_element(By.CSS_SELECTOR, value='div[data-testid="tweetButtonInline"]')
                post.click()

bot = TwitterBot()
print("Getting your download speed:")
bot.get_internetSpeed()
print(f"Down:{bot.down}\nUp:{bot.up}")


if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    TWEET = f"Hey! ISP, why my internet speed is -> {bot.down}Mbps/{bot.up}Mbps, when I pay for {PROMISED_DOWN}Mbps/{PROMISED_UP}Mbps"
    print(f"Whoopsie! {bot.down} < {PROMISED_DOWN} = {bot.down < PROMISED_DOWN}\n{bot.up} < {PROMISED_UP} = {bot.up < PROMISED_UP}")
    bot.tweet_at_provider(TWEET)