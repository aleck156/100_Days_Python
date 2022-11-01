from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/railgun/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# driver.get('https://www.amazon.com/')
# price = driver.find_element(By.NAME, 'a-price-whole')
# print(price.text)

driver.get('https://python.org/')
documentation_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
print(documentation_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}

for n in range(len(event_times)-1):
    events[n] = {
        "time": event_times[n],
        "name": event_names[n]
    }

print(events)

driver.quit()