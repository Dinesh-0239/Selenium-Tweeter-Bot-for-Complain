CHROMEDRIVER_PATH = "D:\Software\chromedriver-win64\chromedriver-win64\chromedriver.exe"
PROMISHED_DOWN = 25
PROMISHED_UP = 30
TWITTER_UNAME = "dinesh_239"
TWITTER_PASSWORD = "ridhima_arya@309"

"""
Date:- Aug 02, 2023
Developer: Dinesh Singh

Description:- I automate the tweeter bot to complain about slow internet speed after checking the internet speed then compare
it with promised speed, if it is not as per the promise then complain via tweet.

This involves zero intervention of human, means proceed automatically.

Tech used: Python's selenium module.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(executable_path=CHROMEDRIVER_PATH)
        self.option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service,options=self.option)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        sleep(3)
        go = self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        sleep(30)
        self.down = float(self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        sleep(3)
    def tweet_at_provider(self):
        if self.up < PROMISHED_UP and self.down < PROMISHED_DOWN:
            self.driver.get("https://twitter.com/i/flow/login?lang=en")
            sleep(3)
            uname = self.driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            uname.send_keys(TWITTER_UNAME)
            uname.send_keys(Keys.ENTER)
            sleep(3)
            password = self.driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            sleep(3)
            post = self.driver.find_element(by=By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span')
            post.click()
            sleep(3)
            tweet = f"Hey <@Internet Provider>, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISHED_DOWN}down/{PROMISHED_UP}up?"
            msg = self.driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            msg.send_keys(tweet)
            sleep(3)
            post_msg = self.driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
            post_msg.click()
            sleep(10)

complain = InternetSpeedTwitterBot()
complain.get_internet_speed()
complain.tweet_at_provider()
