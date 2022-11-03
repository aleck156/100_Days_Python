import time
from datetime import datetime
from selenium import  webdriver
from selenium.webdriver.common.by import By

URL = 'http://orteil.dashnet.org/experiments/cookie/'

chrome_driver_path = "/home/railgun/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)

time.sleep(1)
cookie_item = driver.find_element(By.ID, 'cookie')

dt = datetime.now()
initial_time = int(datetime.timestamp(dt))

print(time)
while True:
    cookie_item.click()
    current_timestamp = int(datetime.timestamp(datetime.now()))
    if current_timestamp > initial_time + 3:
        initial_time = current_timestamp
        current_timestamp = int(datetime.timestamp(datetime.now()))

        print(f'[{current_timestamp}]: Check for new options')
        upgrade_list = driver.find_elements(By.CSS_SELECTOR, '#store div[class=""]')
        # select the most expensive one from the list - the last one, o course
        most_expensive_upgrade = upgrade_list[-1]
        most_expensive_upgrade.click()
        print(most_expensive_upgrade.text)
        print(most_expensive_upgrade.find_element(By.CSS_SELECTOR, ''))


# /html/body/div[3]/div[5]/div/div[5]/b/text()[2]
# b/text()[2]