import time
import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "/Users/andrea.huerfano/Desktop/Development/chromedriver.exe"
serv = Service(CHROME_DRIVER_PATH)

URL = "https://www.instagram.com/"
ACCOUNT_TARGET='camilaberval'

def find_button_text_index(buttons, text) -> int:
    index = 0
    for button in buttons:
        if button.text == text:
            return index
        else:
            index += 1


class InstaFollower():

    def __init__(self):
        self.driver = webdriver.Chrome(service=serv)

    def click_tag_with_text(self, tag: str, text: str):
        """Clicks on the tag which has the given text in it, if text is not found it does nothing."""

        index = 0
        tags = self.driver.find_elements(by=By.TAG_NAME, value=tag)
        for tag in tags:
            if text in tag.text:
                time.sleep(5)
                tags[index].click()
                break
            else:
                index += 1

    def login(self):

        EMAIL = os.environ.get('my_phone')
        PASSWORD = os.environ.get('my_ig_pass')

        self.driver.get(URL)
        time.sleep(10)
        login_email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_email.send_keys(EMAIL)
        time.sleep(3)
        login_password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_password.send_keys(PASSWORD)
        time.sleep(3)
        buttons = self.driver.find_elements(by=By.TAG_NAME, value="button")
        buttons[find_button_text_index(buttons, "Log in")].click()
        time.sleep(10)

        ##Save credentials
        buttons = self.driver.find_elements(by=By.TAG_NAME, value="button")
        buttons[find_button_text_index(buttons , "Not Now")].click()
        time.sleep(5)

        ##Notifications
        self.click_tag_with_text("button", "Not Now")
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f'{URL}{ACCOUNT_TARGET}/followers')
        time.sleep(5)

    def follow(self):
        list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, 'button')
        for item in list_of_followers:
            if item.text == "Follow":
                print("click")
                item.click()
                time.sleep(random.randint(1, 2))
                list_of_followers.append(self.driver.find_elements(By.CSS_SELECTOR, 'button'))

            else:
                print('Already following')



bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()