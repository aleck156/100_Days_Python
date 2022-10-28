from bs4 import BeautifulSoup
import requests

URL = 'https://news.ycombinator.com/news'

res = requests.get(URL)