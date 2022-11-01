from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://en.wikipedia.org/wiki/Main_Page'

chrome_driver_path = "/home/railgun/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)
find_number = driver.find_element(By.CSS_SELECTOR, '#articlecount a')

print(find_number.text)

driver.quit()