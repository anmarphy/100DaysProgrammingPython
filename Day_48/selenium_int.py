from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("/Users/andrea.huerfano/Desktop/Development/chromedriver.exe")

driver = webdriver.Chrome(service=serv)
"""URL = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/"
driver.get(URL)

values = driver.find_element(By.ID, "attach-base-product-price")
print(values.get_attribute('value'))
driver.quit()"""

URL = "https://www.python.org/"
driver.get(URL)
#logo=driver.find_element(By.CLASS_NAME, 'python-logo')
#print(logo)

bug_link = driver.find_element(By.XPATH,'//*[@id="container"]/li[4]/ul/li[4]/a')
print(bug_link.text)