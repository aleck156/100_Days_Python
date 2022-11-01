from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

URL = 'https://en.wikipedia.org/wiki/Main_Page'

chrome_driver_path = "/home/railgun/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)
article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(article_count.text)
article_count.click()

search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

# driver.quit()