# scraping the list of 100 greatest movies of all times
from bs4 import BeautifulSoup
import requests

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

res = requests.get(URL)

print(res.text)
