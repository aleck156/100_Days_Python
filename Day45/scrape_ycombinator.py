from bs4 import BeautifulSoup
import requests

URL = 'https://news.ycombinator.com/news'

res = requests.get(URL)
yc_page = res.text

soup = BeautifulSoup(yc_page, "html.parser")
print(soup.title.string)

elements = soup.find(name='span', class_='titleline')
print(elements.getText())
print(elements.find(name='a').get('href'))