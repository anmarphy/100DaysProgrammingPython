from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv = Service("/Users/andrea.huerfano/Desktop/Development/chromedriver.exe")

driver = webdriver.Chrome(service=serv)
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)

article_count= driver.find_element(By.CSS_SELECTOR,"#articlecount a")
#print(article_count.text)
#article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, 'Wikipedia')
#all_portals.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys('Yoga')
search.send_keys(Keys.ENTER)



