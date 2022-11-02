import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

URL = 'http://orteil.dashnet.org/experiments/cookie/'

chrome_driver_path = "/home/railgun/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)

time.sleep(5)
cookie_item = driver.find_element(By.ID, 'cookie')

while True:
    cookie_item.click()

