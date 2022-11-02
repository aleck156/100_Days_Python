from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://secure-retreat-92358.herokuapp.com'

chrome_driver_path = "/home/railgun/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)

first_name = driver.find_element(By.CSS_SELECTOR, '.top')
last_name = driver.find_element(By.CSS_SELECTOR, '.middle')
email_address = driver.find_element(By.CSS_SELECTOR, '.bottom')

first_name.send_keys('Thomas')
last_name.send_keys('Anderson')
email_address.send_keys('neo@gmail.com')

first_name.send_keys(Keys.ENTER)