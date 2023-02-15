from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("/Users/andrea.huerfano/Desktop/Development/chromedriver.exe")

driver = webdriver.Chrome(service=serv)
URL = "https://www.python.org/"
driver.get(URL)

item_list = driver.find_elements(by=By.CSS_SELECTOR,
                                 value="div.event-widget ul.menu li")
#print(item_list)

upcoming_events = {
    item_list.index(item): {"Time": item.find_element(by=By.TAG_NAME, value="time").text,
                            "Name": item.find_element(by=By.TAG_NAME, value="a").text} for item in item_list}

print(upcoming_events)