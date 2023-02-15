from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv = Service("/Users/andrea.huerfano/Desktop/Development/chromedriver.exe")

driver = webdriver.Chrome(service=serv)
URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)

def game():
    m = 1
    while m < 5:
        for _ in range(60):
            driver.find_element(By.XPATH, '//*[@id="cookie"]').click()
        print(f'{m} minutes')
        m+=1




game()





