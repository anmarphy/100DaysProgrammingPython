from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://www.linkedin.com/home'
EMAIL = 'my_email'
PASSWORD = 'my_password'
serv = Service("/Users/andrea.huerfano/Desktop/Development/chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.get(URL)
login_email = driver.find_element(By.XPATH, '//*[@id="session_key"]')
login_email.send_keys(EMAIL)

login_password = driver.find_element(By.NAME, 'session_password')
login_password.send_keys(PASSWORD)

driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button' ).click()






driver.quit()